
import json

with open('Fooddata.json', 'r') as file:
    fooddata = json.load(file)
foods = fooddata["FoundationFoods"]

poss_units = {}
for food in foods:
    for nutrient in food["foodNutrients"]:
        unit = nutrient["nutrient"]["unitName"]
        name = nutrient["nutrient"]["name"]
        if name == "Protein" or "Total lipid (fat)" or "Carbohydrate, by difference" or "Fiber, total dietary" or "Sodium, Na":
            if unit not in poss_units:
                poss_units[name] = unit

print(poss_units["Protein"])
print(poss_units["Total lipid (fat)"])
print(poss_units["Carbohydrate, by difference"])
print(poss_units["Fiber, total dietary"])
print(poss_units["Sodium, Na"])
print(poss_units["Energy"])
