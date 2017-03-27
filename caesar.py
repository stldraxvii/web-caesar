import string
alphabet = {'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7,'i':8,
'j':9,'k':10,'l':11,'m':12,'n':13,'o':14,'p':15,'q':16,'r':17,
's':18,'t':19,'u':20,'v':21,'w':22,'x':23,'y':24,'z':25}
alphalist = list(alphabet.keys())
alphalist.sort()

def alphabet_position(letter):
    letter = letter.lower()
    return alphabet[letter]


def rotate_character(char, rot):
    rot = rot % 26
    if char in string.ascii_letters:
        start = alphabet_position(char)
        end = start + rot
        end = end % 26
        if char in string.ascii_uppercase:
            char = alphalist[end]
            char = char.upper()
        else:
            char = alphalist[end]
    return char


def encrypt(text,rot):
    newtext = ''
    for i in text:
        x = rotate_character(i,rot)
        newtext = newtext + x
    return newtext
