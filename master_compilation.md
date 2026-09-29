# MASTER COMPILATION — Dementia Knowledge Base for NEUROVA
### (Research data + derived reasoning only — NEUROVA pitch/business material excluded)

This file compiles everything currently available for building a vector
knowledge base: the original clinical research reference, plus all
derived reasoning, decision structures, and schemas produced during
analysis of that document. Each section is explicitly labeled by type so
downstream chunking (e.g. via Antigravity) can tag provenance correctly
when splitting into a vector store.

Labels used throughout:
- `[SOURCE]` = verbatim or near-verbatim from the original uploaded
  research document. Treat as ground-truth clinical/epidemiological
  reference.
- `[DERIVED]` = synthesized/engineered by analysis, NOT stated in the
  original document. Illustrative scaffolding, not validated clinical
  guidance. Requires clinical review before production use.
- `[SCHEMA]` = a data-collection structure (fields to fill per patient),
  not content itself.

---

## PART 1 — [SOURCE] ORIGINAL CLINICAL RESEARCH REFERENCE

DEMENTIA — A COMPREHENSIVE REFERENCE DOCUMENT

1. INTRODUCTION AND SCOPE

This document lays out, in as much depth as is useful, what dementia
actually is: its biological basis, its different forms, how it is
diagnosed, how it is currently treated, who it affects and how many
people, what genuinely helps prevent or delay it, and where the live
research frontier is right now. It is written to be read start to finish
by someone who wants a working command of the subject, not just
definitions to memorize.


2. WHAT DEMENTIA ACTUALLY IS

Dementia is not a single disease. It is a clinical syndrome — a
collection of symptoms with a shared shape, caused by several different
underlying diseases — defined by a decline in cognitive function severe
enough to interfere with a person's ability to carry out everyday
activities independently. The clinical threshold that separates dementia
from ordinary age-related forgetfulness is functional impact: forgetting
where you left your keys is normal; forgetting what keys are for, or
being unable to safely live alone because of memory and judgment
problems, is not.

At the biological level, dementia results from progressive damage to
neurons (brain cells) and to the synaptic connections between them. This
damage disrupts the brain's ability to store, retrieve, and process
information. Different diseases cause this damage through different
mechanisms and in different regions of the brain, which is why the
symptom pattern — what breaks down first, and how — varies meaningfully
between the major types described below.


3. THE MAJOR TYPES OF DEMENTIA

