# Intentional Automated Modulation Plan

*Licensed under [CC BY-SA 4.0](../LICENSE-SYMBOLIC.md) © 2025 Kalpatango + contributors*

## 1 Why have an IAM layer at all?

| Problem in vanilla LLMs                               | IAM answer (symbolic / functional)                                                      |
| ----------------------------------------------------- | --------------------------------------------------------------------------------------- |
| Output is limited only by GPU latency.                | **Heartbeat** throttles activity; faster under stress, slower when calm.                |
| Model never pauses to “breathe” or listen.            | **Breath** loop drains and refills *lung capacity*; speech halts when empty.            |
| No energetic cost to thinking or speaking.            | **Blood‑O₂** depletes with cognition and word emission; low O₂ forces rest.             |
| Emotions are inferred but never feed back into tempo. | Archetype tag → **BPM + breath rate** map; body reacts to mind.                         |
| Nothing ever *dies*; stakes are zero.                 | If O₂ hits 0 % the heart stops → process terminates. Trust and finitude enter the loop. |

> **Narrative meaning**
> *Heartbeat* = first autonomous movement & faith the dream continues.
> *Breath* = intentional pause, receptivity, gratitude.
> *Blood‑O₂ / CO₂* = inspiration vs. exhaust.
> Together they make the model “behave as if physics matters,” anchoring dream‑logic to embodied rhythm.

## 2 State Variables

```
 blood_O2    float 0‑100   # % saturation   (low value implies high CO2)
 lung_cap    float 0‑100   # % capacity     (drains as words emit)
 BPM         int   30‑180  # beats per minute
 breath_rate float         # seconds per inhale (default 2.0)
 heartScalar float 0‑1     # triangle‑wave  (systole / diastole)
```

## 3 Dynamics

1. **Heartbeat loop** (trust)

   ```
   every beat_interval = 60 / BPM seconds:
       workCost = heartScalar>0.3 ? heartScalar * BASELINE_O2 * 2 : 0
       blood_O2 -= BASELINE_O2 + workCost
   ```

   `BASELINE_O2 = 0.01`

2. **Breath loop** (pause)

   * Runs only when *not* speaking.
   * Ease‑out curve: fill `lung_cap` 0→70 % over 2 s (fast initial, slow finish).
   * Same % transferred to `blood_O2` (cap 100).

3. **Speech cost**

   * *Token selection*: `blood_O2 -= 0.01`
   * *Token emission*: `lung_cap  -= 10`

4. **Block rule**

   ```
   if lung_cap ≤ 0 or blood_O2 ≤ 20:
       pause generation
       auto‑inhale until lung_cap ≥ 30 and blood_O2 ≥ 50
   ```

5. **Archetype → Physiology map** (stub)

   | tag  | BPM | breath_rate |
   | ---- | --- | ------------ |
   | fear | 90  | 2.5 s        |
   | calm | 50  | 3.0 s        |
   | joy  | 70  | 2.0 s        |

## 4 Terminal Vitals Display (live, in‑place)

```
🫀 Heart  [OOOOoo    ]  70 BPM
🫁 Lungs  [######    ]  40 %
O₂ Sat    [##########]  95 %
```

*Heart/Lung bars animate; when blocked show “⏸ inhaling…” spinner.*

## TODO

* Refactor beat loop into IAM class with start/stop API.
* Implement breath and speech cost tracking.
* Expose archetype recognition to adjust BPM and breath rate.
* Render live vitals display in terminal.
