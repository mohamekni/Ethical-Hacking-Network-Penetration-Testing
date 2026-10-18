#! /bin/python3

#print string
print("Strings")
print('Hello,world!')
print(""" Hello, this
is multi-line! """)
print("This is "+"a String")

print('\n') # New Line

#Math
print("Math Time:")
print(50 + 50) # add
print(50 - 50) # subtract
print(50 * 50) # multiply
print(50 / 50) # divide
print(50 + 50 - 50 * 50 / 50) # PEMDAS
print(50 ** 2) #exponents
print(50 % 6) #modulo
print(50 // 6) # number without leftovers

print('\n') # New Line

#Variables & Methods
print ("Fun with variables and methods :")
quote = 'All is fair in love and war'
print(len(quote)) #length
print(quote.upper()) #uppercase
print(quote.lower()) #lowercase
print(quote.title()) #title

name = "Moha"
age = 25 #int type
gpa = 3.7 #float type

print(int(age))
print(int(29.9)) #does not round

print("My name is " + name + "and i am " + str(age) + " Years old.")

print('\n') # New Line

age += 1
print(age)

birthday = 1
age += birthday

print(age)

print('\n') # New Line

#Functions
print("Now, some functions")
def who_am_i():
	name = "Moha"
	age = 25
	print("My name is " + name + "and i am " + str(age) + " Years old.")

who_am_i()

#adding in parameters
def add_one_hundred(num):
	print(num + 100)
	
add_one_hundred(100)

#add in multiple parameters
def add(x,y):
	print(x + y)

add(7,7)
add(305,207.03)

#using return
def multiple(x,y):
	return x * y
print(multiple(7,7))

def square_root(x):
	return x ** 5

print(square_root(64))

print('\n') # New Line

#Boolean expressions (True or False)

print("Boolean Experessions :")
bool1 = True
bool2 = 3*3 == 9
bool3 = False
bool4 = 3*3 != 9

print(bool1,bool2,bool3,bool4)
print(type(bool1))

bool5 = "True"
print(type(bool5)) # String

# Relational and boolean Operators
greater_than = 7 > 5
less_than = 7 < 5
greater_than_equal_to = 7 >= 1
less_than_equal_to = 7 <= 7

print(greater_than,less_than,greater_than_equal_to,less_than_equal_to)

test_and = (7 > 5) and (5 < 7) # both is true
test_or = (7 > 5) or (5 < 7)
test_not = not True

print(test_and,test_or,test_not)

#Conditional Statements
print("Conditional Statements")
def soda(money):
	if money >= 2 :
		return "You've got yourself a soda"
	else:
		return "No Soda for you ! "
		
print(soda(4))
print(soda(2))

def laptop(age,money):
	if(age>=21) and (money>=2000):
		return "Congrat"
	elif (age>=21) and (money < 2000):
		return "Come back with more money"
	elif(age<21) and (money >= 2000):
		return "Nice try, kids"
		
print(laptop(22,1500))
print(laptop(19,2100))
print(laptop(22,2000))

print('\n') # New Line

#Lists
print("Lists have brackets:")

movies = ["when harry met sally", "The hangover", "The Perks of Being a Wallflower", "The Exorcist"]

print(movies[0])
print(movies[1:3])
print(movies[1:])
print(movies[:1])
print(movies[-1])
print(len(movies))
movies.append("JAWS")
print(movies)
movies.pop()
print(movies)

movies.pop(1)
print(movies)

movies = ["when harry met sally", "The hangover", "The Perks of Being a Wallflower", "The Exorcist"]
person = ["Heath","Jake","Jeff"]
combined = zip(movies,person)
print(list(combined))

#Tuples
print("Tuples have parentheses and cannot change")
grades = ("A","B","C","D","F")
print(grades[1])

#Looping
print("For loops - start to finish of iterate:")
vegetables = ["cucumber","spinach","cabbage"]
for x in vegetables:
	print(x)

print("while loop Execute as long as True")
i = 1
while i < 10 :
	print(i)
	i +=1
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	



