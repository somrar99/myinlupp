# Uppgift 4
# Skapa en funktion fibonacci(n) som returnerar en lista med de första n Fibonacci-talen.

def fibonacci(n: int) -> list:
    """
    Funktionens namn är is_odd och tar en parameter n av datatypen int.
    Funktionen returnerar en lista med de första n Fibonacci-talen
    """
    # Handle edge cases where n <= 0
    if n <= 0:
        return []
    # Handle the first Fibonacci number
    if n == 1:
        return [0]
    # Handle the first two Fibonacci numbers
    if n == 2:
        return [0, 1]

    # Initialize the sequence with the first two Fibonacci numbers
    sequence = [0, 1]

    # Generate the remaining Fibonacci numbers
    for i in range(2, n):
        next_number = sequence[-1] + sequence[-2]  # Sum of the last two numbers
        sequence.append(next_number)

    return sequence

