---
id: 0001
date: 2026-04-17
status: active
supersedes: null
superseded_by: null
---

# AetherHeal's theory of trust formation

## Prior Position

AetherHeal was originally designed around a conventional two-sided platform thesis. The operating model was: identify the best clinics in Korea, attract the top 20% of the international patient market by socioeconomic segment, charge a percentage of procedure cost as the platform's revenue, and use early volume to attract additional high-quality clinics, which would in turn attract more patients. Trust, in this model, was a consequence of scale — the platform would become trustworthy because it had aggregated quality supply and premium demand, and the aggregation itself would serve as the signal.

This thesis assumed that the core problem in medical tourism was coordination — bringing the right patients to the right clinics — and that a well-executed platform could solve it by virtue of being well-executed.

## Current Position

AetherHeal is designed around a different thesis: trust is a consequence of structure, not of scale. The platform's function is to construct a mechanism in which no participant earns more by recommending worse options for the patient, and in which that property is verifiable from the outside. Once this structure exists, good clinics self-select into participation because the architecture distinguishes them from clinics whose business model depends on information asymmetry. Patients are not segmented by socioeconomic tier; segmentation happens through the demand created by the structure itself.

The percentage-fee model is structurally incompatible with this thesis and has been replaced throughout the system by flat fees — fixed annual hospital verification fees by tier, flat patient navigation fees by service tier, and fixed Angel Physician stipends. No revenue anywhere in AetherHeal scales with procedure cost.

## Causal Update

The shift happened on or around 10 March 2026, while working through Akerlof's 1970 paper *The Market for Lemons* as part of ongoing reading on market design and asymmetric information.

Akerlof's argument is that when buyers cannot distinguish quality and sellers can, the market drives quality out — good sellers exit because they cannot credibly signal quality at a price the market will bear, and the remaining market is populated by lower-quality sellers trading at prices that reflect average rather than true quality. The mechanism is not malice; it is the structural consequence of information asymmetry in the absence of reliable signals.

Applied to international medical tourism, the implication was immediate and uncomfortable. The medical tourism market is an Akerlof market. Patients cannot evaluate clinical quality directly. Price is the only legible signal, and price correlates poorly with quality, so the signal is noise. Good clinics, being unable to credibly distinguish themselves, operate at a margin compressed by the presence of lower-quality clinics charging similar prices. Patients, being unable to identify good clinics, select on price or on marketing sophistication, both of which are uncorrelated or inversely correlated with clinical quality. This is the structure that produced my own failed hair transplant — I chose on price because I had no other signal, and I only recognized the failure after becoming a specialist capable of evaluating what had been done to me.

The original AetherHeal thesis did not solve this problem. It relocated it. A platform that aggregates clinics and patients, charges a percentage of procedure cost, and targets the top 20% of the market is still operating in an Akerlof market, and is still subject to its dynamics. Worse, the percentage-fee structure gives the platform an incentive gradient toward higher-cost options — the same incentive gradient that distorts clinic-side recommendations in the existing market. Even if the platform never consciously acts on this gradient, the gradient exists, which means the platform cannot be a credible trust-producing entity. It can only be a more polished version of the problem it claims to solve.

The corrective insight from Akerlof was not that information asymmetry is a problem — this was already known — but that the solution to an Akerlof market is not better signaling within the existing structure. It is the construction of a new structural mechanism that makes quality legible independent of price, and that removes the incentive to misrepresent quality from every actor in the system. This is what Hurwicz, Myerson, and Roth formalize as mechanism design. The correct response to the lemons problem is not to scale within the broken market; it is to build a mechanism in which the lemons dynamic cannot operate.

Flat fees remove the platform's incentive gradient. Standardized verification with public rejection rates makes quality legible. Patient-satisfaction-based partial refund of navigation fees places the platform's compensation at risk on outcomes rather than on transactions. Independent external physician advisory boards prevent regulatory capture of the verification function. Together, these are not design preferences; they are the structural preconditions for trust to form in a market that otherwise cannot produce it.

The deeper update is about the order of operations. My prior thesis treated trust as an output of a well-executed platform; my current thesis treats trust as an input that the platform's architecture must produce before any transactions are legitimate. This is the distinction that separates AetherHeal from a medical tourism broker. The reversal recorded here is the moment the distinction became architecturally binding rather than aspirational.

---

*This entry is part of The Founder's Errata. Entries are append-only and are never deleted or rewritten. Corrections to this entry, if any, will appear as new entries that reference this one by ID.*
