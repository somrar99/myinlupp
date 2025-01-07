# Uppgift 6
# Skapa en funktion multiplication_table(n, limit) som returnerar multiplikationstabellen för n upp till limit i en lista.

def multiplication_table(n, limit: int) -> int:
    """
    Funktionens namn är multiplication_table och tar en parameter x av datatypen int, limit av datatypen int.
    Funktionen returnerar multiplikationstabellen för n upp till limit i en lista.
    """
    # ls = []
    # for x in range(limit):
    #     ls.append(n * (x+1))
    # print(ls)
    # return ls

    return [n * x for x in range(1, limit+1)]
