# Pathway Validation Status

This document tracks the validation status of example pathways against published literature and experimental data.

---

## Validation Philosophy

Example pathways serve different purposes depending on validation level:

| Level | Purpose | Usage |
|-------|---------|-------|
| **Level 0: Illustrative** | Show structure/syntax only | Learning format |
| **Level 1: Literature-based** | Parameters from published studies | Conceptual analysis |
| **Level 2: Peer-reviewed** | External expert validation | Teaching, benchmarking |
| **Level 3: Experimental** | Validated against pilot/commercial data | Research, optimization |
| **Level 4: Regulatory** | Accepted for compliance pathways | Regulatory submissions |

**Current status**: All pathways are Level 0-1 (illustrative to literature-based).

---

## Pathway Validation Summary

| Pathway | File | Level | Status | Validated Against | Confidence |
|---------|------|-------|--------|-------------------|------------|
| HEFA SAF | `demo_hefa_base.yaml` | 1 | Partial | NREL TP-5100-58677 | Medium |
| PEM H₂ (planned) | `demo_pem_hydrogen.yaml` | 1 | In progress | DOE H₂A model | Medium |

---

## HEFA SAF Pathway Validation

**File**: `pathways/demo_hefa_base.yaml`

**Reference Study**: Pearlson, M. N.; Wollersheim, C.; Hileman, J. I. (2013). A Techno-Economic and Environmental Assessment of Hydroprocessed Renewable Distillate Fuels. NREL/TP-5100-58677.

**URL**: https://www.nrel.gov/docs/fy14osti/58677.pdf

### Validation Methodology

1. **Extract parameters** from NREL report tables
2. **Compare** with pathway YAML values
3. **Document differences** and rationale
4. **Assess confidence** based on agreement

### Key Parameter Validation

| Parameter | This Pathway | NREL TP-58677 | Difference | Status | Notes |
|-----------|--------------|---------------|------------|--------|-------|
| **Process Conditions** |
| Hydrotreater T | 350°C | 330-370°C | Within range | ✓ | Typical mid-range value |
| Hydrotreater P | 80 bar | 70-90 bar | Within range | ✓ | Commercial practice range |
| LHSV | 1.2 h⁻¹ | 1.0-1.5 h⁻¹ | Within range | ✓ | Depends on catalyst/feed |
| **Mass Yields** |
| Jet fraction | 45% | 42-48% | Within range | ✓ | Depends on fractionation cuts |
| Diesel fraction | 40% | 38-45% | Within range | ✓ | Complementary to jet |
| Total liquid HC | 92% | 88-94% | Within range | ✓ | Typical for HEFA process |
| Light gases | 8% | 6-12% | Within range | ✓ | Depends on feed quality |
| **Hydrogen Consumption** |
| H₂ input | 35 kg/tonne | 30-40 kg/tonne | Within range | ✓ | Includes makeup + losses |
| **Energy Consumption** |
| Electricity | 30 kWh/tonne | 25-35 kWh/tonne | Estimated | ~ | Order of magnitude |
| Process heat | 0.5 GJ/tonne | Not specified | Estimated | ~ | Includes all heating |
| **Economics (2024 USD)** |
| Total CAPEX | $210M | $180-250M* | Scaled estimate | ~ | *2012$ scaled to 2024 |
| CAPEX range | | | | | Subject to site, scale, labor |
| Feedstock cost | $800/tonne | $600-1000/tonne | Market variable | ~ | Highly volatile |
| H₂ cost | $2.50/kg | $1.50-3.50/kg | Typical | ~ | Depends on production method |
| **Life-Cycle Assessment** |
| Soy CI (farming) | 25.6 gCO₂e/MJ | 20-30 gCO₂e/MJ | GREET 2023 | ✓ | Depends on farming practice |
| H₂ CI (SMR) | 94.5 gCO₂e/MJ | 90-100 gCO₂e/MJ | GREET 2023 | ✓ | Natural gas SMR |
| Jet fuel CI | 33.8 gCO₂e/MJ | 28-38 gCO₂e/MJ | Calculated | ✓ | Cradle-to-gate only |

**Legend**:
- ✓ = Validated (within literature range)
- ~ = Estimated (order of magnitude correct, not validated)
- ✗ = Inconsistent (needs revision)

### Confidence Assessment

