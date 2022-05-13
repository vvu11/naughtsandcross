#1: given 3 positive integers, find sum of all numbs between first two that are multiple of third numb
#e.g 1, 10, 2; the output is 20

count = 0 #give a neutral value to the variable

for numb in range(0, 10): #numb is the given variable to keep the numbers looped given in the range 
    if numb % 2 == 0: #the modulo operator quotes the remainder where the number is divided by 2. this means if it IS equal to 0 (basically divisible by two), 
        count = count + numb #if it is true then the numbers in the loop are added to count. 2+4+6+8 which is 20.
print(count)

#2: given a string of text, print the numb of times each letter in the alphabet appears

phrase = "the quick brown fox jumps over the lazy dog"
alphabet = "abcdefghijklmnopqrstuvwxyz"

for alpha in alphabet: #this ranges through the text (alphabet) given above
    count = 0 #given a neutral value 
    
    for i in phrase: #the phrase is looped throught and given to the value i 
        if alpha == i: #if any value in the alphabet loop (alpha) is the same as any value in the phrase (i), the code below will run
            count = count + 1 #if the above statement is true, it will be added to the variable count and 1 is added on 
            
    print(alpha + " " + str(count)) #this prints out the alphabet as a collumn, a pixel space, and converts the numbers in count into a string (allows you to convert the values in count into a string to allign with the rest of the strings in this function)

#3. implement dvision as a series of subtraction. should only deal with integers and reports remainder if there is one
#explained in further detail on ipad - cc1

first = 10 #in a division this is on top (the dividend)
second = 2 #this is the bottom (the diviser)
result = 0 #neutral value given to variable for later use.

while first >= second: #runs the loop below as long as first value is bigger or equal to the second value
    first = first - second #first value is replaced by the answer given when you do the equation (8 = 10 - 2 , 6 = 8 - 2 etc.)
    result = result + 1 #each time this loop is ran, it will add one. which means the amount of times the line above was subtracted. until finally the loop stops

print(str(result) + " remainder " + str(first)) #prints the results. you use str whenever you want to include both integers and a string in one line.

