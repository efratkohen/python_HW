def trifeca(word):
    """Checks whether word contains three consecutive double-letter pairs.
    Parameters
    ----------
    word : string
        Input to check
    Returns
    -------
    result : bool
        True if three consecutive double-letter pairs were found,
        False otherwise
    """
    # Your code goes here...
    if(type(word)!=str):
        print(word,"is not a string")
        return False
    l=len(word)
    if l<6:
        return False
    i=1
    while i+4<l:
        if (word[i-1:i]==word[i:i+1] and word[i+1:i+2]==word[i+2:i+3] and word[i+3:i+4]==word[i+4:i+5]):
            return True
        else:
            i+=1
    return False

print(trifeca(34))