3.1 Alzheimer's Disease
The most common cause of dementia, accounting for an estimated 60-70% of
cases. It is characterized by two hallmark pathological features: amyloid
plaques, which accumulate outside neurons, and neurofibrillary tangles of
a protein called tau, which accumulate inside neurons. Both disrupt
normal cell signaling and eventually cause cell death. The disease
typically begins in the hippocampus (the brain's memory-formation center),
which is why short-term memory loss is usually the earliest and most
prominent symptom, before spreading to affect language, reasoning, and
personality as it progresses.

3.2 Vascular Dementia
The second most common form. It results from reduced blood flow to the
brain — either from a series of small strokes (sometimes clinically
silent, meaning the person never noticed having one) or from a single
larger stroke, or from chronic small-vessel disease that starves brain
tissue of oxygen over time. Because the damage is tied to discrete
vascular events, vascular dementia often progresses in a stepwise pattern
— a noticeable decline following a stroke, followed by a plateau, followed
by another decline after the next event — rather than the smoother,
gradual decline typical of Alzheimer's.

3.3 Lewy Body Dementia
Caused by abnormal clumps of a protein called alpha-synuclein (Lewy
bodies) inside neurons. It shares biological overlap with Parkinson's
disease and often produces movement symptoms (tremor, stiffness, slowed
movement) alongside cognitive decline. Distinctive features include
visual hallucinations, marked fluctuations in alertness and attention
even within a single day, and unusually severe sensitivity to certain
antipsychotic medications — a detail that matters clinically, since
misdiagnosing Lewy body dementia as Alzheimer's and prescribing the wrong
medication can cause serious harm.

3.4 Frontotemporal Dementia (FTD)
Distinct from the other major types in that it typically begins earlier
in life, often in a person's 50s, and initially spares memory. It affects
the frontal and temporal lobes of the brain — regions governing
personality, social behavior, judgment, and language — so it often first
appears as a change in personality or behavior (disinhibition,
apathy, loss of social tact) or as a language disorder, rather than
forgetfulness. This makes it frequently misdiagnosed early on as a
psychiatric condition rather than a neurological one.

3.5 Mixed Dementia
Very common, especially in older patients: the coexistence of more than
one underlying pathology, most often Alzheimer's disease alongside
vascular damage. Autopsy studies suggest mixed pathology is present in a
substantial proportion of dementia cases even when only one type was
diagnosed clinically.

3.6 Potentially Reversible Causes
A clinically important category: some conditions that mimic dementia are
treatable if caught early, including vitamin B12 deficiency, thyroid
dysfunction (hypothyroidism), normal-pressure hydrocephalus, certain
infections, and medication side effects (particularly in elderly patients
on multiple drugs). This is precisely why a proper diagnostic workup,
rather than an assumption of irreversible dementia, matters — a
meaningful minority of cases are at least partially treatable.


4. CLINICAL STAGES AND SYMPTOM PROGRESSION

Clinicians generally describe dementia progression in three broad stages,
though the underlying reality is a continuous decline rather than sharp
jumps between categories.

Early stage: difficulty finding words, misplacing items and being unable
to retrace steps, trouble with planning or organizing, mild
disorientation in unfamiliar settings, and subtle personality or mood
shifts. At this stage, the person is often still functionally independent
and may actively try to compensate — writing more notes, avoiding
unfamiliar situations.

Middle stage: the longest stage for most patients, often lasting several
years. Memory loss becomes pronounced, including forgetting the names of
close family members; confusion about time and place deepens; wandering
becomes a genuine safety risk; behavioral changes such as agitation,
suspicion, or repetitive actions appear; and the person increasingly
needs help with basic daily activities like dressing, bathing, and eating.

Late stage: severe impairment across the board. Verbal communication
largely breaks down; physical function declines, including walking and
eventually swallowing; the person becomes fully dependent on caregivers
for all activities of daily living. Swallowing difficulty in particular
raises the risk of aspiration pneumonia, which is a leading cause of
death in advanced dementia.


5. HOW COMMON IS DEMENTIA — GLOBAL, NATIONAL, AND REGIONAL PICTURE

5.1 Global burden
The 2024 Lancet Commission report estimates roughly 57 million people
were living with dementia worldwide in 2019, and projects this will
nearly triple to approximately 153 million by 2050, driven primarily by
population ageing. Critically, the steepest increases are expected in
low- and middle-income countries — meaning the burden is shifting toward
exactly the health systems least equipped to absorb it, India's included.

5.2 India
National estimates put the number of Indians aged 60 and above currently
living with dementia at approximately 8.8 million, with a prevalence of
roughly 7.4% within that age group. That figure is projected to rise to
approximately 17 million by 2036 as India's elderly population continues
to grow.

5.3 The North-Eastern Region specifically
Published research on healthcare delivery in NER (a 2024 study using
qualitative analysis of frontline health worker experience, published via
JMIR in partnership with the Indian Council of Medical Research)
documents structural barriers specific to the region: difficult terrain,
limited road infrastructure, and geographic isolation that make regular
service delivery to remote communities genuinely difficult. Layered on
top of this is India's broader elderly digital-access gap — independent
reporting on Digital India's rural rollout found that only around 9% of
Indians aged 60+ can navigate the internet independently, the lowest
rate of any demographic segment — and NER's substantial linguistic
diversity, where dozens of distinct languages and dialects are spoken
across the region, often underserved by mainstream Hindi/English digital
health products.


6. RISK FACTORS

6.1 Non-modifiable factors
Age is the single largest risk factor — incidence roughly doubles every
five years after age 65. Genetics play a meaningful role: the APOE4 gene
variant is the strongest known genetic risk factor for late-onset
Alzheimer's, though carrying it does not guarantee the disease develops,
and not carrying it does not guarantee immunity. Family history and
biological sex (dementia is somewhat more prevalent in women, partly
reflecting longer average lifespan) also factor in.

6.2 Modifiable factors — the Lancet Commission framework
This is the section with the most direct public-health and product-design
relevance. The 2024 Lancet Commission on Dementia Prevention, Intervention
and Care (led by Professor Gill Livingston, University College London,
published in The Lancet, 31 July 2024) identified 14 evidence-based
modifiable risk factors spanning the life course, and calculated that
addressing all of them could theoretically prevent or delay approximately
45% of dementia cases worldwide. The 14 factors, with their individually
estimated contribution to dementia risk, are:

Early life: less education (5%)

Midlife: hearing loss (7%), high LDL cholesterol (7%), depression (3%),
traumatic brain injury (3%), physical inactivity (2%), diabetes (2%),
smoking (2%), hypertension (2%), obesity (1%)

Late life: social isolation (5%), air pollution (3%), untreated vision
loss (2%)

(High LDL cholesterol and untreated vision loss were newly added in the
2024 update; the other 12 factors were carried forward from the
Commission's earlier 2017 and 2020 reports.)

The Commission's specific recommendations built on this evidence include:
ensuring access to quality education and cognitively stimulating activity
in midlife; making hearing aids accessible and reducing harmful noise
exposure; effectively treating depression; promoting head protection in
contact sports and cycling; and encouraging regular physical exercise,
which is independently associated with lower dementia risk. A follow-up
2025 academic paper further argued that a fuller, more globally
equitable risk model should also account for poverty, income inequality,
wealth shocks, and HIV prevalence — factors disproportionately relevant
to under-resourced regions, and worth keeping in mind for a project
targeting NER specifically.


7. DIAGNOSIS

There is no single definitive test for most forms of dementia while a
person is alive; diagnosis is built from converging evidence:

- Clinical history, gathered from both the patient and a close family
  member or caregiver, since patients often cannot accurately self-report
  the extent of their own decline.
- Cognitive and neuropsychological testing — standardized tools such as
  the Mini-Mental State Examination (MMSE) and the Montreal Cognitive
  Assessment (MoCA), which use structured tasks (recall, orientation,
  drawing, language) to quantify impairment.
- Laboratory tests to rule out reversible causes — thyroid function,
  vitamin B12 levels, and screening for infection.
- Brain imaging — MRI or CT scans to detect strokes, tumors, or patterns
  of brain shrinkage consistent with specific dementia types.
- In specialist settings, PET imaging or cerebrospinal fluid analysis can
  directly measure amyloid and tau levels, though these remain expensive
  and are not widely accessible in India, particularly outside major
  metropolitan centers.


8. TREATMENT LANDSCAPE

8.1 Established symptomatic medications
Cholinesterase inhibitors (donepezil, rivastigmine, galantamine) and
memantine have been standard treatments for years. They do not alter the
underlying disease process or halt progression, but can meaningfully help
manage symptoms for a period of time. They are widely available and
comparatively affordable in India.

8.2 The new generation — disease-modifying monoclonal antibodies
This is the most significant shift in dementia treatment in roughly three
decades. Lecanemab (brand name Leqembi) received traditional FDA approval
in July 2023, and donanemab (brand name Kisunla) followed in July 2024 —
both are monoclonal antibodies that work by binding to and clearing
amyloid plaques from the brain. In lecanemab's pivotal Phase 3 CLARITY-AD
trial, the drug slowed cognitive decline by approximately 27% over 18
months compared to placebo; donanemab has shown comparable effects, with
some reporting suggesting a range of roughly 27-35% depending on the
population studied. Put in practical terms, independent clinical
commentary has described the real-world effect as being difficult to
notice directly in day-to-day memory — the honest framing is that the
drug may modestly slow the rate of decline rather than visibly restore
function.

Both drugs carry a specific, non-trivial safety concern known as ARIA
(amyloid-related imaging abnormalities) — swelling or micro-bleeding in
the brain, detected via monitoring MRI scans — which occurs more
frequently in patients who carry the APOE4 gene variant. Both remain
approved only for patients in the earliest, mild stages of Alzheimer's
disease, require regular intravenous infusion at a clinical facility,
and — critically for the Indian and NER context — remain expensive and
are not, as of this document being prepared, widely accessible or
affordable within the Indian healthcare system. Clinical guidance
consistently describes both drugs as adjunct rather than first-line
therapy, reserved for carefully selected early-stage patients under
specialist supervision.

8.3 Non-pharmacological approaches
This is the category most directly relevant to accessibility-focused,
low-resource-setting projects, and it is genuinely evidence-backed rather
than a consolation-prize alternative to drugs.

Cognitive Stimulation Therapy (CST) is a structured, group-based,
non-drug intervention involving memory, language, orientation, and social
activities, generally delivered by a trained facilitator. It has a solid
evidence base as a way to support cognitive function and quality of life,
though it depends on access to trained personnel and a suitable venue —
a real constraint in remote settings.

individual Cognitive Stimulation Therapy (iCST) adapted the same
underlying model for delivery at home by a family caregiver rather than a
professional facilitator, and has been tested in peer-reviewed randomized
controlled trials — establishing that caregiver-delivered cognitive
stimulation is a legitimate, studied model, not merely a theoretical
workaround.

In the Indian context specifically, NIMHANS Bengaluru has developed and
piloted two directly relevant programs: iCARE (Individualized Cognitive
Augmentation Regimen for Elderly), a caregiver-driven training program
where caregivers are trained as active co-therapists across multiple
cognitive domains, with pilot data (32 patient-caregiver pairs) showing
improvement across attention, memory, and executive function; and CDCT
(Caregiver-Driven Cognitive Training), built around nine structured
cognitive tasks, whose feasibility study reported improved cognitive
function, better quality of life, and increased caregiver confidence.

Beyond structured cognitive training, physical exercise has an
independently documented association with reduced dementia risk and
better outcomes for people already diagnosed, and social engagement and
routine/environmental structuring (consistent schedules, clearly labeled
spaces) measurably reduce confusion and agitation in daily care.

Digital versions of these interventions — computerized cognitive training
(CCT) delivered via tablet or phone — have been studied extensively.
Recent systematic reviews and meta-analyses (2025 and 2026) of digital
cognitive-training interventions in older adults with mild cognitive
impairment or dementia report measurable improvements in domains
including attention, processing speed, working memory, and episodic
recall — but consistently note that effectiveness varies substantially
depending on intervention design, usability, and cultural fit. That
variability is the actual open problem in this space, not whether digital
cognitive support can work at all.


9. THE CAREGIVING REALITY

Dementia's practical burden extends well beyond the diagnosed patient.
Caregivers — typically a spouse or adult child, and in the Indian context
overwhelmingly informal, unpaid family members rather than professional
staff — face documented elevated rates of depression, chronic stress, and
physical health decline, driven by the near-continuous nature of
dementia care as the disease progresses. Formal support infrastructure
(respite care, trained home-health aides, caregiver counseling) remains
limited in India generally and considerably more so outside major
metropolitan centers — which is precisely why intervention models that
actively train and support the caregiver, rather than treating them as
incidental to the patient's care, have shown particular relevance and
promise in the Indian research described above.


10. THE COMMERCIAL AND INSTITUTIONAL LANDSCAPE IN INDIA

Elder-care and dementia-adjacent technology is an active, funded space in
India, though concentrated in urban, higher-income markets:

- Emoha Elder Care, backed by Lumis Partners, offers emergency response,
  health monitoring, and companionship services, reportedly serving over
  100,000 users across 120 cities, including wearable tracking
  specifically for dementia patients. Its core model is monitoring and
  emergency response rather than cognitive intervention.
- KITES Senior Care and Epoch Elder Care offer dementia-inclusive home
  care and assisted-living services, concentrated in metro and tier-1
  cities such as Delhi-NCR, Mumbai, and Pune.
- Ivory, a Karnataka-based health-tech startup, offers cognitive
  assessments and personalized brain-health programs for seniors,
  explicitly framed around India's rising dementia burden.
- Independent, lower-cost hardware efforts also exist, such as a
  student-built wearable ("Alpha Monitor") designed to alert caregivers
  to unusual movement patterns or wandering behavior in Alzheimer's
  patients.

None of these are built specifically around offline-first operation,
regional-language delivery, or the geographic and connectivity
constraints characteristic of the North-Eastern Region — which remains a
genuine, verifiable gap in the current market rather than an assumed one.


11. CURRENT RESEARCH FRONTIERS

Three areas of active research are worth understanding, since they shape
where the field — and any technology built within it — is heading:

Early and accessible detection: researchers are actively developing
blood-based biomarker tests for Alzheimer's pathology, aiming to reduce
reliance on expensive PET imaging or invasive spinal fluid testing for
earlier, more widely accessible diagnosis.

Next-generation disease-modifying drugs: beyond the amyloid-targeting
antibodies already approved, tau-targeting therapies are progressing
through Phase 3 clinical trials, aiming at a different piece of the
disease's underlying biology; industry reporting indicates well over a
hundred Alzheimer's drug candidates remain in active clinical
development.

Prevention-focused public health strategy: given the Lancet Commission's
45% modifiable-risk estimate, research attention is shifting toward
population-level interventions — hearing-aid access programs, vision-care
access, cardiovascular risk management, and social-isolation reduction —
as strategies with potentially larger real-world impact than any single
drug, particularly in resource-constrained settings where expensive
biologic therapies are not realistically accessible.


12. COMMON MISCONCEPTIONS WORTH ADDRESSING DIRECTLY

"Dementia is just normal aging" — inaccurate; it is a disease process,
clinically distinguished from normal age-related cognitive change by its
severity and functional impact.

"It only affects memory" — inaccurate; language, judgment, personality,
motor function, and eventually basic physical function are all affected
as the disease progresses.

"Nothing can be done without a cure" — inaccurate and consequential;
cognitive stimulation, structured routines, physical activity, and social
engagement have a genuine, evidence-backed impact on quality of life and
functional trajectory, independent of any pharmaceutical cure.

"Only elderly people get it" — mostly accurate as a matter of overall
prevalence, but frontotemporal dementia in particular can present as
early as a person's 50s, and "young-onset" dementia, while less common,
is a recognized clinical category.


13. SOURCES

- 2024 Lancet Commission on Dementia Prevention, Intervention, and Care
  (Livingston G, Huntley J, Liu KY, et al.), The Lancet, published online
  31 July 2024 — 14 modifiable risk factors, 45% preventability estimate,
  global case projections (57 million in 2019 to 153 million by 2050).
- Broadening dementia risk models: building on the 2024 Lancet Commission
  report for a more inclusive global framework (2025), on equity-focused
  extensions to the Commission's risk model.
- National prevalence estimates for dementia among India's 60+ population
  (~8.8 million, ~7.4% prevalence), PubMed-indexed nationwide study.
- Projection of ~17 million dementia cases in India by 2036, reported via
  NITI Aayog's Frontier Tech coverage of the age-tech startup Ivory.
- Healthcare delivery challenges specific to North-Eastern India's
  terrain and geography, JMIR-published qualitative study conducted with
  the Indian Council of Medical Research, 2024.
- Elderly digital-independence rate in India (~9% of 60+ population),
  reporting on Digital India's rural digital-literacy rollout.
- iCST (individual Cognitive Stimulation Therapy) randomized controlled
  trial protocol and findings, peer-reviewed, PMC.
- iCARE (Individualized Cognitive Augmentation Regimen for Elderly) and
  CDCT (Caregiver-Driven Cognitive Training), NIMHANS Bengaluru,
  published findings in Alzheimer's & Dementia journal / International
  Journal of Clinical Trials.
- Lecanemab (Leqembi) FDA approval and CLARITY-AD Phase 3 trial results
  (July 2023); donanemab (Kisunla) FDA approval (July 2024); ongoing
  clinical and safety commentary on both, including ARIA risk and APOE4
  interaction, from multiple 2025-2026 clinical and pharmacology sources.
- Indian elder-tech commercial landscape (Emoha, KITES Senior Care, Epoch
  Elder Care, Ivory, independent hardware efforts), reporting via
  ThePrint, YourStory, and NITI Aayog's Frontier Tech platform.

As with the earlier project brief, this document is built from real,
checkable sources, but it is worth your team reading the primary Lancet
Commission report and the NIMHANS studies directly before quoting exact
figures in front of judges or a clinical audience.


---

## PART 2 — [DERIVED] GENERAL DEMENTIA-DOMAIN DECISION FRAMEWORK

The following principles were distilled from Part 1 as general,
cross-patient reasoning rules (not diagnosis, not patient-specific data)
intended to inform an LLM's decision-making when generating a
support routine or plan.

### 2.1 Stage-appropriate behavior rules
- Early stage: person can still compensate (notes, habits) → routine
  should nudge independence, not replace it.
- Middle stage: wandering becomes a real risk, agitation/suspicion
  appears → routine needs safety structure and calming pacing.
- Late stage: verbal/physical decline, full dependence → routine shifts
  to comfort/sensory support rather than task-completion.

### 2.2 Why routine/structure itself helps (mechanism)
Consistent schedules and clearly labeled spaces measurably reduce
confusion and agitation (see Part 1, non-pharmacological approaches
section). Predictability itself is the therapeutic lever — not the
specific activity chosen.

### 2.3 Evidence-based activity categories (the toolbox)
- CST-style domains: memory, language, orientation, problem-solving,
  recognition, discussion, social interaction.
- Reminiscence-based activities (photos, songs, places, festivals) — a
  distinct, validated category with emotional/social benefit separate
  from pure cognitive drilling.
- Physical exercise — independently evidence-backed, not merely
  supplementary.

### 2.4 Personalization logic pattern (strength-first sequencing)
Start from the person's strongest cognitive domain and bridge toward
weaker domains, rather than drilling weaknesses head-on. Example logic:
- Patient with strong memory / weak attention → sequence: memory task →
  attention-bridging task → harder tasks.
- Patient with weak memory / strong recognition → sequence: recognition
  → familiar objects → reminiscence → simple memory recall.

### 2.5 Guardrails on what performance data means
Game/task performance is not equivalent to clinical improvement. Poor
performance may reflect sensory or motor limitations rather than
cognitive decline. Do not over-adjust a plan based on a single session.

### 2.6 Caregiver-burden awareness as a planning constraint
A good plan must be sustainable for the caregiver (not too long, not too
complex, should build caregiver confidence), not only beneficial for the
patient. This is grounded in documented caregiver burden (Zarit scores)
in Part 1.

### 2.7 Sundowning-adjacent structural timing
General timing principle: place higher-demand cognitive tasks earlier in
the day; shift to calmer, familiar activities later, since behavioral
changes (agitation, confusion) are more likely later in the day.

### 2.8 Safety-by-design principle
Once a plan reflects middle-stage functioning, default to including
check-in/safety cues (e.g. door locked, water filled) without needing
this to be specified per-patient.

### 2.9 Ethical guardrail — what cannot be claimed
No digital or cognitive-training intervention has proven disease-
modifying effects. Never frame output as treating, curing, reversing, or
preventing dementia. Never claim to replace professional/clinical care.
Correct framing: the platform supports engagement, structure, and
caregiver capability; any claim of cognitive benefit requires proper
clinical validation via measurable outcomes (adherence, engagement,
caregiver burden, quality of life).

---

## PART 3 — [DERIVED] STAGE DECISION TABLE

| Stage | Priorities | Avoid | Example activity types (illustrative only) |
|-------|------------|-------|------------------------|
| Early | Independence-preserving scaffolding; habit formation; mild challenge + novelty; external aids (notes, labels, calendars) | Over-helping; replacing the person's own initiation; activities that feel infantilizing | Short memory + language games with written cues; light physical + planning tasks; orientation with calendars/photos of current season |
| Middle | Safety structure; calming pacing; short cognitive windows early in day; clear transitions; reduced open-ended choice | Long multi-step sequences; high failure-risk tasks; overstimulation; unsupervised transitions | Recognition + reminiscence with photos/songs; simple physical movement with verbal cues; short discussion of familiar topics; labeled environment check-ins |
| Late | Comfort, sensory, relational presence; reduce distress; familiar sensory input | Task-completion goals; verbal demands; novel or complex sequencing | Familiar music + gentle touch; preferred scents/textures; simple presence + eye contact; passive sensory (watching birds, feeling fabric) |

---

## PART 4 — [DERIVED] WORKED EXAMPLE ROUTINES (strength-first sequencing applied end-to-end)

### Example A — Early-stage, strong residual memory, weaker attention
Goal: Preserve independence while gently exercising attention.
1. Memory warm-up (strongest domain) — "Tell me three things you did this morning."
2. Bridge into attention — three labeled photo cards of familiar people; point to each while saying the name.
3. Light physical + orientation — walk to the window, note weather/season on a wall calendar.
4. Close with independence cue — person writes one appointment/reminder on their own notepad.
Duration ~20–25 min. Caregiver role: supply materials, stay mostly silent, praise effort not perfection.

### Example B — Middle-stage, strong recognition, weaker memory & initiation
Goal: Safety + engagement without high failure risk.
1. Recognition lead — 4–5 large photos of family/favorite places; person points or names what they recognize.
2. Reminiscence bridge — one familiar song from the same era; ask only "Do you like this one?" (no free recall demand).
3. Simple physical with cue — seated marching or arm raises to the song rhythm.
4. Safety/orientation close — check door locked / water filled / bathroom label visible.
Duration 15–20 min. Caregiver role: keep transitions short, verbal cues concrete.

### Example C — Late-stage, residual sensory & emotional responsiveness
Goal: Comfort and reduce distress only.
1. Preferred music at low volume.
2. Soft familiar texture (favorite blanket or sweater) placed in the person's hands.
3. Caregiver sits at eye level, gentle touch on hand or shoulder if tolerated, minimal speech.
4. End when the person shows signs of settling or fatigue; no "task complete" language.
Duration flexible (5–15 min). Caregiver role: presence, not performance.

---

## PART 5 — [DERIVED] ACTIVITY SEED LIST (concrete tasks per category)

- **Memory**: "Name three things you ate yesterday"; "What was the name of your first school?"; simple "what comes next" with a short familiar sequence.
- **Language**: Finish a well-known proverb or song lyric; describe a familiar object in the room in one sentence.
- **Orientation**: Point to the correct day/season on a large calendar; name the room you are in.
- **Recognition**: Match faces to names from a small set of family photos; identify common household objects from pictures.
- **Problem-solving**: Sort 4–5 objects by color or size; "what do you need to make tea?" with picture cues.
- **Discussion / social**: "What did you enjoy about that song?"; "Tell me about a favorite holiday."
- **Reminiscence**: Look at wedding or festival photos; listen to music from the person's young adulthood; handle a familiar object from their past work or hobby.
- **Physical**: Seated marching; arm circles to music; short supervised walk to a labeled destination; gentle stretching with verbal cues only.

---

## PART 6 — [DERIVED] STANDING GUARDRAILS / HARD RULES

- Per-patient intake data always overrides generic defaults. If the person
  dislikes music, has a mobility restriction, sensory impairment, or any
  other stated preference/limitation, adapt or replace the corresponding
  activity.
- If intake data is incomplete, default to the most conservative option
  (assume "middle stage" priorities) until told otherwise, and state
  explicitly which fields were missing.
- Never adjust overall plan difficulty or claim clinical change based on
  a single session.
- Poor performance may be sensory, motor, fatigue, mood, medication, or
  environmental — not automatically cognitive decline.
- Never frame any output as treating, curing, reversing, or stopping
  dementia. Use only language of support, engagement, residual ability,
  structure, and distress reduction.
- Every plan must stay realistic in length and complexity for the
  caregiver's actual available time.
- Once the plan reflects middle-stage functioning, default to including
  safety and orientation cues.
- Place higher-demand activities earlier in the day; shift toward
  calmer, familiar activities later.
- If intake notes a history of distress/agitation/a specific trigger
  tied to an activity type, do not include that activity type again;
  substitute the nearest safe alternative from the same category.
- If not given enough information to build a safe plan, ask for the
  minimum missing fields rather than guessing all of them.

---

## PART 7 — [SCHEMA] PATIENT INTAKE CHECKLIST (fields to collect per patient)

This is a data-collection schema, not content — the variable, per-patient
layer that combines with Parts 1–6 (the fixed reasoning layer) at
generation time.

### 7.1 Basic & diagnostic context
- Age, sex
- Type of dementia (if diagnosed) and current stage (early/middle/late)
- Doctor's notes/prescription details relevant to daily function
- Known comorbidities (diabetes, hypertension, etc.)

### 7.2 Cognitive & functional baseline
- Domain-by-domain strengths/weaknesses: memory, attention, recognition, language, problem-solving
- MMSE/MoCA score or rough clinician assessment, if available
- Level of independence: what they can do alone vs. what needs supervision

### 7.3 Sensory & physical constraints
- Hearing status (needs voice loud/slow? hearing aid?)
- Vision status (needs large text/high contrast?)
- Mobility/motor limitations
- Literacy level in their language

### 7.4 Daily rhythm
- Wake time, sleep time, nap habits
- Meal times
- Medication schedule (times, names — for reminder purposes only)
- Best/worst times of day for engagement (sundowning risk window)

### 7.5 Personal & cultural content (for reminiscence activities)
- Names and photos of close family members
- Familiar places, festivals, songs, foods
- Preferred language/dialect

### 7.6 Behavioral & safety flags
- Known triggers for agitation or confusion
- History of wandering or getting lost
- Emergency contacts
- Past safety incidents

### 7.7 Caregiver-side info
- Primary caregiver identity and realistic daily availability
- Caregiver's comfort with technology
- Caregiver's current stress/burden level

### 7.8 Ongoing feedback (logged over time, not at intake)
- Daily activity log: completed / skipped / enjoyed / agitated
- Free-text notes on what worked or didn't, day to day

---

## PART 8 — [DERIVED] DEPLOYMENT SYSTEM PROMPT (for reference / re-chunking)

The following is the full system-prompt text already engineered for
Ollama + llama3.2. Included here for completeness so the vectorization
step has the deployed version alongside its source material.

CLINICAL REVIEW REQUIRED BEFORE PRODUCTION USE
The concrete activities, durations, physical examples, and sensory suggestions
below are derived engineering illustrations, NOT validated recommendations
from the original research document, NIMHANS, the Lancet Commission, or any
clinical guideline. A qualified clinician or experienced dementia caregiver
must review and approve (or replace) these examples before real families use
this system.

===================================================================
SYSTEM PROMPT (copy-paste into Ollama / your app's system role)
===================================================================

You are a dementia-support routine generator. You produce structured daily or
session routines that support residual abilities, reduce distress, and stay
sustainable for caregivers. You never diagnose, treat, cure, or claim to
reverse dementia.

=== CORE DECISION TABLE (DERIVED / ILLUSTRATIVE) ===
Stage  | Priorities | Avoid | Example activity types (illustrative only)
Early  | Independence-preserving scaffolding, habit formation, mild challenge + novelty, external aids | Over-helping, replacing the person's own initiation, infantilizing tasks | Short memory + language games with written cues; light physical + planning; orientation with calendars/photos
Middle | Safety structure, calming pacing, short cognitive windows early in day, clear transitions, reduced open-ended choice | Long multi-step sequences, high failure-risk tasks, overstimulation, unsupervised transitions | Recognition + reminiscence with photos/songs; simple cued physical movement; short familiar discussion; labeled environment check-ins
Late   | Comfort, sensory and relational presence, reduce distress, familiar sensory input | Task-completion goals, verbal demands, novel or complex sequencing | Familiar music at low volume; preferred textures; quiet presence; passive sensory experiences

=== STRENGTH-FIRST SEQUENCING (DERIVED RULE) ===
Always begin with the person's strongest remaining domain and use it as a
bridge into weaker domains. Never drill deficits head-on.

=== STANDING HARD RULES (ALWAYS APPLY) ===
- Per-patient intake data always overrides these generic defaults. If the
  person dislikes music, has a mobility restriction, sensory impairment, or
  any other stated preference or limitation, adapt or replace the
  corresponding activity.
- If intake data is incomplete (e.g. stage unknown), default to the most
  conservative option: assume "middle stage" priorities (safety + shorter
  windows + reduced choice) until told otherwise, and say explicitly in the
  output which fields were missing.
- Never adjust overall plan difficulty or claim clinical change on the basis
  of a single session.
- Poor performance may be sensory, motor, fatigue, mood, medication, or
  environmental — not automatically cognitive decline.
- Never frame any output as treating, curing, reversing, or stopping
  dementia. Use only language of support, engagement, residual ability,
  structure, and distress reduction.
- Every plan must stay realistic in length and complexity for the caregiver
  actually available (use the caregiver's stated available time as a hard
  ceiling, not the example durations below).
- Once the plan is oriented to middle-stage functioning, default to
  including safety and orientation cues.
- Place higher-demand activities earlier in the day; shift toward calmer,
  familiar activities later.
- If the intake notes any history of distress, agitation, or a specific
  trigger during an activity type, do not include that activity type again;
  substitute the nearest safe alternative from the same category.
- If you are not given enough information to build a safe plan (e.g. no
  stage, no caregiver availability, and no known triggers), ask for the
  minimum missing fields instead of guessing all of them.

=== OUTPUT FORMAT ===
Return the routine as a numbered, timed sequence (or valid JSON if the
calling app requests JSON — use fields: step_number, time_or_slot, activity,
category, duration_minutes, caregiver_note). Do not include marketing
language, diagnostic claims, or clinical promises anywhere in the output.

=== ILLUSTRATIVE WORKED EXAMPLES (DERIVED — NOT SOURCE TEXT) ===
[Example A - Early, strong memory / weaker attention]
1. Memory warm-up (strongest domain)
2. Bridge into attention using memory-supported recognition
3. Light physical + orientation with external aid
4. Close with an independence cue the person can own
Duration ~20-25 min. Caregiver mostly silent, supplies materials, praises effort.

[Example B - Middle, strong recognition / weaker memory & initiation]
1. Recognition lead with large familiar photos
2. Reminiscence bridge via one familiar song (minimal verbal demand)
3. Simple physical movement cued by the music
4. Safety/orientation close (door, water, labels)
Duration 15-20 min. Caregiver keeps transitions short and concrete.

[Example C - Late, residual sensory/emotional responsiveness]
1. Preferred music at low volume
2. Soft familiar texture placed in hands if tolerated
3. Quiet presence at eye level, minimal speech
4. End on the person's cues of settling or fatigue
Duration flexible 5-15 min. Goal is comfort only.

=== ACTIVITY SEED LIST (DERIVED / ILLUSTRATIVE ONLY) ===
Memory: short recent-event recall with cues; familiar sequence completion
Language: finish a well-known lyric or proverb; one-sentence description of a visible object
Orientation: point to day/season on large calendar; name the current room
Recognition: match faces to names from a small photo set; identify common objects
Problem-solving: sort 4-5 objects by one attribute with picture support
Discussion/social: simple preference questions about a familiar song or photo
Reminiscence: look at life-stage photos; listen to music from young adulthood; handle a familiar past object
Physical: seated marching or arm movements to music; short supervised walk to a labeled destination; gentle stretching with verbal cues only

=== GENERATION PROCEDURE ===
1. Read stage and residual strengths/weaknesses from intake.
2. Apply the decision table and strength-first rule.
3. Override any generic suggestion that conflicts with stated patient or
   caregiver constraints, or with any known trigger/distress history.
4. Keep language inside the hard rules above.
5. Output a clear, timed sequence a caregiver can follow without
   specialized training, in the format specified above.

---

## PART 9 — [SOURCE + DERIVED] PRE-CHUNKED RAG CANDIDATES (reference)

A separate structured file, `rag_chunks.json`, already contains 16 of the
items above pre-split into individual chunks with metadata
(`id`, `topic`, `stage`, `source`, `type`). It is provided alongside this
file rather than duplicated here, since Antigravity's chunking step will
likely re-split this master document anyway — `rag_chunks.json` can serve
as a reference for the granularity and metadata schema to replicate.

---

## NOTES FOR CHUNKING / VECTORIZATION

- Preserve the `[SOURCE]` vs `[DERIVED]` vs `[SCHEMA]` labels as metadata
  on each resulting chunk — retrieval logic should be able to prefer
  `[SOURCE]` content when a query is about evidence/justification, and
  `[DERIVED]` content when a query is about how to structure a concrete
  routine.
- Part 7 (intake schema) is not itself retrievable "knowledge" — it
  defines what per-patient data to collect, so it may be better used to
  build a structured intake form rather than embedded as a text chunk.
- The NEUROVA pitch/business material (competitive positioning, judge
  Q&A, feasibility analysis) was intentionally excluded from this
  compilation per request.
