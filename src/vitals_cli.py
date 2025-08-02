"""Simple terminal vitals display for IAM."""
import sys, threading, time

class VitalsDisplay:
    def __init__(self, iam):
        self.iam = iam
        self._stop = threading.Event()
        self._thread = threading.Thread(target=self._loop, daemon=True)

    def start(self):
        self._thread.start()

    def stop(self):
        self._stop.set()
        self._thread.join()
        # move cursor to next line and show again
        sys.stdout.write("\x1b[?25h\n")
        sys.stdout.flush()

    # ------------------------------------------------------------------
    def _bar(self, frac: float, length: int, fill: str, empty: str) -> str:
        filled = int(frac * length)
        return fill * filled + empty * (length - filled)

    def _loop(self):
        sys.stdout.write("\x1b[?25l")  # hide cursor
        while not self._stop.is_set():
            stats = self.iam.stats()
            heart_bar = self._bar(stats['heartScalar'], 10, 'O', ' ')
            lung_bar = self._bar(stats['lung_cap']/100, 10, '#', ' ')
            o2_bar = self._bar(stats['blood_O2']/100, 10, '#', ' ')
            lines = [
                f"\U0001FAC0 Heart  [{heart_bar}]  {int(stats['BPM'])} BPM",
                f"\U0001FAC1 Lungs  [{lung_bar}]  {int(stats['lung_cap'])} %",
                f"O₂ Sat    [{o2_bar}]  {int(stats['blood_O2'])} %",
            ]
            sys.stdout.write('\r' + '\n'.join(lines) + f"\x1b[{len(lines)}A")
            sys.stdout.flush()
            time.sleep(0.5)

