"""Intentional Automated Modulation (IAM) runtime."""
from __future__ import annotations
import threading, time
from typing import Dict

class IAM:
    BASELINE_O2 = 0.01

    def __init__(self):
        self.blood_O2 = 100.0
        self.lung_cap = 100.0
        self.BPM = 70
        self.breath_rate = 2.0
        self.heartScalar = 0.0
        self._stop = threading.Event()
        self._lock = threading.Lock()
        self._threads = []
        self._speaking_until = 0.0

    # --- control -------------------------------------------------------
    def start(self) -> None:
        self._stop.clear()
        self._threads = [
            threading.Thread(target=self._heartbeat_loop, daemon=True),
            threading.Thread(target=self._breath_loop, daemon=True),
        ]
        for t in self._threads:
            t.start()

    def stop(self) -> None:
        self._stop.set()
        for t in self._threads:
            t.join()

    # --- public API ----------------------------------------------------
    def on_token(self, token: str) -> None:
        """Account for metabolic cost of producing one token."""
        with self._lock:
            self.blood_O2 = max(0.0, self.blood_O2 - 0.01)
            self.lung_cap = max(0.0, self.lung_cap - 10.0)
            self._speaking_until = time.time() + 0.5

    def stats(self) -> Dict[str, float]:
        with self._lock:
            return {
                "blood_O2": self.blood_O2,
                "lung_cap": self.lung_cap,
                "BPM": self.BPM,
                "breath_rate": self.breath_rate,
                "heartScalar": self.heartScalar,
            }

    def set_bpm(self, bpm: int) -> None:
        with self._lock:
            self.BPM = bpm

    def set_breath_rate(self, rate: float) -> None:
        with self._lock:
            self.breath_rate = rate

    # --- loops ---------------------------------------------------------
    def _heartbeat_loop(self) -> None:
        last = time.time()
        while not self._stop.is_set():
            with self._lock:
                beat_interval = 60.0 / max(1, self.BPM)
            now = time.time()
            phase = (now - last) / beat_interval
            if phase >= 1.0:
                # beat
                last = now
                self.heartScalar = 1.0
                with self._lock:
                    work = self.heartScalar * self.BASELINE_O2 * 2 if self.heartScalar > 0.3 else 0
                    self.blood_O2 = max(0.0, self.blood_O2 - (self.BASELINE_O2 + work))
            else:
                # triangular wave 0->1->0
                self.heartScalar = phase * 2 if phase < 0.5 else (1 - phase) * 2
            time.sleep(beat_interval / 10)

    def _breath_loop(self) -> None:
        while not self._stop.is_set():
            speaking = time.time() < self._speaking_until
            if not speaking:
                with self._lock:
                    # ease-out toward 70%
                    target = 70.0
                    self.lung_cap += (target - self.lung_cap) * 0.1
                    delta = (target - self.lung_cap) * 0.1
                    self.blood_O2 = min(100.0, self.blood_O2 + delta)
            time.sleep(self.breath_rate / 10)
