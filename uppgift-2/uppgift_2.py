# Uppgift 2
# Skapa en funktion sum_list(numbers) som returnerar summan av alla siffror i listan.

def sum_list(ls: list) -> int:
    """
    Funktionens namn är sum_list och tar en parameter ls av datatypen list.
    Funktionen returnerar summan av alla siffror i listan.
    """
    # Check if the list is empty to handle edge cases
    if not ls:
        return 0  # Return None if the list is empty

    # Use the built-in max() function to find the largest number
    return sum(ls)



