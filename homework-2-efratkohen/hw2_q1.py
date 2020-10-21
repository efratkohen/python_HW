MORSE_CODE = {'A': '.-',     'B': '-...',   'C': '-.-.',
              'D': '-..',    'E': '.',      'F': '..-.',
              'G': '--.',    'H': '....',   'I': '..',
              'J': '.---',   'K': '-.-',    'L': '.-..',
              'M': '--',     'N': '-.',     'O': '---',
              'P': '.--.',   'Q': '--.-',   'R': '.-.',
              'S': '...',    'T': '-',      'U': '..-',
              'V': '...-',   'W': '.--',    'X': '-..-',
              'Y': '-.--',   'Z': '--..',

              '0': '-----',  '1': '.----',  '2': '..---',
              '3': '...--',  '4': '....-',  '5': '.....',
              '6': '-....',  '7': '--...',  '8': '---..',
              '9': '----.',

              '.': '.-.-.-', ',': '--..--', ':': '---...',
              "'": '.----.', '-': '-....-',
              }


def english_to_morse(
    input_file: str = "lorem.txt",
    output_file: str = "lorem_morse.txt"
):
    """Convert an input text file to an output Morse code file.

    Notes
    -----
    This function assumes the existence of a MORSE_CODE dictionary, containing a
    mapping between English letters and their corresponding Morse code.

    Parameters
    ----------
    input_file : str
        Path to file containing the text file to convert.
    output_file : str
        Name of output file containing the translated Morse code. Please don't change
        it since it's also hard-coded in the tests file.
    """
 
    test = open('lorem.txt')
    contents = test.read()
    test.close()
    Upper_str=contents.upper()
    t=Upper_str.maketrans(MORSE_CODE)
    out=Upper_str.translate(t).splitlines()
    L=len(out)
    j=0
    output_file = open("lorem_morse.txt",'w')
    while j<L:
        q=out[j].split()
        if(len(q)==0):
            j=j+1
            continue
        for i in q:
            output_file.write(i)
            output_file.write("\n")
        output_file.write("\n")
        j=j+1
        
    output_file.close()
    de = open('lorem_morse.txt')
    cont = de.read()
    de.close()
    l=len(cont)
    last_file = open("lorem_morse.txt",'w')
    p=0
    while p<l-2:
        last_file.write(cont[p])
        p+=1
    last_file.close()

 
english_to_morse("lorem.txt","lorem_morse.txt")
    