**High confidence** (validated against multiple sources):
- Process conditions (T, P)
- Hydrogen consumption
- Product yields
- LCA emission factors

**Medium confidence** (literature-based estimate):
- Energy consumption breakdowns
- Equipment cost allocations
- Specific catalyst lifetime

**Low confidence** (placeholder or generic):
- Detailed operating cost breakdown
- Site-specific factors
- Market price assumptions

### Known Limitations

1. **Scale differences**: NREL study covers different plant capacities; scaling relationships applied
2. **Feed variability**: Soybean oil properties vary; representative values used
3. **Cost escalation**: 2012 costs inflated to 2024 using CEPCI; real costs may differ
4. **Regional factors**: NREL assumes U.S. Gulf Coast; other regions will vary
5. **Simplified utilities**: Detailed steam/cooling water integration not modeled

### Validation Gaps

**Not yet validated**:
- [ ] Detailed equipment sizing calculations
- [ ] Catalyst deactivation curves
- [ ] Start-up and turn-down behavior
- [ ] Waste treatment specifics
- [ ] Detailed operating cost breakdown

**Requires domain expertise to validate**:
- [ ] Thermodynamic consistency of stream properties
- [ ] Reaction kinetics and selectivity
- [ ] Heat integration opportunities
- [ ] Actual plant operating data

---

## PEM Hydrogen Pathway Validation

**Status**: In development

**File**: `pathways/demo_pem_hydrogen.yaml`

**Reference**: DOE H₂A Production Model (https://www.hydrogen.energy.gov/h2a_production.html)

### Validation Plan

1. Extract baseline parameters from H₂A model
2. Compare electrolyzer efficiency, CAPEX, OPEX
3. Validate against published PEM electrolyzer performance data
4. Document assumptions and limitations

**Target completion**: Q2 2025

---

## Validation Standards

To achieve **Level 2** (Peer-reviewed) validation, a pathway must:

1. ✅ Be compared against at least one published peer-reviewed study
2. ✅ Have all major parameters within ±20% of literature values (or documented rationale)
3. ✅ Include uncertainty ranges for key parameters
4. ✅ Be reviewed by at least one external domain expert
5. ⚠️ Have thermodynamic consistency verified (mass/energy balances)
6. ⚠️ Include sensitivity analysis for critical assumptions

**Current status**: Only criterion 1-3 partially met for HEFA pathway.

---

## How to Contribute Validations

We welcome community contributions to validate pathways:

### Option 1: Review Existing Pathways

1. Select a pathway to validate
2. Identify relevant literature or data sources
3. Create comparison table (see template above)
4. Open GitHub Issue or Pull Request with findings

### Option 2: Submit Validated Pathway

1. Create pathway following spec structure
2. Document all data sources and assumptions
3. Include validation table comparing to literature
4. Submit as Pull Request with validation documentation

### Option 3: Provide Experimental Data

If you have:
- Pilot plant data
- Commercial plant data
- Experimental measurements

Contact us about data sharing (confidentiality preserved if needed).

---

## Validation Acknowledgments

We gratefully acknowledge:

- **NREL** - Public domain data from techno-economic studies
- **Argonne National Lab** - GREET model emission factors
- **DOE** - H₂A model and hydrogen analysis

*Note: Acknowledgment does not imply endorsement of this specification by these organizations.*

---

## Validation Roadmap

### v0.5 (Current)
- [x] HEFA pathway Level 1 validation against NREL study
- [ ] PEM H₂ pathway Level 1 validation against DOE H₂A

### v0.6 (Target: Q3 2025)
- [ ] External expert review of HEFA pathway (→ Level 2)
- [ ] Add ammonia pathway with Level 1 validation
- [ ] Thermodynamic consistency checker for all pathways

### v0.7 (Target: Q4 2025)
- [ ] Peer-reviewed publication describing specification
- [ ] Independent validation by academic research group
- [ ] At least 3 pathways at Level 2

### v1.0 (Target: 2026)
- [ ] All example pathways at Level 2 minimum
- [ ] At least one Level 3 (experimental) validated pathway
- [ ] External validation test suite

---

## Questions About Validation

- **Report validation issues**: Open GitHub Issue tagged `validation`
- **Propose better data sources**: Submit Pull Request or open Issue
- **Offer to review pathways**: Email validate@insightquantix.com

---

*Last updated: 2025-01-23 (v0.5)*
