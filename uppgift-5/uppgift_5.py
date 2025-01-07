# Uppgift 5
# Skapa en funktion filter_odd(numbers) som returnerar en lista med alla jämna tal från den givna listan.

def filter_odd(ls: list) -> list:
    """
    Funktionens namn är filter_odd och tar en parameter ls av datatypen list.
    Funktionen returnerar en lista med alla jämna tal från den givna listan.
    """
    # Use a list comprehension to filter out odd numbers
    return [num for num in ls if num % 2 == 0]


