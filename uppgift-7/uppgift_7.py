# Uppgift 7
# Skapa en funktion validate_password(password) som kontrollerar att lösenordet är minst 8 tecken långt och innehåller minst en siffra.

def validate_password(s: str) -> bool:
    """
    Funktionens namn är validate_password och tar en parameter s av datatypen string.
    Funktionen kontrollerar att s är minst 8 tecken långt och innehåller minst en siffra
    Funktionen returnerar en bool.
    """
    ret = len(s) >= 8 and any(char.isdigit() for char in s)
    # print(ret)
    return ret
