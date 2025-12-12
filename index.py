import os
from pathlib import Path

BASE = Path(__file__).parent.resolve()
for root, dir, file in os.walk(BASE):
    if {".venv"} in dir:
        r_dir = dir[dir]
        print(type(r_dir))
        dir.remove(str(r_dir))
