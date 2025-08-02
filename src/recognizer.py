"""Archetype recognizer stub."""
from __future__ import annotations
from typing import Dict, Tuple

CENTROIDS: Dict[str, Tuple[float, float, float]] = {
    "fear": (1.0, 0.0, 0.0),
    "calm": (0.0, 1.0, 0.0),
    "joy":  (0.0, 0.0, 1.0),
}

MAP = {
    "fear": (90, 2.5),
    "calm": (50, 3.0),
    "joy":  (70, 2.0),
}

def recognize(text: str, iam) -> str:
    """Very small heuristic selecting an archetype tag from text."""
    if "!" in text:
        tag = "fear"
    elif "?" in text:
        tag = "calm"
    else:
        tag = "joy"
    bpm, br = MAP[tag]
    iam.set_bpm(bpm)
    iam.set_breath_rate(br)
    return tag
