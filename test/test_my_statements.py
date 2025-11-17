"""Tests for my_statements.py functions."""

from my_statements import dict_function


# write tests for dict_function
def test_dict_function(capsys):
    """Test dict_function to ensure it prints the correct cocktail ingredients."""
    dict_function()
    captured = capsys.readouterr()
    expected_output = (
        "Mojito ingredients:\n"
        "- white rum\n"
        "- sugar\n"
        "- lime juice\n"
        "- soda water\n"
        "- mint\n"
        "\n"
        "Old Fashioned ingredients:\n"
        "- bourbon or rye whiskey\n"
        "- sugar\n"
        "- Angostura bitters\n"
        "- water\n"
        "\n"
        "Margarita ingredients:\n"
        "- tequila\n"
        "- triple sec\n"
        "- lime juice\n"
        "- salt\n"
        "\n"
        "Cosmopolitan ingredients:\n"
        "- vodka\n"
        "- triple sec\n"
        "- cranberry juice\n"
        "- lime juice\n"
        "\n"
    )
    assert captured.out == expected_output
