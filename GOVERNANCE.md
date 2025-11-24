# Governance Model

## Current Reality (v0.5 - Single-Maintainer Phase)

**Status**: This specification is currently maintained by a single organization (Insight Quantix).

### What This Means:
- ✅ **Decision-making**: All technical decisions made by Insight Quantix
- ✅ **Maintenance**: Insight Quantix funds development and documentation
- ✅ **Community input**: Welcomed via GitHub Issues/PRs, but not binding
- ❌ **Multi-stakeholder governance**: Does not exist yet
- ❌ **Independent oversight**: None
- ❌ **Democratic process**: No voting or formal review beyond Insight Quantix

### Why Single-Maintainer Now:
1. **Speed**: Fast iteration during initial development
2. **Clarity**: Clear accountability and decision-making
3. **Resources**: Insight Quantix providing funding and expertise
4. **Transition plan**: Explicit path to community governance (see below)

**This is temporary**. We are actively working toward multi-stakeholder governance by v1.0.

---

## Transition Plan: Current → Community Governance

This document describes:
1. **How governance works today** (single-maintainer)
2. **How we plan to transition** (timeline and milestones)
3. **How you can participate** (contribution paths)

---

## Governance Philosophy (Target State)

The Pathway Specification aims to become a **community-maintained open standard** for TEA/LCA pathway configuration. To achieve this:

1. **Open development**: All discussions, decisions, and changes are public
2. **Technical merit**: Decisions based on engineering validity, not politics
3. **Broad representation**: Input from academia, industry, regulators, and tool developers
4. **Backward compatibility**: Breaking changes minimized; migration paths provided
5. **Reference implementation**: Open-source validation tools maintained alongside spec

---

## Current Phase: Bootstrapping (v0.1 - v0.5)

### Decision-Making

During the initial development phase (versions 0.1 through 0.5):

- **Proposal**: Anyone can propose changes via GitHub Issues or Pull Requests
- **Discussion**: Community feedback solicited for all non-trivial changes
- **Decision**: Insight Quantix makes final decisions, considering community input
- **Transparency**: All decisions documented in GitHub Issues with rationale

### Roles

**Specification Maintainer** (Insight Quantix):
- Review and merge pull requests
- Triage issues and bug reports
- Coordinate releases and versioning
- Maintain reference implementations

**Contributors** (Open to all):
- Submit bug reports and feature requests
- Propose changes via pull requests
- Review and comment on proposals
- Develop tools and implementations

---

## Transition Plan: Toward Community Governance

### Phase 1: Technical Working Group (Target: v0.5)

Establish a **Technical Working Group (TWG)** with representation from:

- Academic institutions (TEA/LCA research groups)
- National laboratories (NREL, Argonne, etc.)
- Industry practitioners (SAF producers, H₂ developers, chemical companies)
- Tool developers (LCA software vendors, modeling platforms)
- Regulatory bodies (EPA, CARB, aviation authorities - advisory capacity)

**TWG Responsibilities**:
- Review major proposals (new fields, structural changes)
- Vote on breaking changes (simple majority required)
- Advise on backward compatibility and migration paths
- Validate reference implementations

**Meeting Cadence**: Quarterly (virtual)

### Phase 2: Formal Standards Body (Target: v1.0+)

Options under consideration:

1. **Independent foundation**: Establish non-profit foundation (e.g., pathway-spec.org)
2. **Existing organization**: Donate to established standards body (e.g., ASTM, ISO TC 207)
3. **Academic consortium**: Host at research institution with industry advisory board

**Decision criteria**:
- Neutral governance (no single-vendor control)
- Sustainable funding model
- International recognition
- Alignment with existing TEA/LCA standards ecosystem

---

## Change Management Process

### Semantic Versioning

The specification follows semantic versioning: `MAJOR.MINOR.PATCH`

- **PATCH** (0.1.1): Clarifications, typo fixes, non-breaking additions
- **MINOR** (0.2.0): New optional fields, backward-compatible extensions
- **MAJOR** (1.0.0): Breaking changes, incompatible restructuring

### Change Categories

#### Category 1: Editorial (No approval required)
- Typo fixes in documentation
- Clarification of existing language
- Example improvements
- Formatting consistency

**Process**: Pull request → Merge

#### Category 2: Minor Additions (Community review)
- New optional fields
- Additional examples
- Extended documentation
- Tool improvements

