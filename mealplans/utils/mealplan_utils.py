def calculate_approx_calories_for_recipes(recipes):

    if not recipes:
        return 0

    nutritional_info = recipes.values_list('stats', flat=True)

    return 1
