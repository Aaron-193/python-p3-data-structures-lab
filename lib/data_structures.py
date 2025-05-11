spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods): 
    names_of_spicy_foods = [food["name"] for food in spicy_foods]
    print(names_of_spicy_foods)
    return names_of_spicy_foods

def get_spiciest_foods(spicy_foods):
    spiciest_foods = list()
    for food in spicy_foods:
        if food["heat_level"] > 5:
            spiciest_foods.append(food)
    return spiciest_foods
        
def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        heat_emojis = "🌶" 
        heat_level = heat_emojis * food["heat_level"]
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {heat_level}")
# print(): Buffalo Wings (American) | Heat Level: 🌶🌶🌶


def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if cuisine == food["cuisine"]:
           return food

def print_spiciest_foods(spicy_foods):
    for food in spicy_foods:
        food_emoji = "🌶"
        heat_level = food_emoji * food["heat_level"]    
        if food["heat_level"] > 5:
            print(f"{food['name']} ({food['cuisine']}) | Heat Level: {heat_level}")
# Buffalo Wings (American) | Heat Level: 🌶🌶🌶
def get_average_heat_level(spicy_foods):
    total_heat = 0
    count = 0
    for food in spicy_foods:
        total_heat += food["heat_level"]
        count += 1
    average = total_heat / count 
    return average  

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods