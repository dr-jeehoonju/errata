---
id: 0002
date: 2026-06-05
status: active
supersedes: null
superseded_by: null
---

# From a medical-tourism platform to augmented-medicine infrastructure

## Prior Position

Entry 0001 corrected *how* AetherHeal produces trust — from a consequence of scale to a consequence of structure — but it left the underlying category of the company untouched. AetherHeal was still, in both versions, a **medical-tourism platform**: an entity whose product is the act of connecting an international patient to a verified Korean clinic, with the trust mechanism (flat fees, public rejection rates, outcome-linked refunds, independent advisory boards) as the thing that made the connection legitimate. The matching-and-navigation layer was the product; the trust architecture was the property that distinguished our matching from everyone else's.

The implicit assumption was that a sufficiently well-constructed trust mechanism, wrapped around patient↔clinic matching, was itself a defensible business. The company's center of gravity was the connection.

## Current Position

AetherHeal is an **AI-augmented medicine certification / infrastructure company**, not a matching platform. The product is no longer the connection between patient and clinic; it is the **trust + certification + proprietary-outcome-data layer on which each specialist owns their own specialty's vertical clinical AI.**

The structural thesis of 0001 is not reversed by this — it is preserved and promoted. The trust mechanism is now the *moat*, sitting alongside a proprietary outcome dataset. What reversed is the category of company built on top of that moat. Three things follow:

- **AetherHeal does not author every specialty's AI.** Authority is domain-specific. For each specialty we invite a domain specialist — preferably professor-grade — to co-author that specialty's vertical AI, so every vertical is anchored on its own author's clinical authority rather than on borrowed authority. This is the structural answer to the obvious objection ("a dermatologist cannot credibly author internal-medicine AI"): the answer is that he does not — the internal-medicine specialist does.
- **Dermatology is the wedge.** DermatoScan, authored by me in the one domain where I am the authority, is the first vertical. It must prove three things: a hospital adopts physician-grade decision support; the AI generates a proprietary outcome dataset; and patient routing to that hospital works — **with explicit incentive separation**, so that selling AI to a hospital and routing patients to it never recreates the referral-kickback structure 0001 was built to abolish. The platform earns the same fee regardless of which verified hospital is chosen.
- **The build is the full unified platform**, not a trimmed validation slice — central orchestration agent, concierge, Dockie-Talkie realtime interpretation, and the per-specialty augmented-medicine vertical. The modules already exist in isolation; the work is unification.

The first closed loop (Step 0) does not change: a patient still pays for navigation and is protected. What changes is the destination — that patient is routed to a DermatoScan-verified hospital, so a single transaction validates the trust mechanism *and* begins outcome-data collection.

## Causal Update

The trigger was the rate of capability release after Opus 4.5. Once general-purpose agents could orchestrate a multi-step cross-border care journey out of the box, the orchestration layer — the thing a "platform" mostly is — became commoditized. A pure patient↔doctor matching layer, however well-built, is no longer defensible, because the part of it that is hard to build is now available to anyone. This diagnosis is one I hold with high confidence, and it is what forced the question 0001 had not asked: if matching is commoditized, what is the company?

The decision crystallized on 4–5 June 2026, and it was stress-tested rather than simply adopted. My first articulation was maximalist: build vertical AI for *every* specialty myself, supply it to hospitals, and route patients to those hospitals. That version was wrong, for reasons that became sharp under examination and that I want recorded here because they are the load-bearing part of the update:

1. **Authority does not generalize across domains.** DermatoScan is credible because I am a dermatologist. The moment I author internal-medicine AI, I become "a dermatologist selling internal-medicine software," and the authority anchor — the actual source of trust — snaps. Being a trusted clinical author across all specialties is not difficult; it is impossible.
2. **Regulatory surface scales with breadth.** Clinical software that supports diagnostic or treatment decisions can fall under SaMD and the attendant approval regime. "Ship every specialty" opens that surface everywhere at once — the precise failure mode behind the Watson Health collapse, which failed not on technology but on scope: dozens of indications, each with its own validation, regulatory, EMR-integration, and sales cycle, attempted simultaneously.
3. **The maximalist form re-creates the disease 0001 was meant to cure.** Selling AI to a hospital while routing patients to that same hospital reintroduces a referral-kickback incentive in new clothing. A patient could rightly ask whether they are being sent somewhere because it is best for them or because that hospital is a customer. Without deliberately designed incentive separation, the new model eats the old moat.

The resolution converts the authority problem from a bug into the structure: AetherHeal becomes the certification + outcome-data + trust *infrastructure* on which each specialist authors their own vertical, each invited specialist (ideally professor-grade) carrying the authority for their domain. Dermatology is the wedge because it is the one specialty where I am that specialist. This is the only form of the pivot that stays consistent with 0001 — the moat is still structure, not the AI stack — while answering the question that capability commoditization forced.

One distinction the word "pivot" tends to hide, and which I am recording so it cannot be quietly assumed away later: a built artifact is not a closed revenue loop. The four pillars exist as modules; that is not the same as one real patient paying and being protected end to end. The vision expanded to the full platform; the binary checkpoint did not move. What proves this company by the end of July is still a single patient who pays and is protected — and the thing that carries them across that line is the trust mechanism of 0001, not the AI stack.

---

*This entry is part of The Founder's Errata. Entries are append-only and are never deleted or rewritten. Corrections to this entry, if any, will appear as new entries that reference this one by ID.*
