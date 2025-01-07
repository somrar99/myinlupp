# Uppgift 8
# Skapa en funktion count_letters(string) som returnerar en dictionary med varje bokstav som nyckel och antalet förekomster som värde.

def count_letters(s: str) -> dict:
    """
    Funktionens namn är count_letters och tar en parameter s av datatypen str.
    Funktionen returnerar en dictionary med varje bokstav som nyckel och antalet förekomster som värde.
    """
    out_dict = {}
    for char in s:
        out_dict[char] = out_dict.get(char, 0) + 1
    # print(out_dict)
    return out_dict

