# Uppgift 9
# Skapa en funktion is_palindrome(string) som kontrollerar om en given sträng är ett palindrom (dvs. samma framifrån och bakifrån).

def is_palindrome(s: str) -> bool:
    """
    Funktionens namn är is_palindrome och tar en parameter s av datatypen str.
    Funktionen kontrollerar om en given sträng är ett palindrom (dvs. samma framifrån och bakifrån) och returnerar en bool.
    """
    # ret = True
    # for x in range(int(len(s)/2)):
    #     if s[x] != s[len(s)-1-x]:
    #         ret = False
    #         break
    # return ret

    # Remove spaces and convert to lowercase for uniformity
    cleaned_string = s.replace(" ", "").lower()

    # Check if the cleaned string is equal to its reverse
    return cleaned_string == cleaned_string[::-1]

