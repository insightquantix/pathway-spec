# Quickstart Guide

Learn the Insight Quantix Pathway Specification in 15 minutes.

---

## What You'll Learn

1. Basic structure of a pathway file
2. How to read and understand pathway definitions
3. How to validate a pathway
4. How to create a simple pathway from scratch

---

## Prerequisites

```bash
# Python 3.10+ and PyYAML
pip install pyyaml
```

---

## 1. Understanding the Structure

Every pathway file has this top-level structure:

```yaml
meta:           # WHO, WHAT, WHEN - pathway metadata
feedstocks:     # INPUTS - materials going in
products:       # OUTPUTS - what you're making
streams:        # FLOWS - material/energy flows between units
units:          # TRANSFORMS - process equipment and operations
balances:       # CHECKS - mass and energy balances
tea:            # ECONOMICS - capital and operating costs
lca:            # ENVIRONMENT - carbon intensity and impacts
```

Only `meta`, `feedstocks`, `products`, and `units` are required. Everything else is optional but recommended.

---

## 2. Reading the Demo Pathway

Let's explore the HEFA demo pathway:

```bash
# View the demo pathway
cat pathways/demo_hefa_base.yaml
```

### Meta Section

```yaml
meta:
  name: "HEFA-based Sustainable Aviation Fuel (Demo)"
  version: "0.1.0"
  functional_unit: "MJ jet fuel (LHV)"
  boundary: "cradle-to-gate"
  reference_year: 2024
  currency: "USD"
```

**What this tells you:**
- **Name**: Human-readable identifier
- **Functional unit**: Basis for LCA (per MJ of jet fuel)
- **Boundary**: What's included (feedstock production → fuel production)
- **Reference year**: When cost data applies

### Feedstocks Section

```yaml
feedstocks:
  soybean_oil:
    name: "Soybean Oil"
    type: "vegetable_oil"
    lhv:
      value: 37.5
      unit: "MJ/kg"
    cost:
      value: 800
      unit: "USD/tonne"
    ci_production:
      value: 25.6
      unit: "gCO2e/MJ"
      source: "GREET 2023"
```

**What this tells you:**
- Energy content (LHV = Lower Heating Value)
- Economic cost
- Carbon intensity of producing this feedstock
- Data source for traceability

### Units Section

```yaml
units:
  hydrotreater:
    name: "Hydrotreating Reactor"
    type: "fixed_bed_reactor"
    inputs: ["S002_pretreated_oil", "S003_hydrogen"]
    outputs: ["S004_reactor_effluent"]
    operating_conditions:
      temperature: {value: 350, unit: "C"}
      pressure: {value: 80, unit: "bar"}
    conversion:
      triglycerides: 0.999
```

**What this tells you:**
- What the unit does (catalytic hydrogenation)
- What goes in and out (stream IDs)
- How it operates (temperature, pressure)
- Reaction performance (99.9% conversion)

---

## 3. Validate a Pathway

Run the basic validation script:

```bash
python examples/validate_pathway.py pathways/demo_hefa_base.yaml
```

Expected output:
```
✓ Pathway loaded successfully
✓ Required sections present: meta, feedstocks, products, units
✓ Mass balance closure: 100.0%
✓ Energy balance closure: 99.5%
⚠ Warning: This pathway has not been validated against experimental data
⚠ Warning: Capital costs are order-of-magnitude estimates only

Summary:
  Pathway: HEFA-based Sustainable Aviation Fuel (Demo)
  Version: 0.1.0
  Products: saf_jet, renewable_diesel, lpg_byproduct
  CI (jet fuel): 33.8 gCO2e/MJ
```

---

## 4. Create a Simple Pathway from Scratch

Let's create a minimal hydrogen production pathway.

### Step 1: Create file

```yaml
# my_hydrogen_pathway.yaml

meta:
  name: "PEM Electrolyzer Hydrogen Production"
  version: "1.0.0"
  date: "2025-01-23"
  author: "Your Name"
  functional_unit: "kg H2 produced"
  boundary: "gate-to-gate"
  reference_year: 2024
  currency: "USD"
  tags:
    - hydrogen
    - PEM
    - electrolysis

feedstocks:
  electricity:
    name: "Grid Electricity"
    type: "electricity"
    phase: "electricity"
    cost:
      value: 0.05
      unit: "USD/kWh"
    ci_production:
      value: 400
      unit: "gCO2e/kWh"

  water:
    name: "Deionized Water"
    type: "water"
    phase: "liquid"
    cost:
      value: 2.0
      unit: "USD/tonne"

products:
  hydrogen:
    name: "Compressed Hydrogen"
    type: "industrial_gas"
    phase: "gas"
    lhv:
      value: 120
      unit: "MJ/kg"

  oxygen:
    name: "Oxygen Byproduct"
    type: "industrial_gas"
    phase: "gas"

streams:
  S001_water_in:
    name: "Water to Electrolyzer"
    from_unit: null
    to_unit: "electrolyzer"
    mass_flow:
      value: 9
      unit: "kg per kg H2"

  S002_electricity:
    name: "Electricity to Electrolyzer"
    from_unit: null
    to_unit: "electrolyzer"
    energy_flow:
      value: 55
      unit: "kWh per kg H2"

  S003_hydrogen_out:
    name: "Hydrogen Product"
    from_unit: "electrolyzer"
    to_unit: null
    mass_flow:
      value: 1
      unit: "kg per kg H2"

  S004_oxygen_out:
    name: "Oxygen Byproduct"
    from_unit: "electrolyzer"
    to_unit: null
    mass_flow:
      value: 8
      unit: "kg per kg H2"

units:
  electrolyzer:
    name: "PEM Electrolyzer Stack"
    type: "electrolyzer"
    inputs: ["S001_water_in", "S002_electricity"]
    outputs: ["S003_hydrogen_out", "S004_oxygen_out"]
    capacity:
      value: 1000
      unit: "kg H2/day"
    efficiency:
      value: 65
      unit: "%"
      notes: "LHV basis, stack efficiency"

tea:
  capex:
    total:
      value: 1.5
      unit: "MM USD"
      notes: "1 MW PEM system including balance of plant"

  opex:
    variable_costs:
      electricity:
        value: 2.75
        unit: "USD/kg H2"
        basis: "55 kWh/kg × $0.05/kWh"
      water:
        value: 0.02
        unit: "USD/kg H2"

    fixed_costs:
      maintenance:
        value: 45000
        unit: "USD/year"
        notes: "3% of CAPEX"

lca:
  functional_unit: "kg H2 produced"
  impact_results:
    climate_change:
      value: 22.0
      unit: "kgCO2e/kg H2"
      method: "IPCC AR6"
      calculation: "55 kWh × 400 gCO2e/kWh / 1000"
```

