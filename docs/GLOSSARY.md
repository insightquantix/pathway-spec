# TEA/LCA Glossary

Terminology reference for the Pathway Specification.

---

## General Concepts

### **Pathway**
A complete process configuration describing transformation of feedstocks into products, including mass/energy flows, unit operations, costs, and environmental impacts.

### **Functional Unit**
The quantification basis for LCA studies. Defines "per what" impacts are calculated.
- Examples: "MJ fuel (LHV)", "kg product", "vehicle-km", "tonne-km transported"
- Must be clearly defined in `meta.functional_unit`

### **System Boundary**
Defines which life-cycle stages are included in the analysis.
- **Cradle-to-gate**: From raw material extraction through production gate
- **Cradle-to-grave**: From raw material extraction through use and disposal
- **Gate-to-gate**: Only the production facility itself
- **Well-to-wake** (fuels): From resource extraction through combustion
- **Well-to-wheel** (vehicles): From resource extraction through vehicle use

### **Basis**
Reference point for scaling calculations (e.g., "per tonne of feedstock", "per MJ of product")

---

## Techno-Economic Analysis (TEA)

### **CAPEX (Capital Expenditure)**
One-time costs to design and construct a facility.
- **Direct costs**: Equipment, materials, labor
- **Indirect costs**: Engineering, construction management, contingency
- Expressed as total installed cost in base year dollars (e.g., "MM USD in 2024 dollars")

### **OPEX (Operating Expenditure)**
Recurring costs to operate a facility, typically expressed annually.
- **Variable costs**: Scale with production (feedstocks, utilities, catalysts)
- **Fixed costs**: Independent of production rate (labor, maintenance, overhead)

### **Capacity**
Design throughput of a plant or unit operation (e.g., "100,000 tonnes/year", "10 MW")

### **Capacity Factor**
Ratio of actual production to design capacity over a time period.
- Example: 90% capacity factor = 8,000 hours/year operation out of 8,760 possible hours

### **Discount Rate**
Time value of money used in NPV calculations, typically 7-12% for industrial projects.

### **Levelized Cost**
Average cost per unit of production over plant lifetime, accounting for capital recovery and time value of money.
- **LCOE**: Levelized Cost of Electricity
- **LCOH**: Levelized Cost of Hydrogen
- **LCOF**: Levelized Cost of Fuel

### **IRR (Internal Rate of Return)**
Discount rate at which NPV = 0; measure of project profitability.

### **NPV (Net Present Value)**
Sum of discounted cash flows over project lifetime.

### **Payback Period**
Time required to recover initial capital investment from operating cash flows.

---

## Life-Cycle Assessment (LCA)

### **LCA (Life-Cycle Assessment)**
Systematic evaluation of environmental impacts throughout a product's life cycle.
- Governed by ISO 14040/14044 standards
- Four phases: Goal & Scope, Inventory, Impact Assessment, Interpretation

### **LCI (Life-Cycle Inventory)**
Compilation of material and energy flows for a product system.
- Inputs: Raw materials, energy, water
- Outputs: Products, co-products, emissions, waste

### **LCIA (Life-Cycle Impact Assessment)**
Translation of LCI data into environmental impact scores.
- Impact categories: Climate change, acidification, eutrophication, toxicity, etc.

### **Carbon Intensity (CI)**
Greenhouse gas emissions per unit of product or energy.
- Common units: gCO₂e/MJ (fuels), kgCO₂e/kg (chemicals), gCO₂e/kWh (electricity)
- Includes direct + indirect emissions

### **GWP (Global Warming Potential)**
Metric for comparing greenhouse gases on a CO₂-equivalent basis.
- **GWP100**: 100-year time horizon (most common)
- Example: Methane has GWP100 ≈ 27-30 (depends on IPCC assessment report)

### **CO₂e (Carbon Dioxide Equivalent)**
Mass of CO₂ that would have equivalent GWP to a given GHG mix.
- Calculation: CO₂e = (mass_CH₄ × GWP_CH₄) + (mass_N₂O × GWP_N₂O) + ...

### **Allocation**
Method for partitioning environmental burdens among multiple co-products.
- **Physical allocation**: Based on mass or energy content
- **Economic allocation**: Based on market value
- **System expansion**: Avoid allocation by expanding system boundary

### **Biogenic Carbon**
Carbon originally absorbed from atmosphere by photosynthesis.
- Combustion emits CO₂ but doesn't add "new" carbon to atmosphere-ocean-biosphere system
- Accounting method varies by standard (e.g., CARB vs. EU RED vs. CORSIA)

### **Attributional LCA**
Describes environmentally relevant flows to/from a product system, holding other systems constant.
- "Accounting" perspective: What is the footprint of this product?

