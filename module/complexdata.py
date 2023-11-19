import json

with open ("module/complexdata/combos.json") as f:
    combos = json.load(f)["combos"]

with open("module/complexdata/meals.json") as f:
    meals = json.load(f)["meals"]

combos = {combo ["id"]: combo for combo in combos}
meals = {meal ["id"]: meal for meal in meals}