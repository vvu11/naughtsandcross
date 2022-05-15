#week 5:
#task 1: a program that uses a lookup table to convert any set of alphabets into their correspondng NATO alphabets
#this is the key with the alphabet and their corresponding nato values
nato_alphabet = {'a':'Alfa', 'A': 'Alfa', 'b': 'Bravo', 'B': 'Bravo', 'c': 'Charlie', 'C': 'Charlie', 'd': 'Delta', 'D':'Delta', 'e': 'Echo', 'E':'Echo', 'f': 'Foxtrot', 'F': 'Foxtrot', 'G': 'Golf', 'g': 'Golf', 'h': 'Hotel', 'H': 'Hotel', 'k': 'Kilo', 'K': 'Kilo', 'l': 'Lima', 'L': 'Lima', 'm': 'Mike', 'M': 'Mike', 'n': 'November', 'N': 'November', 'o': 'Oscar', 'O': 'Oscar',
'p': 'Papa', 'P': 'Papa', 'q': 'Quebec', 'Q': 'Quebec', 'r': 'Romeo', 'R': 'Romeo', 's': 'Sierra', 'S': 'Sierra', 't':'Tango', 'T': 'Tango', 'u': 'Uniform', 'U': 'Uniform', 'V': 'Victor', 'v': 'Victor', 'w': 'Whiskey', 'W': 'Whiskey', 'y': 'Yankee', 'Y': 'Yankee', 'Z': 'Zulu', 'z': 'Zulu'}

#passes through the list
def convert(word_to_convert):
    word_converted = []
    for i in word_to_convert: #iterates over the words
        word_converted.append(" ".join(nato_alphabet[ii.lower()] for ii in i)) 
    return word_converted #fetches the nato value from the alphabet and prints converted values


print(convert(['v', 'hello', 'cat']))