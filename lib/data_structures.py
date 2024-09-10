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
    result = []
    for food in spicy_foods:
        result.append(food['name'])
    return result
 

def get_spiciest_foods(spicy_foods):
    result = []
    for food in spicy_foods:
        if food['heat_level'] > 5:
            result.append(food)
    return result


def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        name = food['name']
        cuisine = food['cuisine']
        # heat_level = food['heat_level']
        heat_emoji = '🌶' * food['heat_level']
        print(f"{name} ({cuisine}) | Heat Level: {heat_emoji}")

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if cuisine == food['cuisine']:
            return food

def print_spiciest_foods(spicy_foods):
    spiciest_foods = get_spiciest_foods(spicy_foods)
    print_spicy_foods(spiciest_foods)

def get_average_heat_level(spicy_foods):
    total_heat = sum(food['heat_level'] for food in spicy_foods)
    total_foods = len(spicy_foods)
    return total_heat / total_foods

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods
