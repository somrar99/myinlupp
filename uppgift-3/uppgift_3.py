# Uppgift 3
# Hitta det största talet i en lista

def max_in_list(ls: list) -> int:
    """
    Funktionens namn är max_in_list och tar en parameter ls av datatypen list.
    Funktionen returnerar det största talet i en lista.
    """
    # Check if the list is empty to handle edge cases
    if not ls:
        return None  # Return None if the list is empty

    # Use the built-in max() function to find the largest number
    return max(ls)

