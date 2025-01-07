# Uppgift 10
# Skapa en funktion celsius_to_fahrenheit(celsius) som konverterar en temperatur från Celsius till Fahrenheit.

def celsius_to_fahrenheit(cel: float) -> float:
    """
    Funktionens namn är celsius_to_fahrenheit och tar en parameter cel av datatypen float.
    Funktionen konverterar en temperatur från Celsius till Fahrenheit och returnerar en float.
    """
    return cel * 9 / 5 + 32
