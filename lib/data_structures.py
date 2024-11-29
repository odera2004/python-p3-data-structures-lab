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
    """Return a list of names of spicy foods."""
    return [food["name"] for food in spicy_foods]
    pass

def get_spiciest_foods(spicy_foods):
    return [food for food in spicy_foods if food.get("heat_level", 0) > 5]
    pass

def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        # Extract food name, cuisine, and heat level
        name = food.get("name", "Unknown Food")
        cuisine = food.get("cuisine", "Unknown Cuisine")
        heat_level = food.get("heat_level", 0)  # Default to 0 if no heat level is provided
        
        # Print the formatted string
        print(f"{name} ({cuisine}) | Heat Level: {'🌶' * heat_level}")


def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    # Find the first food that matches the specified cuisine
    for food in spicy_foods:
        if food["cuisine"] == cuisine:
            return food
    return None  
def print_spiciest_foods(spicy_foods):
    for food in spicy_foods:
        heat_level = food.get("heat_level", 0)
        
        # Only print foods with a heat level greater than 5
        if heat_level > 5:
            # Print food name, cuisine, and heat level using 🌶 emojis
            print(f"{food['name']} ({food['cuisine']}) | Heat Level: {'🌶' * heat_level}")

    pass

def get_average_heat_level(spicy_foods):
    # Ensure there's at least one food item to avoid division by zero
    if not spicy_foods:
        return 0  # Or return None if you prefer to indicate no data available
    
    # Calculate the total sum of heat levels
    total_heat_level = sum(food.get("heat_level", 0) for food in spicy_foods)
    
    # Calculate the average heat level
    average_heat_level = total_heat_level / len(spicy_foods)
    
    return average_heat_level


def create_spicy_food(spicy_foods, new_food):
    # Add the new spicy food to the list
    spicy_foods.append(new_food)
    
    # Return the updated list
    return spicy_foods
