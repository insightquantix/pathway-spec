# Contributing Guide

Thank you for your interest in improving the Insight Quantix Pathway Specification!

This document explains how to contribute effectively.

---

## Ways to Contribute

### 1. Report Issues
Found a problem? Let us know!

- **Bug reports**: Schema errors, validation failures, documentation mistakes
- **Feature requests**: Missing fields, new use cases, tool integrations
- **Questions**: Clarifications on spec interpretation

[Open an issue](https://github.com/insightquantix/pathway-spec/issues/new)

### 2. Improve Documentation
Documentation is always incomplete. Help us make it better.

- Fix typos and unclear language
- Add examples and use cases
- Expand glossary with missing terms
- Improve quickstart guide
- Translate to other languages

### 3. Contribute Example Pathways
Show the spec in action with real examples.

- Validate existing demo pathways against literature
- Create new pathway examples (H₂, NH₃, e-fuels, chemicals)
- Document assumptions and data sources clearly
- Follow the structure in `pathways/demo_hefa_base.yaml`

### 4. Build Tools
Extend the ecosystem with useful tools.

- Validation and linting tools
- Converters (GREET, OpenLCA, Aspen, etc.)
- Visualization tools
- Analysis frameworks
- Language bindings (R, Julia, JavaScript)

### 5. Review Proposals
Help evaluate proposed changes to the spec.

- Comment on GitHub Issues
- Review pull requests
- Test proposed changes with your pathways
- Share expertise in TEA, LCA, or process engineering

---

## Contribution Process

### For Small Changes (Typos, Documentation)

1. **Fork** the repository
2. **Make changes** in your fork
3. **Submit pull request** with clear description
4. **Maintainer review** (typically within 1 week)

### For Significant Changes (New Fields, Structural Changes)

1. **Open an issue first** to discuss the proposal
2. **Gather feedback** from community (2-4 weeks)
3. **Revise proposal** based on feedback
4. **Implement changes** with documentation
5. **Submit pull request** with:
   - Issue reference
   - Rationale for change
   - Examples demonstrating usage
   - Documentation updates
6. **Community review** and iteration
7. **Maintainer decision** (or TWG vote for breaking changes)

---

## Code of Conduct

All contributors must follow the [Contributor Covenant Code of Conduct](https://www.contributor-covenant.org/version/2/1/code_of_conduct/).

**Summary**: Be respectful, professional, and constructive. Focus on technical merit, not personal attacks.

Violations should be reported to: conduct@insightquantix.com

---

## Style Guidelines

### YAML Style

```yaml
# ✓ GOOD: Clear, consistent, well-documented

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
    notes: "Price based on 2024 market average"

# ✗ BAD: Unclear, inconsistent

feedstocks:
  SoybeanOil:  # camelCase inconsistent with schema
    Name: Soybean Oil  # Unquoted string, capitalized key
    lhv: 37.5  # Missing unit!
    cost:
      value: 800  # What currency? What year?
```

**Rules**:
- Use `snake_case` for all identifiers
- Always specify units: `{value: X, unit: "Y"}`
- Add `notes` for non-obvious values
- Use 2-space indentation
- Quote strings containing spaces or special characters
- Document data sources in `source` fields

### Documentation Style

- **Be clear and concise**: Prefer simple language over jargon
- **Use examples**: Show, don't just tell
- **Be precise**: Avoid ambiguous language like "about", "roughly", "usually"
- **Cite sources**: Reference data sources and literature
- **Check formatting**: Preview Markdown before submitting

### Python Code Style

- Follow PEP 8
- Use type hints
- Document functions with docstrings
- Include error handling
- Add unit tests for new functionality

---

## Pathway Contribution Guidelines

When contributing example pathways:

### 1. Clear Disclaimer
Add disclaimer if pathway is not fully validated:

```yaml
# IMPORTANT: This is a demonstration pathway...
# DO NOT USE for regulatory submissions without validation...
```

### 2. Document Data Sources

```yaml
provenance:
  sources:
    greet2023:
      citation: "GREET Model 2023, Argonne National Laboratory"
      url: "https://greet.es.anl.gov/"
      date_accessed: "2025-01-15"
      reliability: "high"
```

### 3. Explain Assumptions

```yaml
provenance:
  assumptions:
    hydrogen_source:
      description: "Hydrogen sourced from natural gas SMR"
      justification: "Most common current industrial source"
      impact: "High CI; green H2 would reduce impact significantly"
```

### 4. Balance Completeness vs. Simplicity
- Include enough detail to be useful
- Don't add complexity without justification
- Comment unusual or non-obvious values

### 5. Validate Before Submitting
- Run validation script: `python examples/validate_pathway.py your_pathway.yaml`
- Check mass and energy balances
- Verify units are consistent
- Compare results to literature if available

---

## What We're Looking For

### High Priority

- **Validated pathway examples** from published studies
- **Tool integrations** (GREET, OpenLCA, Aspen converters)
- **Documentation improvements** (especially for newcomers)
- **Schema validation** against real-world use cases
- **Academic partnerships** for credibility and validation

### Medium Priority

- **Visualization tools** for pathway networks
- **Translation** of documentation to other languages
- **Tutorial content** (videos, workshops, course materials)
- **Case studies** from real projects

### Lower Priority (For Now)

- **Optimization frameworks** (wait for stable schema)
- **Advanced features** (temporal dynamics, spatial distribution)
- **Domain-specific modules** (wait for core validation)

---

## Review Process

### Timeline

- **Small changes** (typos, documentation): 1-7 days
- **Medium changes** (new examples, minor fields): 2-4 weeks
- **Large changes** (schema restructuring): 4-8 weeks + community review

### Criteria

Pull requests are evaluated on:

1. **Technical correctness**: Are the changes accurate?
2. **Clarity**: Is the contribution well-documented and explained?
3. **Scope**: Is the change focused and justified?
4. **Compatibility**: Does it break existing pathways?
5. **Community support**: Do others find this useful?

### Approval Process

- **Maintainer approval**: Required for all changes
- **Community review**: Encouraged for significant changes
- **TWG vote**: Required for breaking changes (v0.5+)

---

## Intellectual Property

By contributing, you agree that:

1. Your contribution is your original work or you have rights to submit it
2. You grant an Apache 2.0 license for the contribution
3. You agree to the [Developer Certificate of Origin (DCO)](https://developercertificate.org/)

Add to your commits:
```
Signed-off-by: Your Name <your.email@example.com>
```

Or configure git:
```bash
git config user.name "Your Name"
git config user.email "your.email@example.com"
```

---

## Getting Help

### Resources

- **Documentation**: Start with `docs/QUICKSTART.md`
- **Examples**: Review `pathways/demo_hefa_base.yaml`
- **Schema**: See `schema/pathway_schema.yaml`
- **Glossary**: TEA/LCA terms in `docs/GLOSSARY.md`

### Ask Questions

- **GitHub Discussions**: General questions and brainstorming
- **GitHub Issues**: Specific problems or proposals
- **Email**: contribute@insightquantix.com for private inquiries

### Stay Informed

- **Watch repository**: Get notifications for changes
- **GitHub Releases**: Subscribe to release announcements
- **Community calls**: Quarterly open meetings (schedule TBD)

---

## Recognition

Contributors will be recognized in:

- **CONTRIBUTORS.md**: List of all contributors
- **Release notes**: Credit for specific contributions
- **Academic publications**: Co-authorship for significant technical contributions
- **Website** (when established): Community contributor showcase

---

## First-Time Contributors

New to open source or TEA/LCA? Welcome!

**Good first issues** are tagged with `good-first-issue` label.

**Simple starting points**:
1. Fix a typo in documentation
2. Add a glossary term
3. Improve an example comment
4. Add a citation to a data source

**Don't be intimidated!** Everyone was new once. We're happy to mentor and help you learn.

---

## Questions About Contributing?

- **General**: Open a GitHub Discussion
- **Specific**: Reference this guide in your issue or PR
- **Private**: Email contribute@insightquantix.com

---

**Thank you for helping build a better TEA/LCA ecosystem!**

*Last updated: 2025-01-23*