### Step 2: Validate it

```bash
python examples/validate_pathway.py my_hydrogen_pathway.yaml
```

### Step 3: Modify and experiment

Try changing:
- Electricity cost → see impact on OPEX
- Grid carbon intensity → see impact on LCA
- Electrolyzer efficiency → see impact on energy consumption

---

## 5. Common Patterns

### Pattern 1: Reference External Data

```yaml
feedstocks:
  corn_stover:
    ci_production:
      value: 15.2
      unit: "gCO2e/MJ"
      source: "GREET 2023"
      source_id: "CS_HARVEST_US_AVG"
      notes: "Includes farming, collection, transport"
```

### Pattern 2: Express Uncertainty

```yaml
tea:
  capex:
    hydrotreater:
      value: 80.0
      unit: "MM USD"
      uncertainty:
        distribution: "triangular"
        min: 65.0
        max: 100.0
```

### Pattern 3: Multiple Scenarios

```yaml
sensitivity:
  scenarios:
    high_feedstock:
      description: "High feedstock cost scenario"
      changes:
        feedstocks.soybean_oil.cost: 1200

    renewable_h2:
      description: "Green hydrogen from electrolysis"
      changes:
        feedstocks.hydrogen.ci_production: 2.5
        feedstocks.hydrogen.cost: 5.00
```

### Pattern 4: Link to Ecoinvent

```yaml
feedstocks:
  methanol:
    source: "ecoinvent"
    process_uuid: "a1234567-890a-bcde-f123-456789abcdef"
    process_name: "methanol production, from natural gas | RoW"
    dataset_version: "3.9.1"
    cost:
      value: 400
      unit: "USD/tonne"
```

---

## 6. Best Practices

### Units
Always specify units explicitly:
```yaml
# ✓ GOOD
temperature:
  value: 350
  unit: "C"

# ✗ BAD
temperature: 350  # What unit? C? K? F?
```

### IDs
Use snake_case for identifiers:
```yaml
# ✓ GOOD
feedstocks:
  soybean_oil: {...}
  renewable_hydrogen: {...}

# ✗ BAD
feedstocks:
  Soybean Oil: {...}  # Spaces make parsing harder
  renewableHydrogen: {...}  # camelCase less readable in YAML
```

### Documentation
Add notes for non-obvious values:
```yaml
catalyst:
  lifetime:
    value: 3
    unit: "years"
    notes: "Vendor specification; actual lifetime may vary with feedstock quality"
```

### Sources
Always cite data sources:
```yaml
ci_production:
  value: 468
  unit: "gCO2e/kWh"
  source: "GREET 2023"
  # NOT: source: "some website I found"
```

---

## 7. Next Steps

**Explore more:**
- Read `schema/pathway_schema.yaml` for complete field documentation
- Review `GLOSSARY.md` for TEA/LCA terminology
- Check `ECOSYSTEM.md` for integration with existing tools

**Create pathways:**
- Start with a simple process you understand well
- Add complexity incrementally
- Validate frequently
- Document assumptions clearly

**Contribute:**
- Share your pathway examples
- Report issues or confusing documentation
- Propose new fields or improvements
- See `CONTRIBUTING.md` for guidelines

---

## Common Questions

**Q: Do I need to fill in every field?**
A: No. Only `meta`, `feedstocks`, `products`, and `units` are required. Add other sections as needed for your use case.

**Q: Can I add custom fields?**
A: Yes, use the `extensions` section to avoid conflicts with core spec fields.

**Q: How detailed should my pathway be?**
A: As detailed as needed for your purpose. Regulatory submissions need more detail than quick conceptual studies.

**Q: Can I use this for non-fuel pathways?**
A: Yes, though current examples focus on fuels. The structure is general enough for any process pathway.

**Q: Where do I get cost and emission data?**
A: See `ECOSYSTEM.md` for sources like GREET, Ecoinvent, literature, vendor quotes, and engineering estimates.

---

## Troubleshooting

### YAML syntax errors

```
Error: mapping values are not allowed here
```

**Fix**: Check for indentation problems or missing colons.

### Missing required fields

```
Error: Required field 'meta.functional_unit' not found
```

**Fix**: Add the missing field to the `meta` section.

### Stream references

```
Warning: Stream 'S005_unknown' referenced but not defined
```

**Fix**: Either define the stream in the `streams` section or remove the reference.

---

**You're ready to create pathways!** Start simple, iterate, and don't hesitate to ask questions via GitHub Issues.
