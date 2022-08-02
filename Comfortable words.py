"""
A comfortable word is a word which you can type always alternating the hand you type with (assuming you type using a QWERTY keyboard and use fingers as shown in the image below).

That being said, complete the function which receives a word and returns true if it's a comfortable word and false otherwise.

The word will always be a string consisting of only ascii letters from a to z.
"""

def comfortable_word(word):
    Left = {'q', 'w', 'e', 'r', 't', 'a', 's', 'd', 'f', 'g', 'z', 'x', 'c', 'v', 'b'}
    Right = {'y', 'u', 'i', 'o', 'p', 'h', 'j', 'k', 'l', 'n', 'm'}
    lista = []
    if word[0] in Left:
        for i in range(len(word)):
            if i%2 != 0:
                if word[i] in Right:
                    lista.append(True)
                else:
                    lista.append(False)
            else:
                if word[i] in Left:
                    lista.append(True)
                else:
                    lista.append(False)

    elif word[0] in Right:
        for i in range(len(word)):
            if i%2 == 0:
                if word[i] in Right:
                    lista.append(True)
                else:
                    lista.append(False)
            else:
                if word[i] in Left:
                    lista.append(True)
                else:
                    lista.append(False)

    return False if False in lista else True
 
print(comfortable_word("peor"))