**Process**:
1. GitHub Issue proposing change
2. 2-week community comment period
3. Maintainer decision
4. Pull request → Merge

#### Category 3: Structural Changes (TWG review, when established)
- New required fields
- Changes to existing field semantics
- Schema reorganization
- Breaking changes

**Process**:
1. GitHub Issue with detailed proposal
2. Community discussion (4 weeks minimum)
3. TWG review and vote (Phase 1+)
4. Implementation PR with migration guide
5. Merge after approval

### Release Schedule

- **Patch releases**: As needed for bug fixes
- **Minor releases**: Quarterly (January, April, July, October)
- **Major releases**: Annual (or when breaking changes justify)

---

## Intellectual Property

### License

The specification itself is licensed under **Apache License 2.0**.

This means:
- ✅ Anyone can implement the spec (commercial or non-commercial)
- ✅ Anyone can modify and extend the spec
- ✅ Anyone can distribute the spec
- ⚠️ Must preserve copyright notices
- ⚠️ Must document modifications

### Patent Policy

**Current commitment** (Insight Quantix):
- No patent claims on the specification format itself
- Royalty-free implementation rights for all users

**Target policy** (v1.0+):
- Formal patent non-assertion covenant
- Require patent grants from all contributors
- Similar to W3C Patent Policy or Apache Patent Grant

### Trademark

"Insight Quantix Pathway Specification" is not trademarked.

Alternative names under consideration:
- Open Pathway Format (OPF)
- TEA-LCA Interchange Format
- Universal Process Pathway (UPP)

Community input welcome on neutral naming.

---

## Funding and Sustainability

### Current Support

- Development time: Insight Quantix (in-kind contribution)
- Infrastructure: GitHub (free for public repositories)
- Documentation: Volunteer contributors

### Future Funding Needs

For sustainable long-term maintenance:

1. **Part-time technical editor** (~0.5 FTE): Coordinate releases, manage issues, review PRs
2. **Infrastructure**: Validation service, CI/CD, documentation hosting
3. **Reference implementations**: Maintain Python/JavaScript/R parsers
4. **Outreach**: Conference presentations, tutorial development

### Potential Funding Sources

- Industry consortium membership fees
- Grant funding (DOE, NSF, EU Horizon)
- In-kind contributions from participating organizations
- Academic institution support

---

## Conflict of Interest

### Disclosure Requirements

Contributors with commercial interests in TEA/LCA tools or products must:

1. Disclose affiliations in GitHub profile or PR comments
2. Recuse from votes on changes that directly benefit their employer
3. Prioritize spec quality over vendor-specific features

### Vendor Neutrality

The specification must:

- Not favor specific commercial tools or platforms
- Not include proprietary data or algorithms
- Support multiple independent implementations
- Avoid design decisions that create vendor lock-in

---

## Communication Channels

### Primary Channels

- **GitHub Issues**: Technical proposals, bug reports, feature requests
- **GitHub Discussions**: General questions, usage examples, brainstorming
- **Mailing List** (planned): Announce releases and major proposals

### Archive and Transparency

- All technical decisions documented in GitHub Issues
- Meeting minutes (when TWG established) published publicly
- Release notes detail all changes with rationale

---

## Code of Conduct

All participants must follow the [Contributor Covenant Code of Conduct](https://www.contributor-covenant.org/version/2/1/code_of_conduct/).

Summary:
- Be respectful and professional
- Focus on technical merit, not personal attacks
- Welcome diverse perspectives and experience levels
- Address conflicts through evidence and constructive dialogue

Violations should be reported to: conduct@insightquantix.com (interim) or TWG chair (future).

---

## Amendments to Governance

This governance document may be amended by:

- **Phase 0 (v0.1-0.4)**: Insight Quantix decision after community input
- **Phase 1 (v0.5+)**: TWG majority vote
- **Phase 2 (v1.0+)**: Process defined by formal standards body

All amendments must:
1. Be proposed via GitHub Issue
2. Have 30-day comment period
3. Include clear rationale
4. Preserve open-source nature of specification

---

## Questions and Feedback

Governance questions should be directed to:

- **GitHub Issue**: Tag with `governance` label
- **Email**: governance@insightquantix.com
- **Community call**: Quarterly open meetings (schedule TBD)

---

*This governance model is itself a v0.1 draft. Feedback welcome.*

*Last updated: 2025-01-23*
