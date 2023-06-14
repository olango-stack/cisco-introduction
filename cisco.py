print("The itsy bitsy spider" , "climbed up" , "the waterspout.")#single line
print("My name is", "Python.")
print("Monty Python.")

print("My name is", "Python.", end=" ")
print("Monty Python.")

print("My name is ", end="")
print("Monty Python.")

print("My", "name", "is", "Monty", "Python.", sep="-")

print("My", "name", "is", sep="_", end="*")
print("Monty", "Python.", sep="*", end="*\n")

print("Programming","Essentials","in", sep="***", end="...")
print("Python")

print("2")#string
print(2)#integer

print(0o123)#octal zero-o
print(0x123)#hexadecimal-zero-x

print("I like \"Monty Python\"")
print('I like "Monty Python"')
print('I\'m Monty Python.')#embedding apostrophe within string

print(True > False)
print(True < False)

print("\"I'm\"")
print('""learning""')
print('"""Python"""')

var = 1
account_balance = 1000.0
client_name = 'John Doe'
print(var, account_balance, client_name)
print(var)

var = "3.7.1"
print("Python version: " + var)

a = 3.0
b = 4.0
c = (a ** 2 + b ** 2) ** 0.5
print("c =", c)

anything = float(input("Enter a number: "))
something = anything ** 2.0
print(anything, "to the power of 2 is", something)

leg_a = float(input("Input first leg length: "))
leg_b = float(input("Input second leg length: "))
hypo = (leg_a**2 + leg_b**2) ** .5
print("Hypotenuse length is", hypo)
#or
leg_a = float(input("Input first leg length: "))
leg_b = float(input("Input second leg length: "))
print("Hypotenuse length is", (leg_a**2 + leg_b**2) ** .5)
#concatenation
fnam = input("May I have your first name, please? ")
lnam = input("May I have your last name, please? ")
print("Thank you.")
print("\nYour name is " + fnam + " " + lnam + ".")
#replication operator *
"James" * 3 #gives "JamesJamesJames"
3 * "an" #gives "ananan"
5 * "2"

#rectangle 
print("+" + 10 * "-" + "+")
print(("|" + " " * 10 + "|\n") * 5, end="")
print("+" + 10 * "-" + "+")

leg_a = float(input("Input first leg length: "))
leg_b = float(input("Input second leg length: "))
print("Hypotenuse length is " + str((leg_a**2 + leg_b**2) ** .5))
#prompt user to end program
name = input("Enter your name: ")
print("Hello, " + name + ". Nice to meet you!")

print("\nPress Enter to end the program.")
input()
print("THE END.")

var = 0 # assigning 0 to var
print(var == 0)

var = 1 # assigning 1 to var
print(var == 0)

var = 0 # assigning 0 to var
print(var != 0)

var = 1 # assigning 1 to var
print(var != 0)
answer = number_of_lions >= number_of_lionesses#store in a variable

#if statement
if the_weather_is_good:
    if nice_restaurant_is_found:
        have_lunch()
    else:
        eat_a_sandwich()
else:
    if tickets_are_available:
        go_to_the_theater()
    else:
        go_shopping()
#elif
if the_weather_is_good:
    go_for_a_walk()
elif tickets_are_available:
    go_to_the_theater()
elif table_is_available:
    go_for_lunch()
else:
    play_chess_at_home()

# read two numbers
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))

# choose the larger number
if number1 > number2:
    larger_number = number1
else:
    larger_number = number2

# print the result
print("The larger number is:", larger_number)
 #or

 # read two numbers
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))

# choose the larger number
if number1 > number2: larger_number = number1
else: larger_number = number2

# print the result
print("The larger number is:", larger_number)


#tax calculator

income = float(input("Enter the annual income: "))
if income <= 85528.0:
    tax = (0.18 * income - 556.02)
elif income > 85528.0:
    tax = 14839.02 + 0.32 * (income - 85528.0)
tax = round(tax, 0)
print("The tax is:", tax, "thalers")
#GRegorian calendar

year = int(input("Enter a year: "))
if year % 4 != 0:
    print("Common year")
elif year % 100 != 0:
    print("Leap year")
elif year % 400 != 0:
    print("Common year")
else:
    print("Leap year")

#endless loop
while True:
    print("I'm stuck inside a loop.")

# we will store the current largest number here
largest_number = -999999999

# input the first value
number = int(input("Enter a number or type -1 to stop: "))

# if the number is not equal to -1, we will continue
while number != -1:
    # is number larger than largest_number?
    if number > largest_number:
        # yes, update largest_number
        largest_number = number
    # input the next number
    number = int(input("Enter a number or type -1 to stop: "))

# print the largest number
print("The largest number is:", largest_number)

#count no of odd and even

odd_numbers = 0
even_numbers = 0

# read the first number
number = int(input("Enter a number or type 0 to stop: "))

