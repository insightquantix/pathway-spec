#!/usr/bin/env python3
"""
Pathway Specification Validator (v0.1)

Basic validation tool for Insight Quantix Pathway Specification YAML files.

This is a reference implementation demonstrating validation concepts.
It performs basic structure and consistency checks but is not comprehensive.

Usage:
    python validate_pathway.py pathway.yaml

Requirements:
    pip install pyyaml
"""

import sys
import yaml
from pathlib import Path
from typing import Dict, List, Any, Optional

class PathwayValidator:
    """Validates pathway YAML files against specification requirements."""

    def __init__(self, filepath: str):
        self.filepath = Path(filepath)
        self.pathway: Dict[str, Any] = {}
        self.errors: List[str] = []
        self.warnings: List[str] = []

    def load(self) -> bool:
        """Load and parse YAML file."""
        try:
            with open(self.filepath, 'r', encoding='utf-8') as f:
                self.pathway = yaml.safe_load(f)
            return True
        except FileNotFoundError:
            self.errors.append(f"File not found: {self.filepath}")
            return False
        except yaml.YAMLError as e:
            self.errors.append(f"YAML syntax error: {e}")
            return False

    def validate_structure(self) -> None:
        """Check for required top-level sections."""
        required_sections = ['meta', 'feedstocks', 'products', 'units']

        for section in required_sections:
            if section not in self.pathway:
                self.errors.append(f"Missing required section: '{section}'")

        # Check for recommended sections
        recommended_sections = ['balances', 'tea', 'lca']
        for section in recommended_sections:
            if section not in self.pathway:
                self.warnings.append(f"Missing recommended section: '{section}'")

    def validate_meta(self) -> None:
        """Validate meta section fields."""
        if 'meta' not in self.pathway:
            return

        meta = self.pathway['meta']
        required_meta_fields = ['name', 'version', 'functional_unit', 'boundary']

        for field in required_meta_fields:
            if field not in meta:
                self.errors.append(f"Missing required meta field: 'meta.{field}'")

        # Check version format (basic check)
        if 'version' in meta:
            version = str(meta['version'])
            parts = version.split('.')
            if len(parts) < 2:
                self.warnings.append(f"Version '{version}' should follow semantic versioning (MAJOR.MINOR.PATCH)")

    def validate_feedstocks(self) -> None:
        """Validate feedstocks section."""
        if 'feedstocks' not in self.pathway:
            return

        feedstocks = self.pathway['feedstocks']

        if not feedstocks:
            self.warnings.append("Feedstocks section is empty")
            return

        for feedstock_id, feedstock in feedstocks.items():
            if not isinstance(feedstock, dict):
                self.errors.append(f"Feedstock '{feedstock_id}' must be a dictionary")
                continue

            # Check for name field
            if 'name' not in feedstock:
                self.warnings.append(f"Feedstock '{feedstock_id}' missing 'name' field")

    def validate_products(self) -> None:
        """Validate products section."""
        if 'products' not in self.pathway:
            return

        products = self.pathway['products']

        if not products:
            self.errors.append("Products section is empty (must define at least one product)")
            return

        for product_id, product in products.items():
            if not isinstance(product, dict):
                self.errors.append(f"Product '{product_id}' must be a dictionary")
                continue

            if 'name' not in product:
                self.warnings.append(f"Product '{product_id}' missing 'name' field")

    def validate_streams(self) -> None:
        """Validate streams and their connectivity."""
        if 'streams' not in self.pathway:
            return

        streams = self.pathway['streams']
        if not streams:
            return

        unit_ids = set(self.pathway.get('units', {}).keys())

        for stream_id, stream in streams.items():
            if not isinstance(stream, dict):
                self.errors.append(f"Stream '{stream_id}' must be a dictionary")
                continue

            # Check stream connectivity
            from_unit = stream.get('from_unit')
            to_unit = stream.get('to_unit')

            if from_unit and from_unit not in unit_ids:
                self.errors.append(f"Stream '{stream_id}' references undefined unit '{from_unit}' in from_unit")

            if to_unit and to_unit not in unit_ids:
                self.errors.append(f"Stream '{stream_id}' references undefined unit '{to_unit}' in to_unit")

    def validate_units(self) -> None:
        """Validate unit operations."""
        if 'units' not in self.pathway:
            return

        units = self.pathway['units']
        if not units:
            self.errors.append("Units section is empty (must define at least one unit)")
            return

        stream_ids = set(self.pathway.get('streams', {}).keys())

        for unit_id, unit in units.items():
            if not isinstance(unit, dict):
                self.errors.append(f"Unit '{unit_id}' must be a dictionary")
                continue

            # Check for inputs and outputs
            inputs = unit.get('inputs', [])
            outputs = unit.get('outputs', [])

            if not inputs and not outputs:
                self.warnings.append(f"Unit '{unit_id}' has no inputs or outputs defined")

            # Check that referenced streams exist
            for stream_ref in inputs:
                if stream_ref not in stream_ids:
                    self.warnings.append(f"Unit '{unit_id}' references undefined input stream '{stream_ref}'")

            for stream_ref in outputs:
                if stream_ref not in stream_ids:
                    self.warnings.append(f"Unit '{unit_id}' references undefined output stream '{stream_ref}'")

    def validate_balances(self) -> Optional[Dict[str, float]]:
        """Validate mass and energy balances if present."""
        if 'balances' not in self.pathway:
            return None

        balances = self.pathway['balances']
        results = {}

        # Mass balance
        if 'mass_balance' in balances:
            mb = balances['mass_balance']
            if 'closure' in mb:
                closure_val = mb['closure'].get('value')
                if closure_val:
                    results['mass_balance'] = closure_val
                    if abs(closure_val - 100.0) > 1.0:
                        self.warnings.append(f"Mass balance closure is {closure_val}% (outside typical ±1% tolerance)")

        # Energy balance
        if 'energy_balance' in balances:
            eb = balances['energy_balance']
            if 'closure' in eb:
                closure_val = eb['closure'].get('value')
                if closure_val:
                    results['energy_balance'] = closure_val
                    if abs(closure_val - 100.0) > 2.0:
                        self.warnings.append(f"Energy balance closure is {closure_val}% (outside typical ±2% tolerance)")

        return results if results else None

    def extract_validation_warnings(self) -> None:
        """Extract warnings from pathway validation section if present."""
        if 'validation' in self.pathway:
            pathway_warnings = self.pathway['validation'].get('warnings', [])
            for warning in pathway_warnings:
                self.warnings.append(f"Pathway warning: {warning}")

    def validate(self) -> bool:
        """Run all validation checks."""
        if not self.load():
            return False

        self.validate_structure()
        self.validate_meta()
        self.validate_feedstocks()
        self.validate_products()
        self.validate_streams()
        self.validate_units()
        self.validate_balances()
        self.extract_validation_warnings()

        return len(self.errors) == 0

    def print_results(self) -> None:
        """Print validation results to console."""
        print("\n" + "="*70)
        print(f"Pathway Validation: {self.filepath.name}")
        print("="*70 + "\n")

        # Errors
        if self.errors:
            print("❌ ERRORS:")
            for error in self.errors:
                print(f"  - {error}")
            print()
        else:
            print("✓ No structural errors found\n")

        # Warnings
        if self.warnings:
            print("⚠  WARNINGS:")
            for warning in self.warnings:
                print(f"  - {warning}")
            print()
        else:
            print("✓ No warnings\n")

        # Summary information
        if not self.errors:
            print("SUMMARY:")

            meta = self.pathway.get('meta', {})
            print(f"  Name: {meta.get('name', 'N/A')}")
            print(f"  Version: {meta.get('version', 'N/A')}")
            print(f"  Functional Unit: {meta.get('functional_unit', 'N/A')}")

            feedstocks = self.pathway.get('feedstocks', {})
            print(f"  Feedstocks: {len(feedstocks)}")

            products = self.pathway.get('products', {})
            print(f"  Products: {', '.join(products.keys()) if products else 'None'}")

            units = self.pathway.get('units', {})
            print(f"  Units: {len(units)}")

            # Balance results
            balances = self.validate_balances()
            if balances:
                if 'mass_balance' in balances:
                    print(f"  Mass Balance Closure: {balances['mass_balance']:.1f}%")
                if 'energy_balance' in balances:
                    print(f"  Energy Balance Closure: {balances['energy_balance']:.1f}%")

            # LCA results if present
            lca = self.pathway.get('lca', {})
            if 'impact_results' in lca:
                impacts = lca['impact_results']
                if 'climate_change' in impacts:
                    cc = impacts['climate_change']
                    print(f"  Carbon Intensity: {cc.get('value')} {cc.get('unit')}")

            print()

        # Final verdict
        print("-"*70)
        if self.errors:
            print("❌ VALIDATION FAILED")
            print(f"   {len(self.errors)} error(s) must be fixed")
        else:
            print("✓ VALIDATION PASSED")
            if self.warnings:
                print(f"   {len(self.warnings)} warning(s) for review")
        print("="*70 + "\n")

        return len(self.errors) == 0


def main():
    """Main entry point."""
    if len(sys.argv) != 2:
        print("Usage: python validate_pathway.py pathway.yaml")
        print("\nExample:")
        print("  python validate_pathway.py pathways/demo_hefa_base.yaml")
        sys.exit(1)

    filepath = sys.argv[1]
    validator = PathwayValidator(filepath)

    success = validator.validate()
    validator.print_results()

    # Exit with appropriate code
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
