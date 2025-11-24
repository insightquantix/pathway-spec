# Ecosystem Integration

## Current Integration Status

> **⚠️ REALITY CHECK (v0.5)**
>
> **Implemented integrations**: **ZERO**
> **Working converters**: **NONE**
> **Validated interoperability**: **NOT DEMONSTRATED**
>
> This document describes the **vision and strategy** for ecosystem integration.
> All integrations mentioned below are conceptual, planned, or aspirational.
> No production-grade tools currently exist for importing/exporting pathway data
> to/from GREET, OpenLCA, Ecoinvent, Aspen, or other established systems.
>
> **We are actively seeking collaborators** to build these integrations.

---

## Purpose of This Document

This specification does not exist in isolation. The TEA/LCA community has decades of established tools, databases, and standards. This document explains:

1. How the Pathway Specification relates to existing systems
2. Where integration is **planned or possible** (not implemented)
3. What role this spec fills vs. existing approaches
4. Compatibility and interoperability considerations

---

## Overview: The TEA/LCA Landscape

### Established Systems

| System | Type | Primary Use | Maintained By |
|--------|------|-------------|---------------|
| **GREET** | TEA/LCA Database + Model | Transportation fuel pathways | Argonne National Lab |
| **Ecoinvent** | LCA Database | Background processes, materials | Ecoinvent Association |
| **OpenLCA** | LCA Software | Process-based LCA studies | GreenDelta |
| **SimaPro** | LCA Software | Commercial LCA studies | PRé Sustainability |
| **GaBi** | LCA Software | Industrial LCA | Sphera |
| **Aspen Plus/HYSYS** | Process Simulation | Chemical process design | AspenTech |
| **SuperPro Designer** | TEA Software | Bioprocess economics | Intelligen |
| **ISO 14040/14044** | Standard | LCA methodology framework | ISO |
| **ISO 14067** | Standard | Carbon footprint quantification | ISO |

### Gap This Spec Addresses

None of the above provide a **lightweight, version-controlled, machine-readable pathway configuration format** suitable for:

- Git-based collaboration
- CI/CD integration
- Automated scenario generation
- Transparent peer review
- AI-assisted modeling

The Pathway Specification is designed to complement these tools, not replace them.

---

## Integration Strategy by System

### 1. GREET (Greenhouse Gases, Regulated Emissions, and Energy Use in Technologies)

**What GREET does**:
- Provides validated life-cycle emission factors for fuels and vehicles
- Excel-based model with embedded calculations
- Focus on transportation pathways
- Regulatory credibility (EPA, CARB)

**Relationship to Pathway Spec**:

| Aspect | GREET | Pathway Spec |
|--------|-------|--------------|
| **Emission factors** | Source of validated data | References GREET data |
| **Pathway structure** | Hard-coded in Excel | Explicit YAML representation |
| **Customization** | Manual Excel editing | Programmatic modification |
| **Version control** | File versioning | Git-native |

**Integration opportunities**:
- **Import GREET data**: Create converter to extract GREET pathways → YAML format
- **Reference GREET factors**: Link to GREET database IDs for emission factors
- **Validation**: Compare Pathway Spec results against GREET for standard pathways

**Example integration**:
```yaml
lca:
  emission_factors:
    electricity_us_grid:
      source: "GREET 2023"
      source_id: "ELC_US_MIX"
      value: 468  # gCO2e/kWh
      notes: "U.S. average grid mix, GREET 2023 version"
```

**Status**: No formal integration yet. Community contribution opportunity.

---

### 2. Ecoinvent Database

**What Ecoinvent does**:
- Comprehensive LCA database (10,000+ processes)
- Background data for materials, energy, transportation
- Used by most LCA software tools
- Subscription-based access

**Relationship to Pathway Spec**:

| Aspect | Ecoinvent | Pathway Spec |
|--------|-----------|--------------|
| **Process data** | Source for background LCI | References Ecoinvent processes |
| **Foreground modeling** | Requires LCA software | Direct YAML representation |
| **Data quality** | Curated, peer-reviewed | User-defined + references |
| **Scope** | Background + generic foreground | Custom foreground pathways |

**Integration opportunities**:
- **Reference Ecoinvent UUIDs**: Link pathway inputs to Ecoinvent processes
- **Import background data**: Fetch Ecoinvent process data via API
- **Hybrid modeling**: Foreground in Pathway Spec, background from Ecoinvent

**Example integration**:
```yaml
feedstocks:
  hydrogen:
    source: "ecoinvent"
    process_uuid: "a1234567-b890-1234-5678-abcdef123456"
    process_name: "hydrogen production, polymer electrolyte membrane electrolysis | RoW"
    dataset_version: "3.9.1"
    ci_intensity: 2.5  # kgCO2e/kg H2 from Ecoinvent
```

**Status**: Concept only. Requires Ecoinvent license for implementation.

---

### 3. OpenLCA

**What OpenLCA does**:
- Open-source LCA software
- Process-based modeling with network visualization
- Supports Ecoinvent, ELCD, and other databases
- IPC API for programmatic access

**Relationship to Pathway Spec**:

| Aspect | OpenLCA | Pathway Spec |
|--------|---------|--------------|
| **Modeling approach** | GUI-based process networks | Text-based configuration |
| **Data format** | JSON-LD (linked data) | YAML (simple structure) |
| **Use case** | Full LCA studies | Pathway configuration |
| **Ecosystem** | Mature, established | Emerging, experimental |

