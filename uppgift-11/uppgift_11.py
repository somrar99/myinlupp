# Uppgift 11
# Skapa en funktion word_count(text) som returnerar antalet ord i en given text.

def word_count(s: str) -> int:
    """
    Funktionens namn är word_count och tar en parameter s av datatypen str.
    Funktionen returnerar antalet ord i en given text.
    """
    # get the number of space in the text
    ret = sum(1 for char in s if char.isspace())

    # if the number of space if zero it means it is an empty string
    if ret > 0:
        ret += 1
    print(ret)
    return ret

word_count("")

