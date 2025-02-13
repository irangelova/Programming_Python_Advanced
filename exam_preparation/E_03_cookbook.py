def cookbook(*recipes_data):
    recipes_per_cuisine = {}
    for recipe, cuisine, ingredients in recipes_data:
        if cuisine not in recipes_per_cuisine.keys():
            recipes_per_cuisine[cuisine] = []
        recipes_per_cuisine[cuisine].append((recipe, ingredients))

    recipes_per_cuisine_sorted_per_cuisine = dict(sorted(recipes_per_cuisine.items(), key=lambda x: (-len(x[1]), x[0])))

    result = []
    for current_cuisine, current_recipes in recipes_per_cuisine_sorted_per_cuisine.items():
        sorted_recipes = sorted(current_recipes, key=lambda x: x[0])
        result.append(f"{current_cuisine} cuisine contains {len(sorted_recipes)} recipes:")
        for recipe_name, ingredients in sorted_recipes:
            result.append(f"  * {recipe_name} -> Ingredients: {', '.join(ingredients)}")
    return "\n".join(result)


print(cookbook(
    ("Spaghetti Bolognese", "Italian", ["spaghetti", "tomato sauce", "ground beef"]),
    ("Margherita Pizza", "Italian", ["pizza dough", "tomato sauce", "mozzarella"]),
    ("Tiramisu", "Italian", ["ladyfingers", "mascarpone", "coffee"]),
    ("Croissant", "French", ["flour", "butter", "yeast"]),
    ("Ratatouille", "French", ["eggplant", "zucchini", "tomatoes"])
))
print(cookbook(
   ("Pad Thai", "Thai", ["rice noodles", "shrimp", "peanuts", "bean sprouts", "tamarind sauce"])
   ))
print(cookbook(
   ("Spaghetti Bolognese", "Italian", ["spaghetti", "tomato sauce", "ground beef"]),
   ("Margherita Pizza", "Italian", ["pizza dough", "tomato sauce", "mozzarella"]),
   ("Tiramisu", "Italian", ["ladyfingers", "mascarpone", "coffee"]),
   ("Croissant", "French", ["flour", "butter", "yeast"]),
   ("Ratatouille", "French", ["eggplant", "zucchini", "tomatoes"]),
   ("Sushi Rolls", "Japanese", ["rice", "nori", "fish", "vegetables"]),
   ("Miso Soup", "Japanese", ["tofu", "seaweed", "green onions"]),
   ("Guacamole", "Mexican", ["avocado", "tomato", "onion", "lime"])
   ))
