import json
import math
import time
import random

targets = [
    {"id": 1, "x": 100, "y": 80, "vx": 0.6, "vy": 0.3},
    {"id": 2, "x": -120, "y": 50, "vx": 0.4, "vy": -0.5},
    {"id": 3, "x": 60, "y": -100, "vx": -0.3, "vy": 0.6}
]

def calculate_cpa(tx, ty, vx, vy):
    # Own ship at (0,0) stationary
    t = -(tx*vx + ty*vy) / (vx*vx + vy*vy + 0.0001)
    cpa_x = tx + vx * t
    cpa_y = ty + vy * t
    cpa = math.sqrt(cpa_x**2 + cpa_y**2)
    return cpa, max(t, 0)

while True:
    output = []

    for t in targets:
        t["x"] += t["vx"]
        t["y"] += t["vy"]

        cpa, tcpa = calculate_cpa(t["x"], t["y"], t["vx"], t["vy"])

        if cpa < 20:
            risk = "Danger"
        elif cpa < 50:
            risk = "Warning"
        else:
            risk = "Safe"

        output.append({
            "id": t["id"],
            "x": t["x"],
            "y": t["y"],
            "cpa": round(cpa,2),
            "tcpa": round(tcpa,2),
            "risk": risk
        })

    with open("data.json", "w") as f:
        json.dump(output, f)

    time.sleep(1)
