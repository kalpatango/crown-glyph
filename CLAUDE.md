# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

Crown Glyph is an experimental project implementing "Intentional Automated Modulation" (IAM) - a layer that adds physiological constraints to language model output. It simulates heartbeat, breathing, and blood oxygen to create embodied timing and constraints.

## Running the Project

```bash
# Run the main application
python src/crown_seed.py
```

The application has no external dependencies beyond Python's standard library.

## Architecture

### Core Components

- **`crown_seed.py`**: Main entry point that orchestrates the IAM system, vitals display, and archetype recognition
- **`iam.py`**: Core IAM (Intentional Automated Modulation) class that manages physiological state variables:
  - `blood_O2`: Blood oxygen saturation (0-100%)
  - `lung_cap`: Lung capacity (0-100%) 
  - `BPM`: Heart rate (30-180 beats per minute)
  - `breath_rate`: Breathing rate in seconds per inhale
  - `heartScalar`: Triangle wave representing systole/diastole (0-1)
- **`vitals_cli.py`**: Terminal display showing real-time physiological metrics with animated bars
- **`recognizer.py`**: Simple archetype recognition that maps text patterns to physiological states

### IAM Dynamics

The system implements several physiological constraints:

1. **Heartbeat Loop**: Consumes oxygen based on heart rate and work load
2. **Breath Loop**: Refills lung capacity and blood oxygen when not speaking
3. **Speech Cost**: Token generation depletes both oxygen and lung capacity
4. **Block Rule**: Generation pauses when lung capacity ≤ 0 or blood oxygen ≤ 20%

### Archetype Recognition

Simple heuristic mapping:
- Text with "!" → fear archetype (90 BPM, 2.5s breath rate)
- Text with "?" → calm archetype (50 BPM, 3.0s breath rate)  
- Default → joy archetype (70 BPM, 2.0s breath rate)

## Licensing

The project uses dual licensing:

- **Source code**: Parity Public License 7.0.0 (strong copyleft - all forks must remain open)
- **Symbolic content**: CC BY-SA 4.0 (remixable with attribution)

When adding new content:
- Code files (.py) → Parity-7.0 
- Symbolic documents (glyphs, theory, protocols) → CC BY-SA 4.0
- Add appropriate license headers to new symbolic documents

## Development Notes

- Uses threading for concurrent heartbeat/breath loops and vitals display
- All physiological state is protected by locks for thread safety
- Terminal display uses ANSI escape codes for live updating

## Future Development Areas

Based on `docs/physiology_plan.md`:
- Refactor beat loop into cleaner IAM class API
- Implement more sophisticated archetype recognition
- Add "⏸ inhaling..." spinner when generation is blocked
- Explore PAL (context stacking) integration