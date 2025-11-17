"""This module contains functions demonstrating different data structures."""


def dict_function():
    """sample function using a dictionary to store cocktail ingredients"""
    my_dict = {
        "Mojito": ["white rum", "sugar", "lime juice", "soda water", "mint"],
        "Old Fashioned": [
            "bourbon or rye whiskey",
            "sugar",
            "Angostura bitters",
            "water",
        ],
        "Margarita": ["tequila", "triple sec", "lime juice", "salt"],
        "Cosmopolitan": ["vodka", "triple sec", "cranberry juice", "lime juice"],
    }

    for cocktail, ingredients in my_dict.items():
        print(f"{cocktail} ingredients:")
        for ingredient in ingredients:
            print(f"- {ingredient}")
        print()  # Print a newline for better readability]
