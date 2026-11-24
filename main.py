"""inv-1125: one-sentence invention pitch, 220-char gate."""

import json
import os

CAPS = {"entry": "entry.txt", "ceiling": 220}


def blueprint(folder):
    with open(os.path.join(folder, CAPS["entry"]), encoding="utf-8") as napkin:
        sketch = napkin.read().strip()
    if not sketch:
        raise SystemExit("the napkin is blank")
    if len(sketch) > CAPS["ceiling"]:
        raise SystemExit("pitch exceeds the napkin: %d chars" % len(sketch))
    return sketch


def patent(folder, sketch):
    vault = os.environ.get("MAKEFUN_OUTPUT_DIR") or folder
    os.makedirs(vault, exist_ok=True)
    shelf = os.path.join(vault, CAPS["entry"])
    with open(shelf, "w", encoding="utf-8", newline="\n") as clerk:
        clerk.write(sketch + "\n")
    return shelf


desk = os.path.dirname(os.path.abspath(__file__))
sketch = blueprint(desk)
print(json.dumps({"gizmo": sketch[:46], "sketch_chars": len(sketch), "patent_pending": "obviously", "shelf": patent(desk, sketch)}))
