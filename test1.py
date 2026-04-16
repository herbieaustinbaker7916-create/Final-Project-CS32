"""
function that gets all nutrient information and returns those values
"""

input = "Yogurt, Greek, plain, nonfat"
#input = "Pears, raw, bartlett"
result = {}
import json

with open('Fooddata.json', 'r') as file:
        fooddata = json.load(file)
foods = fooddata["FoundationFoods"]
for food in foods:
    if food["description"] == input:

        for nutrient in food["foodNutrients"]:
            name = nutrient["nutrient"]["name"]
            amount = nutrient.get("amount", 0)
            unit = nutrient["nutrient"]["unitName"]

            if name == "Protein":
                result["protein"] = amount
            elif name == "Total lipid (fat)":
                result["fat"] = amount
            elif name == "Carbohydrate, by difference":
                result["carbs"] = amount
            elif name == "Fiber, total dietary":
                result["fiber"] = amount
            elif name == "Sodium, Na":
                result["sodium"] = amount
            elif name == "Energy" and unit == "kcal":
                result["energy"] = amount
            #elif name == "Energy" and unit == "kJ":
                #result["energy"] = amount

        for amount in food["foodPortions"]:
            quant = amount["gramWeight"]




final_value = {}
def calc(amount,quant):
    normalised = (100*amount)/quant
    return (normalised)
for item in result:
    final = calc(result[item],quant)
    final_value[item] = final
print(final_value)
