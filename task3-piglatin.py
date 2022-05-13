# a function which takes two arguments, (the second of which is optional) and prints a greeting according to which is provided

question = input("Will you be providing a surname? ") #asks user to input an answer which is answere with either yes or no

if question == "yes": #calls an if function - if the answer to the question is yes:
    name = input("What is your name? ") #this will run

    surname = input("What is your surname? ")
    print("Hello, " + name + " from the house of " + surname + "!")
else: 
    name = input("What is your name? ") #if answer is no this code will run instead 
    print("Hi, " + name)


#write a sanction that takes any english word/sentence and turns it into pig latin

def pig_latin(text):
    words = text.split() #this splits the string(text) into a list and adds it to words
    pigg = [] #defines pigg to be used later

    for word in words: #this will iterate through the code below as many times as the given words in the string
        word = word[1:] + word[0] + 'ay' #takes all chars after the first, + the first (because they run at 0 index. 0=1.) + "ay"
        pigg.append(word) #.append adds an element to the list. here 

    return ','.join(pigg) #.join joins all the items in the dictionary (words) into a string (pigg). the ',' is the seperator

print(pig_latin("Hello how are you"))

