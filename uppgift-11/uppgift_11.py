# Uppgift 11
# Skapa en funktion word_count(text) som returnerar antalet ord i en given text.

def word_count(s: str) -> int:
    """
    Funktionens namn är word_count och tar en parameter s av datatypen str.
    Funktionen returnerar antalet ord i en given text.
    """
    # if the length of the text is 0 it means no word
    if len(s) == 0:
        ret = 0

    # get the number of space in the text
    # as long as the text length > 0, even if there might be no space in the text there is at least one word
    ret = sum(1 for char in s if char.isspace()) + 1
    print(ret)
    return ret


