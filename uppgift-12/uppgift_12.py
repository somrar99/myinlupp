# Uppgift 12
# Skapa en funktion create_student_register(students) som tar emot en lista med namn och ålder och returnerar en dictionary där namnet är nyckeln och åldern är värdet.

def create_student_register(ls: list) -> dict:
    """
    Funktionens namn är create_student_register och tar emot en lista med namn och ålder.
    Funktionen returnerar en dictionary där namnet är nyckeln och åldern är värdet.
    """
    out_dict = {}
    for l in ls:
        out_dict[l[0]] = l[1]
        print("*********")
    return out_dict
