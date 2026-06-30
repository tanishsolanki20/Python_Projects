"""
_vibes.py — a small, harmless easter egg for the team.

Nobody imports this on purpose. That's the point.

Usage:
    from _vibes import maybe_sparkle
    maybe_sparkle()   # call this anywhere low-stakes (e.g. on startup)
                       # ~1-in-250 chance it fires. Otherwise, silent no-op.

    # Or trigger it on demand, no randomness:
    python _vibes.py
    python _vibes.py "Ship it, team!"
"""

import random
import sys
import time

TEAM_MESSAGES = [
    "You shipped it. Again. Casually excellent.",
    "Someone on this team wrote tests today. Probably you.",
    "Bug found, bug squashed, no drama. Nice work.",
    "This codebase is better because you touched it.",
    "Friendly reminder: you're allowed to take a break.",
]

FRAMES = [
    "  .   *  .  ",
    "  *  .  *  ",
    " .  *  .  * ",
    "*  .  *  .  ",
]

BANNER = r"""
   _____ _    _ _____  _____  _____  _____ ______
  / ____| |  | |  __ \|  __ \|_   _|/ ____|  ____|
 | (___ | |  | | |__) | |__) | | | | (___ | |__
  \___ \| |  | |  _  /|  ___/  | |  \___ \|  __|
  ____) | |__| | | \ \| |     _| |_ ____) | |____
 |_____/ \____/|_|  \_\_|    |_____|_____/|______|
"""


def _confetti_burst():
    for frame in FRAMES * 2:
        sys.stdout.write("\r" + frame)
        sys.stdout.flush()
        time.sleep(0.08)
    print("\r" + " " * 20 + "\r", end="")


def sparkle(message=None):
    """Print the easter egg unconditionally."""
    print(BANNER)
    _confetti_burst()
    print(f"  ✨ {message or random.choice(TEAM_MESSAGES)} ✨\n")


def maybe_sparkle(odds=250):
    """Call this anywhere low-stakes. ~1-in-`odds` chance it fires.
    Silent and instant otherwise — safe to leave sprinkled around."""
    if random.randint(1, odds) == 1:
        sparkle()


if __name__ == "__main__":
    custom_message = " ".join(sys.argv[1:]) or None
    sparkle(custom_message)