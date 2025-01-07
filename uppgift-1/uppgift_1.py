# Uppgift 1
# Skapa en funktion is_odd(x) som returnerar True om x är udda och False om x är jämnt.
# def funktions_namn(variabel_namn: datatyp) -> returtyp:
# Exempel: def is_odd(x: int) -> bool:
# Förklaring: Funktionens namn är is_odd och tar en parameter x av datatypen int. Funktionen returnerar en bool.

def is_odd(num: int) -> bool:
    """
    Funktionens namn är is_odd och tar en parameter num av datatypen int.
    Funktionen returnerar en bool.
    """
    # Check if the number is odd
    return num % 2 == 1
