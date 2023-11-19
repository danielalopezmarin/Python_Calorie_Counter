from module.data import meals, combos
from module.exceptions import MealTooBigError

def calorie_counter(*items):
    total = 0
    for item in items:
        if item in meals:
            total += meals [item]
        elif item in combos:
            total += calorie_counter (*combos [item])
        else:
            print (f"{item} not found in the menu")
    if total > 2000:
        raise MealTooBigError(total)
    return total
