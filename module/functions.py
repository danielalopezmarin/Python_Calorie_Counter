from module.complexdata import combos, meals
from module.exceptions import MealTooBigError

combos = {combo ["id"]: combo for combo in combos}
meals = {meal ["id"]: meal for meal in meals}

def calorie_counter(items):
    total = 0
    for item in items:
        if item in meals.keys():
            total += meals [item] ["calories"]
        elif item in combos.keys():
            total += calorie_counter (combos [item]["meals"])
        else:
            print (f"{item} not found in the menu")
    if total > 2000:
        raise MealTooBigError(total)
    return total

def price_counter(items):
    total = 0
    for item in items:
        if item in meals.keys():
            total += meals [item] ["price"]
        elif item in combos.keys():
            total += combos [item] ["price"]
        else:
            print (f"{item} not found in the menu")
    return total