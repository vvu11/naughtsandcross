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

#task2:  a caesar cipher function which takes a string + shift amount, ouputs the encrypted string

text = input(str("Please type your text in all caps: ")) #defining the text
shift = 7 #defining the shift

output = " "

for c in text:
    if c.isupper():
        
        #finds the position in 0-25
        c_unicode = ord(c)
        c_index = ord(c) - ord("A")

        #performs the shift
        new_index = (c_index + shift) % 26 

        #converts to the new character
        new_unicode = new_index + ord("A")

        new_character = chr(new_unicode)

        #appends to ouput string
        output = output + new_character

    else:

        output += c 

print ("Original Text: " , text)

print ("New Text: " , output)