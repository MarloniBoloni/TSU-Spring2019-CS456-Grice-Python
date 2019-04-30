#open file given filename from user
filename = input("please type in filename >> ")  #Not good enough 
file = open(filename, 'r')
#read in text and print
text = file.read()
print('\n')
print(text)
#using split function, create a list of each word (using white space as a delimiter)
listOfWords = text.split()
print(listOfWords)
nonrepWords = {} #creating a dictionary of non repeating words
#if word in dictionary, increment count, if not, put in dictionary and enter 1 as count
for word in listOfWords:
    if word not in nonrepWords:
        nonrepWords[word] = 1
    else:
        nonrepWords[word] = nonrepWords[word] + 1
file.close() #close the file
print(nonrepWords)
#for every word, 
for word in nonrepWords:
    print(word + ', ', end='')
    print(nonrepWords[word], end='')
    print(', ', end = '')
    print(len(word), end='')
    if word[0].isdecimal():
        print(', ' + "digit", end='\n')
    elif word[0].isalpha():
        print(', ' + "alpha", end='\n')
    else:
        print(', ' + "special", end='\n')