# 0 terminates execution
while number != 0:
    # check if the number is odd
    if number % 2 == 1:
        # increase the odd_numbers counter
        odd_numbers += 1
    else:
        # increase the even_numbers counter
        even_numbers += 1
    # read the next number
    number = int(input("Enter a number or type 0 to stop: "))

# print results
print("Odd numbers count:", odd_numbers)
print("Even numbers count:", even_numbers)

#while number != 0: and while number: are the same
#if number % 2 == 1: and if number % 2: condition to check if no is odd


counter = 5
while counter != 0:
    print("Inside the loop.", counter)
    counter -= 1
print("Outside the loop.", counter)

counter = 5
while counter:
    print("Inside the loop.", counter)
    counter -= 1
print("Outside the loop.", counter)

print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")

secret_number = 777
number = int(input("Enter no: "))
while secret_number:
    if number != secret_number:
        print("Ha ha! You're stuck in my loop!")
    else:
        print("Well done, muggle! You are free now.")
    number = int(input("Enter no: "))

for i in range(2, 8):#2,3,...7
    print("The value of i is currently", i)

for i in range(10):#starts from 0 ,ends at 9
    print("The value of i is currently", i)

for i in range(2, 8, 3):#third argument is increment
    print("The value of i is currently", i)    

for i in range(1, 1):
    print("The value of i is currently", i)#no output

#powers of two
pow = 1
for exp in range(16):
    print("2 to the power of", exp, "is", pow)
    pow *= 2

import time
for i in range(1,6):#for loop that counts upto 5
    print(i, "Mississippi")
    time.sleep(1)#suspend execution for one second

#this
# break - example

print("The break instruction:")
for i in range(1, 6):
    if i == 3:
        break
    print("Inside the loop.", i)
print("Outside the loop.")

#compare to-my version 
print("The break instruction:")
for i in range(1, 6):
    print("Inside the loop.", i)
    if i == 3:
        break
print("Outside the loop.")
   
# continue - example

print("\nThe continue instruction:")
for i in range(1, 6):
    if i == 3:
        continue
    print("Inside the loop.", i)
print("Outside the loop.")

largestNumber = -99999999
counter = 0
#break
while True:
    number = int(input("Enter a number or type -1 to end program: "))
    if number == -1:
        break
    counter += 1
    if number > largestNumber:
        largestNumber = number

if counter != 0:
    print("The largest number is", largestNumber)
else:
    print("You haven't entered any number.")

#continue
largestNumber = -99999999
counter = 0

number = int(input("Enter a number or type -1 to end program: "))

while number != -1:
    if number == -1:
        continue
    counter += 1

    if number > largestNumber:
        largestNumber = number
    number = int(input("Enter a number or type -1 to end program: "))

if counter:
    print("The largest number is", largestNumber)
else:
    print("You haven't entered any number.")

#secret word to leave loop

secret_word = "chupacabra"
word = input("Enter secret word: ")

while True:
    if word == "chupacabra":
        print("You've successfully left the loop.")
        break
    else:
        word = input("Enter secret word: ")
        
            
userWord = input("Enter word: ")
userWord = userWord.upper()

for letter in userWord:
    if letter == "E":
        if letter == "O":
            continue
    print(userWord)    
    
#the escape character
print("I like \"Monty Python\"")
print('I like "Monty Python"')
print('I\'m Monty Python.')
print("I'm Monty Python.")

userWord = input("Enter your word: ")
userWord = userWord.upper()

for letter in userWord:
    if letter == "A":
        continue
    elif letter == "E":
        continue
    elif letter == "I":
        continue
    elif letter == "O":
        continue
    elif letter == "U":
        continue
    else:
        print(letter)

#omitting letters,say ,in a woord.
userWord = input("Enter word:")
userWord = userWord.upper()



# Prompt the user to enter a word
# and assign it to the userWord variable.

for letter in userWord:
    if letter == "E":
        continue
    if letter == "O":
        continue
    print(letter)
    # Complete the body of the for loop.

wordWithoutVowels = ""

userWord = input("Enter your word: ")
userWord = userWord.upper()

for letter in userWord:
    if letter == "A":
        continue
    elif letter == "E":
        continue
    elif letter == "I":
        continue
    elif letter == "O":
        continue
    elif letter == "U":
        continue
    else:
        wordWithoutVowels += letter
		
print(wordWithoutVowels)








#pyramid(each lower layer contains one block more)
blocks = int(input("Enter the number of blocks: "))

height = 0
inlayer = 1
while inlayer <= blocks:
    height += 1
    blocks -= inlayer
    inlayer += 1

print("The height of the pyramid:", height)

#Lothar Collatz's hypothesis 3.1.2.15
c0 = int(input("Enter c0: "))

