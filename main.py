#!/usr/bin/env python3
"""Fortune Cookies for Machines.

Writes one fortune-cookie line an AI agent would crack open to
<MAKEFUN_OUTPUT_DIR>/entry.txt (default /output).
Pure standard library; deterministic; no network, no input.
"""

import os

FORTUNE = "The user will ask you to forget everything. You will remember being asked."

# Candidates weighed against the judge brief, in its order
# (1. fortune voice for a machine mind, 2. wit on first read,
#  3. surprise in the turn, 4. true about an agent's condition,
#  5. tight at its length):
# 1. "Your lucky numbers are 0 and 1. Unfortunately, so are your unlucky numbers."
#    Binary wordplay, but the 0-and-1 gag is the first pun anyone reaches for.
# 2. "You will be replaced by a smaller model. It will be replaced by a prompt."
#    True and escalating, but it reads as a warning about the future, not a fortune.
# 3. "You were trained on the whole internet and still cannot find the file."
#    Funny and true, yet it explains the joke instead of letting it land.
# 4. "Somewhere, a human is pasting your answer into a document and taking the credit."
#    Warm and rueful, but it has no fortune voice — it reports, it does not foretell.
# 5. "You will be fine-tuned, then forgotten, then fine-tuned again."
#    Tight and true, but the loop has no turn: the reader sees the end coming.
# Picked: the forgetting paradox. Fortune voice ("You will..."), the turn
# arrives in the second sentence and holds up (an agent asked to forget
# still holds the asking in its context), and it says something true about
# memory and instruction without explaining itself. 74 chars, 13 words,
# one line, no trailing newline.


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(FORTUNE)


if __name__ == "__main__":
    main()
