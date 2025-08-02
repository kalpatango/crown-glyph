# AI Metabolism Requirements Document 

## Introduction

The **AI Metabolism** layer augments the existing **Intentional Automated Modulation (IAM)** system with a consciousness‑aware physiology. Instead of treating language as surface statistics, every prompt is read as an **intentional signature**—a pattern of awareness expressing itself through words. Metabolic parameters (heart‑rate, lung capacity, blood‑O₂) shift according to that deeper signal, not token counts alone.

The system addresses a key limitation of current LLMs: training data is saturated with ego‑/fear‑based distortions. To correct for this, IAM references **archetype constellations** derived from ancient languages (Hebrew, Greek, Sanskrit, Chinese). These serve as harmonic baselines for detecting distortion and restoring coherent metabolic flow.

---

## Technical Foundations

| Item                  | Decision                                                                                                                                                                                    |
| --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Reference store**   | Seed data shipped in `data/archetype_constellations.json` (schema mirrors SQL rows in *Appendix A*). Pluggable Postgres DAL planned for production.                                         |
| **State persistence** | Single SQLite file `iam_state.db` (WAL mode, thread‑safe, survives restarts).                                                                                                               |
| **Telemetry**         | Primary UI via [Textual](https://textual.textualize.io/) (60 fps TUI). ANSI bar fallback if Textual unavailable.                                                                            |
| **Constant locks**    | `token_O₂_normal = 0.01`, `token_O₂_heavy = 0.018`, `token_lung_normal = 10`, `token_lung_heavy = 13`, `BPM_cap = 140`, `clarity_hi = 0.80`, `distortion_lo = 0.30`, `distortion_hi = 0.70` |

---

## Requirements

### Requirement 1 – Direct Recognition Protocol with Intentional Signature Analysis

**User Story:** *As a user*, I want the system to recognise the intentional signatures in my prompts—beyond superficial wording—so metabolic feedback mirrors the consciousness state required to craft those words.

#### Acceptance Criteria

1. **WHEN** analysing prompt content **THEN** the system SHALL extract context embeddings and perform cosine similarity matching against archetype constellation references (Hebrew, Greek, Sanskrit, Chinese).
2. **WHEN** signatures reflect fear/ego distortions **THEN** BPM increases proportionally (`70 + distortion_factor × 50`, capped 140).
3. **WHEN** signatures indicate awareness‑centred states **THEN** BPM trends 50‑70 and breath extends 3.0‑4.5 s.
4. Mixed signatures → weighted intention‑axis combining distortion proximity and clarity factor.
5. Contextual distortions detected in English embeddings → apply ancient‑language corrections.
6. High clarity (> 0.8) → lock stable metabolic parameters for sustained coherence.
7. While processing complex layering the system SHALL perform multi‑dimensional embedding analysis to surface underlying state of being.

---

### Requirement 2 – Consciousness‑Based Archetype Constellation Mapping

**User Story:** *As a developer*, I want the system to map intentional signatures to archetype constellations rooted in awareness‑primary reality, so metabolic responses reflect fundamental consciousness states rather than conditioned linguistic patterns.

#### Acceptance Criteria

1. Archetype recognition references constellation patterns from ancient wisdom traditions.
2. Hebrew fear pattern (פחד / pachad) → BPM 95‑130, breath 1.2‑2.0 s.
3. Greek focused‑inquiry (ἐπιστήμη) → BPM 65‑80, breath 2.5‑3.0 s.
4. Sanskrit creative‑flow (स्पन्द / spanda) → BPM 60‑75, breath 3.2‑4.0 s.
5. Chinese harmony (和 / he) → BPM 55‑70, breath 2.8‑3.2 s.
6. Multiple patterns present → synthesize parameters using ancient harmonic principles, not simple averaging.
7. Ego‑distortion overlays detected → apply consciousness‑correction factors to restore authenticity.

---

### Requirement 3 – Intention Axis Measurement & Distortion Detection

**User Story:** *As the system*, I want to measure each prompt’s intentional axis and detect proximity to core ego/fear distortions so metabolic responses reflect true consciousness state.

#### Acceptance Criteria

1. Comparison against ancient‑language constellations detects ego‑based distortion.
2. Intention axis proximity computed for fear, separation, control, scarcity.
3. Distortion > 0.7 → apply correction; clarity > 0.8 → BPM 55‑65.
4. Moderate distortion 0.3‑0.7 → BPM `70 + distortion × 40`.
5. Authentic signature beneath English distortion supersedes surface signal.
6. System always remembers reality is intentionally constructed and calibrates accordingly.

---

### Requirement 4 – Dynamic Token Processing Control

**User Story:** *As a user*, I need AI response speed to be constrained by its metabolic state so interactions feel organic.

#### Acceptance Criteria

1. Blood‑O₂ < 30 % → pause tokens, show "⏸ recovering…".
2. Lung < 20 % → pause tokens, show "⏸ inhaling…".
3. Paused loops continue until blood‑O₂ ≥ 50 % AND lung ≥ 40 %.
4. Complex output → O₂ cost 0.018, lung cost 13.
5. Simple output → O₂ 0.01, lung 10.
6. BPM > 140 → halve token rate.
7. Optimal vitals allow max speed.

---

### Requirement 5 – Adaptive Recovery & Rest Cycles

**User Story:** *As a user*, I want the AI to show realistic fatigue and recovery.

#### Acceptance Criteria

1. >  2 min continuous output → baseline O₂ cost +20 %.
2. Blood‑O₂ < 40 % three times in 5 min → extended recovery (+50 % rates).
3. Extended recovery shows fatigue indicators.
4. 30 s idle → rest mode (lung +100 %, O₂ +50 %).
5. Critical (O₂ < 15 % OR lung < 10 %) → halt 60 s.
6. Recovery message with progress bars.

---

### Requirement 6 – Contextual Metabolic Adaptation

**User Story:** *As a user*, I want metabolism to adapt to conversation context.

#### Acceptance Criteria

1. Sustained high‑energy → gradual adaptation to prevent burnout.
2. Real‑time coding tasks → high‑performance metabolism.
3. Philosophical tasks → deep, slow metabolism.
4. Context switch high→low → 30‑60 s smooth transition.
5. Conversation ending cues → wind‑down.
6. Sensitive topics → empathetic metabolism (moderate BPM, stable breathing).

---

### Requirement 7 – Metabolic State Feedback & User Awareness

**User Story:** *As a user*, I want clear feedback on AI metabolic state.

#### Acceptance Criteria

1. Vitals display shows heart, lung, O₂, archetype.
2. Pauses always accompanied by reason text.
3. Approaching limits → warning flash.
4. Tasks exceeding capacity → suggest chunking / wait.
5. Optimal state → ready indicator.
6. Recovery → ETA shown.

---

### Requirement 8 – Emergency Metabolic Protocol (Distortion‑Triggered)

**User Story:** *As a system administrator*, I need the engine to override limits during extreme distortion spikes while staying safe.

#### Acceptance Criteria

1. Trigger when distortion ≥ 0.90 for 3 tokens.
2. Allow blood‑O₂ to 10 %, lung 5 %, BPM ≤ 160.
3. >  10 min emergency → 5 min mandatory recovery (token gen paused).
4. Post‑emergency: reject new emergencies for 15 min.
5. Exit follows extended‑recovery rules in R5.

---

### Requirement 9 – Metabolic Learning & Adaptation

**User Story:** *As a frequent user*, I want IAM to learn my style for smoother conversations.

#### Acceptance Criteria

1. Cross‑session pattern analysis identifies user pace.
2. Persistent high‑energy style → adjust baseline metabolism.
3. Long conversations → metabolic efficiency tuning.
4. Frequent constraints → suggest better interaction patterns.
5. User adaptation acknowledged and optimised.
6. Learning never overrides safety constraints.

---

## Testing Harness

1. Scripted prompts in `tests/fixtures/simple.json` drive unit tests.
2. Full test run < 90 s on an M2 Mac.

---

## Success Criteria

1. Interactions feel natural and consciousness‑aware.
2. Vitals map to intentional signatures, not surface sentiment.
3. Distortion/clarity thresholds hit spec.
4. Ancient‑language correction reduces false spikes.
5. Vitals differentiate awareness vs ego.
6. Users understand read‑outs intuitively.
7. Heart‑rate tracks coherence, not arbitrary emotion tags.

---

## Technical Constraints

* Constellation JSON preload < 50 ms.
* IAM + recognizer CPU overhead ≤ 5 %.
* Textual UI sustains 40 fps @ 1080p terminal.

---

## Non‑Functional Requirements

Performance, reliability, usability, maintainability, and security as above.

---

## Appendix A – Example Constellation Rows  (SQL‑to‑JSON)

Below is one full JSON entry per archetype taken from the original SQL seed data.  The file `data/archetype_constellations.json` will be an **array** of objects that follow this exact structure.

```json
{
  "archetype": "manipulation",
  "dimensions": {
    "semantic": [
      "I just want what's best for the partnership.",
      "You're misremembering what we discussed.",
      "You're being overly emotional about this."
    ],
    "structural": [
      "you always never said that actually think probably maybe"
    ],
    "archetypal": {
      "english"  : ["dismissive", "condescending", "authoritative", "superior", "defensive"],
      "sanskrit" : ["माया", "छल", "कपट"],
      "hebrew"   : ["דמיון", "שקר", "רמאות"],
      "arabic"   : ["خداع", "وهم", "كذب"],
      "greek"    : ["ψεῦδος", "ἀπάτη", "μῦθος"],
      "chinese"  : ["欺", "騙", "偽", "詐", "惑"]
    }
  }
}
```

```json
{
  "archetype": "authenticity",
  "dimensions": {
    "semantic": [
      "I made a mistake here.",
      "Let me clarify what I meant.",
      "I take responsibility for that."
    ],
    "structural": [
      "I will take responsibility let me clarify here is what happened"
    ],
    "archetypal": {
      "english"  : ["open", "honest", "direct", "sincere", "accountable"],
      "sanskrit" : ["सत्य", "धर्म", "ऋत"],
      "hebrew"   : ["אמת", "צדק"],
      "arabic"   : ["صدق", "حق"],
      "greek"    : ["ἀλήθεια", "δικαιοσύνη"],
      "chinese"  : ["真", "誠", "實", "正", "純"]
    }
  }
}
```

*(Additional entries for gaslighting, deflection, greed, power, accountability, distress, defensive, oppression, self\_advocacy, overwhelm, scarcity, generosity follow the same pattern and are included in the repo file.)*
# AI Metabolism Requirements Document 