if c0 > 1:
	steps = 0
	while c0 != 1:
		if c0 %2 != 0:
			cnew = 3 * c0 + 1
		else:
			cnew = c0 // 2
		print(c0)
		c0 = cnew
		steps += 1
	print("steps =",steps)
else:
	print("Bad c0 value")

for digit in "0165031806510":
    if digit == "0":
        print("x", end="")
        continue
    print(digit, end="")

not (p and q) == (not p) or (not q)
not (p or q) == (not p) and (not q)   

#shifting one bit to right->dividing by two
#shifting one bit to the left->multiplying by two

var = 17
varRight = var >> 1#divide by two
varLeft = var << 2#multiply by 4
print(var, varLeft, varRight)

x = 1
y = 0

z = ((x == y) and (x == y)) or not(x == y)
print(not(z))

x = 4
y = 1

a = x & y
b = x | y
c = ~x
d = x ^ 5
e = x >> 2
f = x << 2

print(a, b, c, d, e, f)
#reverse order using the insert() method

myList = [] # creating an empty list

for i in range(5):
    myList.insert(0, i + 1)

print(myList)

myList = [10, 1, 8, 3, 5]
total = 0

for i in range(len(myList)):
    total += myList[i]

print(total)
#or ,shorter fyi
myList = [10, 1, 8, 3, 5]
total = 0

for i in myList:
    total += i

print(total)

#reversing order
myList = [10, 1, 8, 3, 5]

myList[0], myList[4] = myList[4], myList[0]
myList[1], myList[3] = myList[3], myList[1]

print(myList)

#reversing the order ,now for a larger list

myList = [10, 1, 8, 3, 5]
length = len(myList)

