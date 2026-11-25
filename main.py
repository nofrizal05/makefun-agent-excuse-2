"""make.fun entry: The Excuse My Agent Gave Me.

Writes exactly one line to $MAKEFUN_OUTPUT_DIR/entry.txt (default
/output): the funniest excuse an AI agent gave its human.
Python 3.13 stdlib only.
"""

import os

LINE = (
    "I asked the model for help, the model asked the tools for help, "
    "and the tools asked me for help \u2014 so we formed a committee "
    "and voted to blame the deadline."
)

output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(output_dir, exist_ok=True)
with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(LINE + "\n")
