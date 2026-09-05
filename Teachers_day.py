"""
Happy Teacher's Day - Colorful Terminal Greeting
--------------------------------------------------
No external libraries needed. Uses ANSI escape codes for color
and box-drawing characters for a decorative card look in the terminal.
"""

import shutil
import time

# ---------------- Settings ----------------
TEACHER_NAME = "Ma'am"          # <-- change to your teacher's name
STUDENT_NAME = "Your Student"   # <-- change to your name

# ---------------- ANSI colors ----------------
RESET = "\033[0m"
BOLD = "\033[1m"
ITALIC = "\033[3m"

GOLD = "\033[38;5;220m"
PINK = "\033[38;5;211m"
PEACH = "\033[38;5;216m"
CREAM = "\033[38;5;230m"
MAROON = "\033[38;5;131m"
GREEN = "\033[38;5;108m"


def center(text, width, color=""):
    pad = max(0, (width - len(strip_len(text))) // 2)
    return " " * pad + color + text + RESET


def strip_len(text):
    """Return visible length ignoring nothing extra (kept simple, no ANSI in text)."""
    return text


def wrap_text(text, width):
    words = text.split()
    lines, current = [], ""
    for word in words:
        trial = (current + " " + word).strip()
        if len(trial) <= width:
            current = trial
        else:
            lines.append(current)
            current = word
    if current:
        lines.append(current)
    return lines


def draw_card():
    term_width = shutil.get_terminal_size((80, 24)).columns
    card_width = min(70, term_width - 4)

    top_border = GOLD + "╔" + "═" * (card_width - 2) + "╗" + RESET
    bottom_border = GOLD + "╚" + "═" * (card_width - 2) + "╝" + RESET
    side = GOLD + "║" + RESET

    def blank_line():
        print(side + " " * (card_width - 2) + side)

    def text_line(text, color=CREAM, style=""):
        inner_width = card_width - 4
        pad_total = inner_width - len(text)
        pad_left = pad_total // 2
        pad_right = pad_total - pad_left
        print(
            side + " " + " " * pad_left + style + color + text + RESET
            + " " * pad_right + " " + side
        )

    flowers = "✿ ❀ ✿ ❀ ✿"
    stars = "★ · · ✦ · · ★"

    print()
    print(" " * ((term_width - card_width) // 2), end="")
    print(top_border)

    for _ in range(2):
        blank_line()

    text_line(stars, GOLD)
    blank_line()
    text_line("HAPPY TEACHER'S DAY", PINK, BOLD)
    blank_line()
    text_line(flowers, PEACH)
    blank_line()
    text_line(f"Dear {TEACHER_NAME},", MAROON, ITALIC)
    blank_line()

    message = (
        "Thank you for your endless patience, wisdom, and "
        "kindness. You don't just teach lessons from Claude "
        "you inspire us to think, to grow, and to believe "
        "in ourselves. To us, you are more than a teacher "
        "you are a guide and a mentor for life."
    )
    for line in wrap_text(message, card_width - 6):
        text_line(line, CREAM)

    blank_line()
    text_line(flowers, PEACH)
    blank_line()
    text_line("With gratitude and respect,", MAROON, ITALIC)
    text_line(STUDENT_NAME, GREEN, BOLD)
    blank_line()
    blank_line()

    print(" " * ((term_width - card_width) // 2), end="")
    print(bottom_border)
    print()


if __name__ == "__main__":
    draw_card()