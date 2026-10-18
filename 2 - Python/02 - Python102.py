#!/bin/python3

#Importing
print("Importing is important")

import sys #system functions and parameters
from datetime import datetime
print(datetime.now())

from datetime import datetime as dt #importing with an alias
print(dt.now())

def new_line():
	print('\n')
new_line()

#Advanced Strings
print("Advanced Strings :")
my_name = "Moha"
print(my_name[0]) #first letter
print(my_name[-1])  #last letter

sentence = "This is a sentence."
print(sentence[:4]) #first word
print(sentence[-9:-1]) #last word
print(sentence[-0])
print(sentence.split()) #split the sentence by deliminer (space)
sentence_split = sentence.split()
sentence_join = ' '.join(sentence_split)
print(sentence_join)
print('\n'.join(sentence_split))

quoteception = "I said give me all the money"
print(quoteception)
quoteception = "I said, \"give me all the money\"  "
print(quoteception)

print("A" in "Apple")
letter = "a"
word = "Apple"
print(letter in word) #False

word_two = "Bingo"
print(letter.lower() in word.lower() and not (letter.lower() in word_two.lower()))

too_much_space = "               hello               "
print(too_much_space.strip())

fullname = "Moha Rahma"
print(fullname.replace("Rahma","Roucha"))
print(fullname.find("Moha")) #Return Position


movie = "The Hangover"
print("My favorite movie is {}".format(movie))

def favorite_book(title,author):
	fav = "My favorite book is \" {}\" , which is written by {}".format(title,author)
	return fav

print(favorite_book("Moucha","Moha"))

new_line()

#Dictionaries
print("Dictionaries are keys and values")

drink = {"White Russians" : 7,
	"Old FAshion" : 10,
	"LEmon Drop" : 8,
	"Buttert Nipple" : 6
 }
print(drink)

employees = {"Finance" : ["Moucha","Bob","Linda"],
"IT" : ["Gene","Zied","Delice"],
"HR": ["Jimmy","Jr","Mort"]
}
print(employees)

employees['Legal'] = ["Mr . Frond"] # add new key

print(employees)

employees.update({"Sales":["Andie","Olive","Olivia"]})

print(employees)

drink["White Russians"] = 8
print(drink.get("White Russians")) #8
print(drink["White Russians"]) #8

# List And Dictionaries
movies = ["When HArry Met Sally","The HAngover","The PErks of Beeign a wallflower","The Exorcist"]
person = ["tut","Jeff","Jeef","Bob"]
combined = zip(movies, person)
movie_dictionary = {key: value for key, value in combined}
print(movie_dictionary)