**Integration opportunities**:
- **Export to OpenLCA**: Convert Pathway Spec → OpenLCA JSON-LD format
- **Import from OpenLCA**: Extract pathway structure from OpenLCA project
- **Hybrid workflow**: Define pathway in YAML, analyze in OpenLCA

**Technical approach**:
- Use OpenLCA IPC API to inject pathway data
- Map Pathway Spec units → OpenLCA processes
- Export results back to YAML for documentation

**Status**: Not implemented. High-value integration target.

---

### 4. Aspen Plus / Process Simulators

**What Aspen Plus does**:
- Rigorous process simulation (mass/energy balances)
- Thermodynamic property packages
- Equipment sizing and costing
- Industry standard for chemical engineering

**Relationship to Pathway Spec**:

| Aspect | Aspen Plus | Pathway Spec |
|--------|------------|--------------|
| **Fidelity** | High (rigorous thermo) | Simplified (inputs/outputs) |
| **Purpose** | Detailed process design | TEA/LCA configuration |
| **Cost** | Commercial license | Open source |
| **Learning curve** | Steep | Gentle |

**Integration opportunities**:
- **Aspen → Pathway Spec**: Export stream table as YAML
- **Pathway Spec → Aspen**: Generate Aspen input deck from pathway
- **Calibration**: Use Aspen results to populate pathway parameters

**Example workflow**:
1. Run detailed Aspen Plus simulation
2. Extract key stream data and equipment parameters
3. Populate Pathway Spec YAML for TEA/LCA study
4. Version control pathway alongside Aspen backup file

**Status**: Conceptual. Aspen API access required for automation.

---

### 5. ISO 14040/14044 Standards

**What ISO 14040/14044 define**:
- LCA methodology framework
- Four phases: goal/scope, inventory, impact assessment, interpretation
- Data quality requirements
- Reporting guidelines

**Relationship to Pathway Spec**:

The Pathway Specification provides a **machine-readable implementation** of ISO 14040/14044 principles:

| ISO 14040/14044 Element | Pathway Spec Implementation |
|-------------------------|----------------------------|
| Goal and scope definition | `meta` section (functional unit, boundaries) |
| Life cycle inventory (LCI) | `streams`, `units`, `balances` |
| Impact assessment | `lca` section (emission factors, impact categories) |
| Interpretation | External (analysis scripts, reports) |
| Data quality | `uncertainty`, `data_quality` fields |
| Transparency | Full pathway visible in YAML |

**Compliance**:
- Pathway Spec enables ISO-compliant studies when used properly
- Does not replace need for LCA expertise
- Documentation must still follow ISO reporting guidelines

---

### 6. Regulatory Standards (LCFS, RED II, RFS, CORSIA)

**What regulatory standards require**:
- California LCFS (Low Carbon Fuel Standard)
- EU RED II (Renewable Energy Directive)
- US RFS (Renewable Fuel Standard)
- ICAO CORSIA (aviation emissions)

**Relationship to Pathway Spec**:

| Regulatory Aspect | Pathway Spec Support |
|-------------------|---------------------|
| **Pathway certification** | Provides transparent documentation |
| **Boundary definitions** | Explicit in `meta.boundary` |
| **CI calculation** | Defined in `lca` section |
| **Auditable assumptions** | All parameters visible in YAML |
| **Updates and versioning** | Git history tracks changes |

**Integration opportunities**:
- Templates for LCFS/RED II compliant pathways
- Automated validation against regulatory requirements
- Export to regulator-specified formats

**Status**: Regulatory acceptance requires demonstrated validation and community adoption.

---

## Interoperability Priorities

### Near-term (v0.2 - v0.5)

1. **GREET pathway import**: Python script to convert GREET pathways → YAML
2. **Ecoinvent UUID references**: Support linking to Ecoinvent processes
3. **CSV export**: Simple tabular export for Excel users

### Medium-term (v0.6 - v1.0)

4. **OpenLCA converter**: Bidirectional pathway ↔ OpenLCA JSON-LD
5. **Process simulator integration**: Import stream tables from Aspen/HYSYS
6. **LCFS template**: Pre-structured pathway for California LCFS applications

### Long-term (v1.0+)

7. **API integrations**: Direct data fetch from Ecoinvent, GREET APIs
8. **Validation service**: Cloud-based pathway validation against standards
9. **Regulatory plugins**: Automated compliance checking for LCFS, RED II, etc.

---

## Reference Implementation Philosophy

The Pathway Specification should support **multiple independent implementations**:

- Python parser (reference implementation)
- JavaScript/TypeScript parser (web applications)
- R package (academic researchers)
- Command-line validator (CI/CD integration)

This diversity prevents vendor lock-in and demonstrates true openness.

---

## Data Licensing Considerations

### Public Domain Data
- GREET: Publicly available (government work)
- NREL data: Often public domain
- Academic publications: Extractable data usually fair use

### Licensed Data
- Ecoinvent: Subscription required, redistribution restricted
- Commercial databases: Terms of service apply
- Proprietary vendor data: Cannot be included in spec

**Pathway Spec approach**:
- Support **referencing** licensed data by ID/UUID
- Do not **embed** licensed data in pathways
- Provide **placeholders** for users with proper licenses

---

## Questions and Feedback

Ecosystem integration questions:

- **General**: Open GitHub Issue tagged `ecosystem`
- **Specific tool integration**: Contact tool maintainers + Pathway Spec team
- **Regulatory pathways**: Email regulatory@insightquantix.com

---

*This ecosystem mapping is preliminary. Corrections and additions welcome.*

*Last updated: 2025-01-23*