### **Consequential LCA**
Describes consequences of changes in product system on other systems.
- "Change" perspective: What happens if we scale up this technology?

### **Background Processes**
Generic processes not specific to the study (e.g., grid electricity, steel production).
- Typically sourced from databases like Ecoinvent

### **Foreground Processes**
Processes specific to the system being studied (e.g., your facility's operations).
- Typically modeled with primary data

---

## Process Engineering

### **Unit Operation**
Individual processing step that transforms material or energy streams.
- Examples: Reactor, distillation column, heat exchanger, compressor, electrolyzer

### **Stream**
Flow of material or energy between units or across system boundary.
- Characterized by: Mass/mole flow rate, composition, temperature, pressure, phase

### **Feedstock**
Raw material input to a process (e.g., biomass, natural gas, water, electricity).

### **Product**
Desired output from a process.

### **Co-product**
Additional valuable output produced alongside main product (e.g., oxygen from electrolysis).

### **Byproduct**
Output with limited or no value (may incur disposal cost).

### **Conversion**
Fraction of reactant transformed in a reaction.
- Example: "98% conversion of triglycerides to hydrocarbons"

### **Yield**
Amount of product obtained relative to theoretical maximum or input.
- **Theoretical yield**: Maximum possible based on stoichiometry
- **Actual yield**: Measured product output

### **Selectivity**
Fraction of converted reactant that forms desired product vs. byproducts.
- Example: "90% selectivity to jet fuel, 10% to lighter gases"

### **Residence Time**
Average time material spends in a reactor or unit operation.

### **LHSV (Liquid Hourly Space Velocity)**
Volumetric flow rate of liquid feed divided by reactor volume (units: h⁻¹).

### **GHSV (Gas Hourly Space Velocity)**
Volumetric flow rate of gas feed divided by reactor volume (units: h⁻¹).

---

## Energy and Thermodynamics

### **LHV (Lower Heating Value)**
Energy released by complete combustion, excluding heat of vaporization of water in products.
- Also called "net calorific value"
- Used for fuels in most practical applications

### **HHV (Higher Heating Value)**
Energy released by complete combustion, including heat of vaporization of water in products.
- Also called "gross calorific value"
- Used in some standards and regulations

### **Efficiency**
Ratio of useful output to total input (energy, mass, or exergy basis).
- **Thermal efficiency**: Energy basis
- **Electrical efficiency**: Electricity output / energy input
- **Exergy efficiency**: Useful work basis (thermodynamically rigorous)

### **Heat Integration**
Systematic use of waste heat from hot streams to heat cold streams, reducing external heating/cooling.
- Pinch analysis is common methodology

### **Utility**
Supporting service required for operations (steam, cooling water, electricity, compressed air).

---

## Renewable Fuels & Chemicals

### **SAF (Sustainable Aviation Fuel)**
Jet fuel produced from renewable or waste feedstocks.
- Must meet ASTM D7566 specification
- Typically blended with conventional jet fuel

### **HEFA (Hydroprocessed Esters and Fatty Acids)**
SAF/renewable diesel production pathway using hydrotreatment of vegetable oils or animal fats.
- ASTM D7566 Annex A2

### **FT (Fischer-Tropsch)**
Catalytic synthesis of liquid hydrocarbons from syngas (CO + H₂).
- Used for biomass-to-liquid (BTL) or gas-to-liquid (GTL) processes

### **ATJ (Alcohol-to-Jet)**
SAF pathway converting alcohols (ethanol, isobutanol) to jet fuel.
- ASTM D7566 Annex A5

### **Power-to-X (PtX)**
Technologies converting renewable electricity to fuels or chemicals.
- Examples: Power-to-hydrogen, power-to-methanol, power-to-ammonia

### **E-fuel (Electrofuel)**
Synthetic fuel produced using renewable electricity and captured CO₂.
- Examples: E-methanol, E-kerosene, E-diesel

### **Renewable Diesel**
Drop-in diesel fuel from renewable feedstocks, distinct from biodiesel (FAME).
- Chemically identical to petroleum diesel (paraffinic hydrocarbons)
- Higher cetane, lower emissions than biodiesel

### **Green Hydrogen**
Hydrogen produced via electrolysis using renewable electricity.
- Near-zero carbon intensity (depends on electricity source)

### **Blue Hydrogen**
Hydrogen from natural gas (SMR or ATR) with carbon capture.
- Reduced but not zero carbon intensity

### **Gray Hydrogen**
Hydrogen from fossil fuels without carbon capture (current industrial standard).
- High carbon intensity (~9-12 kgCO₂e/kg H₂)

### **Ammonia (NH₃)**
Compound of nitrogen and hydrogen, key fertilizer and potential energy carrier.
- **Green ammonia**: Made from green hydrogen
- **Haber-Bosch process**: Conventional catalytic synthesis from N₂ and H₂

---

## Regulatory & Standards

### **LCFS (Low Carbon Fuel Standard)**
California regulation requiring reduction in transportation fuel carbon intensity.
- Credit trading system
- Requires pathway certification and CI calculation

### **RED II (Renewable Energy Directive)**
EU regulation setting renewable energy targets and sustainability criteria.
- Includes GHG emission savings requirements

### **RFS (Renewable Fuel Standard)**
US federal regulation requiring renewable fuel blending.
- Administered by EPA
- RINs (Renewable Identification Numbers) for compliance

### **CORSIA (Carbon Offsetting and Reduction Scheme for International Aviation)**
ICAO scheme for offsetting aviation emissions growth.
- Eligible SAF pathways must meet life-cycle emission reduction thresholds

### **45Q Tax Credit**
US federal tax credit for carbon capture and sequestration.
- Currently $85/tonne CO₂ stored (as of 2024)

### **45V Tax Credit**
US federal tax credit for clean hydrogen production.
- Tiered based on lifecycle CI of hydrogen

### **GREET (Greenhouse gases, Regulated Emissions, and Energy use in Technologies)**
Life-cycle model developed by Argonne National Laboratory.
- De facto standard for transportation fuel CI in North America
- Excel-based with embedded databases

### **Ecoinvent**
Comprehensive LCA database with 10,000+ processes.
- Subscription-based access
- Used by most LCA software tools

### **IPCC (Intergovernmental Panel on Climate Change)**
International body providing GWP values and climate science assessments.
- **AR6**: Sixth Assessment Report (latest, 2021-2023)
- **AR5**: Fifth Assessment Report (2013-2014, widely used baseline)

### **ISO 14040/14044**
International standards defining LCA methodology and requirements.
- 14040: Principles and framework
- 14044: Requirements and guidelines

---

## Process Technology Abbreviations

### **SMR (Steam Methane Reforming)**
Process for producing hydrogen from natural gas using steam.
- Dominant industrial method (~95% of H₂)

### **ATR (Autothermal Reforming)**
Hydrogen production combining partial oxidation and steam reforming.
- Better for large-scale with carbon capture

### **PEM (Proton Exchange Membrane)**
Type of electrolyzer or fuel cell using polymer electrolyte.
- Fast response, good for renewable integration

### **AEM (Anion Exchange Membrane)**
Emerging electrolyzer technology using alkaline membrane.
- Avoids precious metal catalysts

### **SOEC (Solid Oxide Electrolysis Cell)**
High-temperature electrolyzer with high efficiency potential.
- Can co-electrolyze H₂O and CO₂

### **PSA (Pressure Swing Adsorption)**
Gas separation technology using selective adsorption.
- Common for hydrogen purification

### **MEA (Monoethanolamine)**
Chemical solvent used for CO₂ capture from flue gas.
- Energy-intensive regeneration

### **ASU (Air Separation Unit)**
Plant that separates air into oxygen, nitrogen, and sometimes argon.
- Required for gasification and oxy-combustion

---

## Data Quality & Uncertainty

### **Pedigree Matrix**
Semi-quantitative system for assessing LCA data quality.
- Criteria: Reliability, completeness, temporal/geographic/technological correlation

### **Uncertainty Analysis**
Quantification of result variability due to parameter uncertainty.
- Methods: Monte Carlo simulation, analytical propagation, sensitivity analysis

### **Sensitivity Analysis**
Assessment of how output changes with input parameter variations.
- Identifies critical parameters affecting results

### **Scenario Analysis**
Comparison of results under different assumption sets (discrete scenarios).
- Examples: High/low cost, different feedstocks, future technology improvements

---

## Miscellaneous

### **Basis Year**
Reference year for economic data (CAPEX, OPEX costs).
- Adjust to common basis using cost indices (e.g., CEPCI for chemical plants)

### **CEPCI (Chemical Engineering Plant Cost Index)**
Cost index for adjusting chemical plant capital costs across years.

### **MACRS (Modified Accelerated Cost Recovery System)**
US depreciation schedule for tax calculations.

### **TRL (Technology Readiness Level)**
Scale (1-9) indicating technology maturity.
- TRL 1-3: Basic research
- TRL 4-6: Pilot and demonstration
- TRL 7-9: Commercial deployment

---

## Contributing to Glossary

This glossary is meant to be living documentation. If you find:
- Missing terms
- Unclear definitions
- Errors or outdated information

Please open a GitHub Issue or submit a Pull Request with improvements.

---

*Last updated: 2025-01-23*
