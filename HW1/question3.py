def check_palindrome():
    """Runs through all 6-digit numbers and checks the mentioned conditions.
    The function prints out the numbers that satisfy this condition.
    Notes
    -----
    It should print out the first number (with a palindrome in its last 4 digits),not all four "versions" of it.
    """
    # Your code goes here...
    def polindrom(a):
    s=str(a)
    l=len(s)
    half=l/2
    if (l % 2) == 0: 
        i=0
        while i<half:
            if s[i] != s[len-i]:
                return False


b=1441
print(polindrom(b))
