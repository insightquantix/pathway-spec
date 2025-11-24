# Insight Quantix Pathway Specification

**A proposed open configuration format for techno-economic and life-cycle assessment models**

[![Spec Version](https://img.shields.io/badge/version-v0.5--draft-yellow)](https://github.com/insightquantix/pathway-spec)
[![License](https://img.shields.io/badge/license-Apache_2.0-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.10+-blue)](https://www.python.org/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)

---

## Motivation: Why This Specification Exists

For more than a decade, TEA and LCA modeling has relied on spreadsheets, PDFs, and proprietary tools that make assumptions opaque and studies difficult to reproduce. As models like hydrogen, SAF, electrofuels, ammonia, CCUS become more complex, the limitations of legacy formats prevent automation, collaboration, and transparency.

**The Insight Quantix Pathway Specification proposes a modern alternative**: a human-readable, version-controlled, machine-parseable configuration format for TEA/LCA pathways. The goal is not to replace existing tools, but to give the field a shared language for defining pathways—one that is transparent, auditable, extensible, and compatible with automation workflows and modern software ecosystems.

This draft reflects ongoing work toward an open, community-driven standard. Our goal is to align with best practices from NREL, Argonne, ASTM, and ISO while enabling modern software integration.

---

## Overview

This repository contains a **development draft** of a structured YAML format for representing techno-economic analysis (TEA) and life-cycle assessment (LCA) pathway models.

**Status**: v0.5 draft. Seeking validation, peer review, and community collaboration.

**Purpose**: Provide a reproducible, version-controlled, transparent alternative to spreadsheet-based and proprietary TEA/LCA models.

**Scope**: Currently focused on renewable fuel pathways (SAF, hydrogen, ammonia, electrofuels). Designed to be extensible to other process industries.

---

## Conceptual Model

```
Pathway
 ├── meta                    # Scope definition & metadata
 ├── feedstocks              # Input materials & properties
 ├── products                # Output products & specifications
 ├── streams                 # Material/energy flows
 ├── units                   # Process operations
 │    ├── pretreatment
 │    ├── reactor
 │    ├── separation
 │    └── utilities
 ├── balances                # Mass/energy closure
 ├── tea                     # Techno-economic analysis
 │    ├── capex
 │    ├── opex
 │    └── financials
 └── lca                     # Life-cycle assessment
      ├── allocation
      ├── emission_factors
      └── impact_results
```

Each pathway explicitly defines feedstocks, unit operations, material/energy flows, economics, and environmental impacts in a structured, auditable format that integrates TEA and LCA seamlessly.

---

## Design Goals

This specification is built around six core principles:

1. **Transparency**: All assumptions and data sources explicitly documented
2. **Reproducibility**: Version-controlled configurations enable exact replication
3. **Modularity**: Reusable components (feedstocks, units, streams) across pathways
4. **Interoperability**: Designed to complement GREET, OpenLCA, Ecoinvent, Aspen Plus
5. **Auditability**: Clear traceability for regulatory and peer review
6. **Automation**: Machine-readable format enables scenario generation and optimization

---

## Problem Statement

Techno-economic and life-cycle assessment studies in clean energy face reproducibility challenges:

- **Non-transparent assumptions**: Spreadsheet models hide calculation logic and data sources
- **No version control**: Changes to models are poorly documented
- **Manual processes**: Scenario analysis requires manual file duplication and editing
- **Proprietary lock-in**: Many models exist only in commercial software packages
- **Limited automation**: Difficult to integrate with CI/CD, optimization tools, or AI workflows

These limitations create barriers to peer review, regulatory acceptance, and collaborative development.

---

## Proposed Solution

A structured YAML format that explicitly defines:

- Feedstock sources and properties
- Process unit operations and their connections
- Material and energy streams
- Capital and operating cost structures
- Life-cycle emission factors and allocation methods
- System boundaries and functional units

**Example structure** (simplified - see `pathways/demo_hefa_base.yaml` for complete pathway):
```yaml
meta:
  name: "HEFA Jet Fuel Production"
  version: "1.0"
  functional_unit: "MJ jet fuel (LHV)"
  boundary: "cradle-to-gate"
  reference_year: 2024

feedstocks:
  soybean_oil:
    name: "Soybean Oil"
    lhv: {value: 37.5, unit: "MJ/kg"}
    cost: {value: 800, unit: "USD/tonne"}
  hydrogen:
    name: "Hydrogen (SMR)"
    cost: {value: 2.50, unit: "USD/kg"}

products:
  saf_jet:
    name: "Sustainable Aviation Fuel"
    specification: "ASTM D7566 Annex A2"
    lhv: {value: 43.2, unit: "MJ/kg"}
  renewable_diesel:
    name: "Renewable Diesel (co-product)"
    lhv: {value: 44.0, unit: "MJ/kg"}

units:
  hydrotreater:
    name: "Hydrotreating Reactor"
    type: "fixed_bed_reactor"
    operating_conditions:
      temperature: {value: 350, unit: "C"}
      pressure: {value: 80, unit: "bar"}
    conversion:
      triglycerides: 0.98

tea:
  plant_capacity:
    feedstock_input: {value: 100000, unit: "tonnes/year"}
    jet_output: {value: 45000, unit: "tonnes/year"}
    capacity_factor: {value: 0.90, unit: "fraction"}

  capex:
    total_installed: {value: 210, unit: "MM USD"}
    breakdown:
      process_units: {value: 145, unit: "MM USD"}
      utilities: {value: 25, unit: "MM USD"}
      contingency: {value: 30, unit: "MM USD"}

  opex:
    variable_costs:
      feedstock: {value: 80, unit: "MM USD/year"}
      hydrogen: {value: 8.75, unit: "MM USD/year"}
    fixed_costs:
      labor: {value: 3, unit: "MM USD/year"}
      maintenance: {value: 6.3, unit: "MM USD/year"}

  financial_assumptions:
    discount_rate: {value: 0.10, unit: "fraction"}
    plant_lifetime: {value: 20, unit: "years"}

lca:
  allocation_method: "energy"
  allocation_factors:
    saf_jet: 0.47
    renewable_diesel: 0.43
    other_products: 0.10

  emission_factors:
    feedstocks:
      soybean_oil:
        value: 25.6
        unit: "gCO2e/MJ"
        source: "GREET 2023"
        scope: "cradle-to-gate"
      hydrogen:
        value: 94.5
        unit: "gCO2e/MJ H2"
        source: "GREET 2023"
        notes: "Natural gas SMR"

    utilities:
      electricity:
        value: 468
        unit: "gCO2e/kWh"
        source: "GREET 2023 US grid mix"

  impact_results:
    climate_change:
      value: 33.8
      unit: "gCO2e/MJ jet fuel"
      method: "IPCC AR6 GWP100"
      notes: "Cradle-to-gate only; excludes combustion"
```

**This example demonstrates**:
- **Complete TEA**: CAPEX, OPEX, financial assumptions, plant capacity
- **Complete LCA**: Allocation method, emission factors, impact results
- **Co-product handling**: Energy allocation between jet fuel and diesel
- **System boundary**: Explicitly defined as cradle-to-gate
- **Data provenance**: Sources cited for all emission factors
- **Integration**: TEA and LCA in one coherent configuration

**Why this structure matters**:

Traditional TEA/LCA studies scatter this information across:
- Excel spreadsheets (hidden formulas, no version control)
- PDF reports (not machine-readable)
- Simulation files (requires expensive software)
- Separate TEA and LCA models (inconsistent assumptions)

This specification brings everything together in a **single, transparent, version-controlled configuration** that can be validated, automated, and audited.

See `pathways/demo_hefa_base.yaml` for the full 600-line pathway with streams, detailed unit operations, mass/energy balances, and validation against NREL literature.

---

## Repository Contents

```
pathway-spec/
├── README.md                      # This file
├── GOVERNANCE.md                  # Maintenance and decision-making process
├── ECOSYSTEM.md                   # Relationship to existing TEA/LCA tools
├── COMPARISON.md                  # Comparison with existing approaches
├── LICENSE                        # Apache 2.0 license
├── pathways/                      # Example pathway files
│   └── demo_hefa_base.yaml       # Demo HEFA-based SAF pathway
├── schema/                        # Schema definitions
│   └── pathway_schema.yaml       # Structural specification
├── docs/                          # Documentation
│   ├── QUICKSTART.md             # Getting started guide
│   ├── GLOSSARY.md               # TEA/LCA terminology
│   ├── ROADMAP.md                # Development timeline
│   └── VALIDATION.md             # Pathway validation status
├── examples/                      # Reference implementations
│   └── validate_pathway.py       # Python validation script
└── tools/                         # Utilities
    └── iq-validate                # CLI validation tool (planned)
```

---

## Key Features

### For Researchers
- **Reproducible studies**: Share exact pathway configurations with publications
- **Version control**: Track assumption changes over time with Git
- **Transparent peer review**: All parameters visible and documented
- **Scenario automation**: Programmatically generate parameter sweeps

### For Industry
- **Regulatory submissions**: Transparent, auditable pathway definitions
- **Internal consistency**: Standardized format across project teams
- **Integration-ready**: Compatible with optimization and design workflows
- **Vendor-neutral**: Open format, no lock-in

### For Tool Developers
- **Machine-readable**: Easy to parse and validate programmatically
- **Extensible**: Support custom fields without breaking core structure
- **Interoperable**: Import/export from existing tools (planned)

---

## Validation Strategy

The specification includes multiple validation layers:

**Level 1: Structural Validation** (current)
- YAML syntax checking
- Required field verification
- Stream connectivity validation
- Basic mass/energy balance closure

**Level 2: Literature Validation** (in progress)
- Comparison against published studies (NREL, academic papers)
- Parameter range checking
- Confidence scoring (see `docs/VALIDATION.md`)

**Level 3: Thermodynamic Validation** (planned)
- Physical property consistency
- Mass/energy balance verification
- Temperature/pressure feasibility

**Level 4: Experimental Validation** (future)
- Comparison with pilot plant data
- Commercial facility benchmarking
- Regulatory pathway certification

**Current status**: Demo HEFA pathway validated at Level 1-2 against NREL TP-5100-58677. See `docs/VALIDATION.md` for detailed comparison.

---

## Comparison with NREL Design Cases and Aspen IC Format

Traditional TEA studies often use Aspen Plus simulation files or design case spreadsheets. While these approaches provide thermodynamic rigor, they:

- Embed assumptions within complex simulation files
- Require expensive software licenses
- Lack standardized configuration formats
- Don't easily version control

The Pathway Specification complements these tools by:

- **Extracting key assumptions** into a readable configuration layer
- **Documenting data provenance** explicitly
- **Enabling version control** of pathway definitions
- **Facilitating scenario generation** without manual simulation setup

**Use case**: Run detailed Aspen simulation → extract stream table → populate Pathway Spec → version control configuration → automate scenario variations.

---

## Getting Started

### Installation

```bash
# Clone repository
git clone https://github.com/insightquantix/pathway-spec.git
cd pathway-spec

# Install dependencies
pip install pyyaml jsonschema
```

### Validate a Pathway

```bash
# Run basic validation
python examples/validate_pathway.py pathways/demo_hefa_base.yaml
```

### Read Documentation

- **Quickstart**: `docs/QUICKSTART.md` - Learn the format in 15 minutes
- **Glossary**: `docs/GLOSSARY.md` - TEA/LCA terminology reference
- **Ecosystem**: `ECOSYSTEM.md` - How this relates to GREET, OpenLCA, etc.
- **Validation**: `docs/VALIDATION.md` - Pathway validation status

---

## Development Status

> **Development Roadmap**
>
> This is a v0.5 draft specification under active development:
> - ✅ Core schema structure defined
> - ✅ Demo HEFA pathway (validated against NREL literature)
> - ✅ Basic validation tools
> - ⏳ Tool integrations planned (v0.6-v0.7)
> - ⏳ Peer review in progress
> - ⏳ Multi-domain validation expanding
>
> See `docs/ROADMAP.md` for detailed development plan.

### What's Implemented
- Core YAML schema structure
- HEFA pathway example (validated against NREL TP-5100-58677)
- Python validation script
- Comprehensive documentation

### In Development
- Additional pathway examples (hydrogen, ammonia)
- Formal JSON Schema validation
- Enhanced thermodynamic checking
- Import/export converters for existing tools

### Planned
- Integration interfaces for GREET, OpenLCA, Aspen
- Regulatory pathway templates (LCFS, RED II, CORSIA)
- Multi-stakeholder governance transition
- Peer-reviewed publication

---

## Use Cases

### Academic Research
**Best practice**: Pathway Spec + Python/R analysis
- Version-controlled pathway definitions
- Reproducible studies for publications
- Easy parameter sensitivity analysis

### Regulatory Submission
**Best practice**: GREET/OpenLCA + Pathway Spec documentation
- Maintain regulatory credibility with established tools
- Use Pathway Spec for transparent assumption documentation

### Industry Feasibility Studies
**Best practice**: Pathway Spec + Aspen for detailed design
- Fast iteration with Pathway Spec
- Rigorous validation with process simulation

### Tool Development
**Best practice**: Pathway Spec as configuration layer
- Standard input format for TEA/LCA tools
- Extensible for domain-specific requirements

---

## Contributing

We welcome contributions from:

- **Domain experts**: Suggest improvements to pathway structure
- **Tool developers**: Build parsers, validators, and converters
- **Researchers**: Provide feedback on real-world usage
- **Standards bodies**: Help formalize governance and validation

See `CONTRIBUTING.md` for guidelines.

**Current priorities:**
1. Validate additional pathways against published studies
2. Build integration interfaces for existing tools
3. Expand multi-stakeholder governance
4. Develop formal validation test suite

---

## Comparison with Existing Approaches

| Approach | Transparency | Version Control | Automation | Ecosystem |
|----------|--------------|-----------------|------------|-----------|
| Excel/Google Sheets | Low | Poor | Limited | Universal |
| Aspen Plus | Medium | Poor | Good | Industry standard |
| GREET Model | Medium | None | Medium | Regulatory standard |
| OpenLCA/SimaPro | High | None | Medium | LCA standard |
| **IQ Pathway Spec** | High | Native | High | Emerging |

*Note: IQ Pathway Spec row represents design goals; ecosystem is early-stage (v0.5).*

See `COMPARISON.md` for detailed analysis.

---

## Citation

If you reference this specification in research or publications:

```bibtex
@misc{iqpathway2025,
  title={Insight Quantix Pathway Specification: A Proposed Open Format for TEA-LCA Models},
  author={Insight Quantix},
  year={2025},
  version={0.5-draft},
  url={https://github.com/insightquantix/pathway-spec}
}
```

---

## Frequently Asked Questions

**Q: Is this ready for production use?**
A: This is a v0.5 development draft. It's suitable for research, prototyping, and providing feedback. For regulatory submissions or investment decisions, independent validation is required.

**Q: Can I use this in my research?**
A: Yes, under Apache 2.0 license. Please cite and note the draft status.

**Q: How does this relate to Insight Quantix's commercial products?**
A: This is an open standard proposal. Insight Quantix uses extended internal versions but commits to maintaining this public specification. The goal is community adoption, not vendor lock-in.

**Q: Will you accept pull requests?**
A: Yes. See `CONTRIBUTING.md` for guidelines.

**Q: What about integration with GREET/OpenLCA/Ecoinvent?**
A: See `ECOSYSTEM.md` for detailed discussion. Integration interfaces are planned for v0.6-v0.7. The goal is complementary integration, not replacement.

**Q: How do I report issues or suggest improvements?**
A: Open a GitHub Issue or submit a Pull Request. We actively review and respond to community feedback.

---

## Current Limitations & Future Work

While the specification structure is well-developed, several areas require continued development:

### Schema & Validation
- **Formal schema**: JSON Schema specification planned for v0.6
- **Thermodynamic validation**: Physical consistency checking under development
- **Unit operation library**: Standard component templates being compiled

### Tool Ecosystem
- **Integrations**: Import/export converters for GREET, OpenLCA, Aspen planned (v0.7)
- **Validators**: Enhanced validation suite with mass/energy balance verification in development
- **Visualization**: Pathway network visualization tools planned

### Governance & Community
- **Multi-stakeholder oversight**: Transition from single-maintainer to Technical Working Group planned (v1.0)
- **Peer review**: Academic publication in preparation
- **External validation**: Seeking partnerships with research institutions

### Domain Coverage
- **Additional examples**: Hydrogen, ammonia, e-fuel pathways in development
- **Regulatory templates**: LCFS, RED II, CORSIA pathway templates planned
- **Industry validation**: Commercial facility benchmarking opportunities being explored

See `docs/ROADMAP.md` for detailed development timeline.

---

## Relationship to Insight Quantix Products

Insight Quantix maintains proprietary TEA/LCA tools and databases that use extended versions of this format internally. However:

- **This spec is open**: Apache 2.0 licensed, free to use and modify
- **Reference data is separate**: Validated CAPEX/OPEX/emission factors remain proprietary
- **Multiple implementations welcome**: This format is not tied to Insight Quantix tools
- **Community governance sought**: See `GOVERNANCE.md` for transition plan

The goal is to establish an **open standard** that benefits the entire TEA/LCA community, even if Insight Quantix products are one implementation among many.

---

## Founder's Note

The Pathway Specification began as an internal backbone of the Insight Quantix TEA-LCA engine. As the clean energy sector accelerates, it's clear that reproducibility, transparency, and audit-friendly modeling are essential for meaningful progress.

This specification is released as a draft because the future of TEA/LCA modeling deserves collaboration, critique, and shared standards. Your feedback will directly influence how this specification evolves.

Whether you're a researcher seeking reproducible methods, an engineer building tools, a regulator evaluating pathways, or a company developing clean energy projects—your input is valuable and welcome.

**Jamie Gomez**
Founder, Insight Quantix

---

## Contact

- **Technical questions**: Open an issue on GitHub
- **Collaboration inquiries**: contribute@insightquantix.com
- **General information**: https://www.insightquantix.com

---

## License

Apache License 2.0 - see `LICENSE` file for details.

---

**Acknowledgments**: This specification builds on decades of TEA/LCA research by NREL, Argonne National Laboratory, academic institutions, and industry practitioners. We gratefully acknowledge their foundational work.

*Last updated: 2025-01-23 | Version: 0.5-draft*