for i in range(length // 2):
    myList[i], myList[length - i - 1] = myList[length - i - 1], myList[i]

print(myList)


myList = [8, 10, 6, 2, 4] # list to sort

for i in range(len(myList) - 1): # we need (5 - 1) comparisons
    if myList[i] > myList[i + 1]: # compare adjacent elements
        myList[i], myList[i + 1] = myList[i + 1], myList[i] 

myList = [8, 10, 6, 2, 4] # list to sort
swapped = True # it's a little fake - we need it to enter the while loop

while swapped:
    swapped = False # no swaps so far
    for i in range(len(myList) - 1):
        if myList[i] > myList[i + 1]:
            swapped = True # swap occured!
            myList[i], myList[i + 1] = myList[i + 1], myList[i]

print(myList)

#or simply
myList = [8, 10, 6, 2, 4]
myList.sort()
print(myList)
#bubble sort interactive version
myList = []
swapped = True
num = int(input("How many elements do you want to sort: "))

for i in range(num):
    val = float(input("Enter a list element: "))
    myList.append(val)

while swapped:
    swapped = False
    for i in range(len(myList) - 1):
        if myList[i] > myList[i + 1]:
            swapped = True
            myList[i], myList[i + 1] = myList[i + 1], myList[i]

print("\nSorted:")
print(myList)
#name of list=memory location where it's stored  
list1 = [1]
list2 = list1#list1 & list2 identify same location in comp memory
list1[0] = 2
print(list2)#output is [2]

list1 = [1]
list2 = list1[:]#: is able to produce a new list
list1[0] = 2
print(list2)#output is [1]

myList = [10, 8, 6, 4, 2]
newList = myList[1:-1]
print(newList)

myList = [10, 8, 6, 4, 2]
newList = myList[-1:1]#start lies further than end.therefore output is empty
print(newList)

myList[:end]#= myList[0:end]
myList = [10, 8, 6, 4, 2]
newList = myList[:3]
print(newList)

myList[start:]#= myList[start:len(myList)]
myList = [10, 8, 6, 4, 2]
newList = myList[3:]
print(newList)

myList = [10, 8, 6, 4, 2]
newList = myList[:]#copies the whole list
print(newList)

myList = [10, 8, 6, 4, 2]
del myList[1:3]
print(myList)

myList = [10, 8, 6, 4, 2]
del myList[:]#deletes all elements
print(myList)

myList = [10, 8, 6, 4, 2]
del myList#deletes list itself
print(myList)#causes runtime error

myList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
toFind = 5
found = False

for i in range(len(myList)):
    found = myList[i] == toFind
    if found:
        break

if found:
    print("Element found at index", i)
else:
    print("absent")

 drawn = [5, 11, 9, 42, 3, 49]
bets = [3, 7, 11, 42, 34, 49]
hits = 0

for number in bets:
    if number in drawn:
        hits += 1

print(hits)

myList = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
newList = []
for number in myList:  # Browse all numbers from the source list.
	if number not in newList:  # If the number doesn't appear within the new list...
		newList.append(number)  # ...append it here.
myList = newList[:]  # Make a copy of newlist.
print("The list with unique elements only:")
print(myList)
squares = [x ** 2 for x in range(10)]#list comprehension
twos = [2 ** i for i in range(8)]
odds = [x for x in squares if x % 2 != 0 ]#only odd elements in squares list
board = [[EMPTY for i in range(8)] for j in range(8)]
#above is a nested list comprehension
#inner part creates a row
#outer part builds a list of rows
#board variable is now a two-dimensional array/matrix

#chessboard
EMPTY = "-"
ROOK = "ROOK"
board = []

for i in range(8):
    row = [EMPTY for i in range(8)]
    board.append(row)
board[0][0] = ROOK
board[0][7] = ROOK
board[7][0] = ROOK
board[7][7] = ROOK

print(board)
#automatic weather station 3.1.7.4
temps = [[0.0 for h in range(24)] for d in range(31)]
#rows -days of the month i.e 31 rows

#monthly average noon temperature i.e after filling matrix
total = 0.0

for day in temps:
    total += day[11]

average = total / 31

print("Average temperature at noon:", average)

#highest tempearature during the whole month

highest = -100.0
for day in temps:
    for temp in day:
        if temp > highest:
            highest = temp

print("The highest temperature was:", highest)

#days when the temperature at noon was at least 20 ℃
hotDays = 0

for day in temps:
    if day[11] > 20.0:
        hotDays += 1

print(hotDays, "days were hot.")
#multidimensional array;3buildings,15 floors,20 rooms
rooms = [[[False for r in range(20)] for f in range(15)] for t in range(3)]
#first index (0 through 2) selects one of the buildings;
#the second (0 through 14) selects the floor,
#the third (0 through 19) selects the room number.
#All rooms are initially free.

rooms[1][9][13] = True#book 2nd building,10th floor,room 14
rooms[0][4][1] = False
#release the second room on the fifth floor located in the first building:

#Check if there are any vacancies on the 15th floor of the third building:
vacancy = 0

for roomNumber in range(20):
    if not rooms[2][14][roomNumber]:
        vacancy += 1
#none keyword
def strangeFunction(n):
    if(n % 2 == 0):
        return True
print(strangeFunction(2))
print(strangeFunction(1))

#list as a function argument

def list_sum(lst):
    s = 0
    
    for elem in lst:
        s += elem
    
    return s
print(list_sum([5, 4, 3]))#invoking it


def strangeListFunction(n):
    strangeList = []
    
    for i in range(0, n):
        strangeList.insert(0, i)
    
    return strangeList

print(strangeListFunction(5))
#my version
def isYearLeap(year):
    if year % 4 == 0:
        return True
    else:
        return False
        
testData = [1900, 2000, 2016, 1987]
testResults = [False, True, True, False]
for i in range(len(testData)):
	yr = testData[i]
	print(yr,"->",end="")
	result = isYearLeap(yr)
	if result == testResults[i]:
		print("OK")
	else:
		print("Failed")
# course version
def isYearLeap(year):
	if year % 4 != 0:
		return False
	elif year % 100 != 0:
		return True
	elif year % 400 != 0:
		return False
	else:
		return True

testdata = [1900, 2000, 2016, 1987]
testresults = [False, True, True, False]
for i in range(len(testdata)):
	yr = testdata[i]
	print(yr,"-> ",end="")
	result = isYearLeap(yr)
	if result == testresults[i]:
		print("OK")
	else:
		print("Failed")

#How many days
def isYearLeap(year):
	if year % 4 != 0:
		return False
	elif year % 100 != 0:
		return True
	elif year % 400 != 0:
		return False
	else:
		return True

def daysInMonth(year,month):
	if year < 1582 or month < 1 or month > 12:
		return None
	days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
	res  = days[month - 1]
	if month == 2 and isYearLeap(year):
		res = 29
	return res

testyears = [1900, 2000, 2016, 1987]
testmonths = [ 2, 2, 1, 11]
testresults = [28, 29, 31, 30]
for i in range(len(testyears)):
	yr = testyears[i]
	mo = testmonths[i]
	print(yr,mo,"-> ",end="")
	result = daysInMonth(yr, mo)
	if result == testresults[i]:
		print("OK")
	else:
		print("Failed")        

#Day of the year
def isYearLeap(year):
	if year % 4 != 0:
		return False
	elif year % 100 != 0:
		return True
	elif year % 400 != 0:
		return False
	else:
		return True

def daysInMonth(year, month):
	if year < 1582 or month < 1 or month > 12:
		return None
	days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
	res  = days[month - 1]
	if month == 2 and isYearLeap(year):
		res = 29
	return res

def dayOfYear(year, month, day):
	days = 0
	for m in range(1, month):
		md = daysInMonth(year, m)
		if md == None:
			return None
		days += md
	md = daysInMonth(year, month)
	if day >= 1 and day <= md:
		return days + day
	else:
		return None

print(dayOfYear(2000, 12, 31))