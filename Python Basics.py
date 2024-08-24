# PYTHON PROBLEMS

# #1)addition
# x,y=input('give values of a and b: ').split(',')
# x=int(x)
# y=int(y)
# #print('Sum:',x+y,sep='')
# print(f'Sum:{x+y}')

# #2) area of circle
# radius=int(input('Give radius:'))
# area=3.14*radius*radius
# #area=3.14*(radius**2)
# #print('Area of the circle:',area,sep='')
# print(f'Area of the circle:{area}')

# #3)quadratic equations finding roots
# a=int(input('Give a:'))
# b=int(input('Give b:'))
# c=int(input('Give c:'))
# d=(b**2)-(4*a*c)
# root1=(-b +(d**(0.5)))/2*a
# root2=(-b -(d**(0.5)))/2*a
# #print(f'root1:{root1}',f'root2:{root2}')
# print(f'Roots:({root1},{root2})')

# #4)swap numbers
# #using temporary variable

# a=10
# b=20
# temp=a
# a=b
# b=temp
# print(f'After swapping:a={a},b={b}')

# a=int(input('Give a:'))
# b=int(input('Give b:'))
# temp=b
# a=temp
# b=a
# print(f'After swapping:a={a},b={b}')

# #without temp variable

# a=int(input('Give a:'))
# b=int(input('Give b:'))
# b=b+a
# #b+=a
# a=b-a
# b=b-a
# print(f'After Swapping:{a},{b}')

# #5)converting temperature units
# temp_celsius=int(input('temp in celsius:'))
# temp_fahrenheit=temp_celsius*(9/5)+32
# temp_kelvin=temp_celsius+273
# print(f'temp in fahrenheit:{temp_fahrenheit}')
# print(f'temp in kelvin:{temp_kelvin}')

# #6)currency converter
# amount_in_USD=int(input('Give amount:'))
# amount_in_euro=amount_in_USD*0.85
# print(f'total amount in euros:{amount_in_euro}')
# '''


# '''
# DECISION MAKING

# #if statement

# weather=input('How is weather:')
# if weather=='sunny':
#     print('play')

# #if-else statement

# weather=input('How is Weather:')
# if weather=='sunny':
#     print('play')
# else:
#     print('study')


# #if-elif-else statement

# weather=input('How is Weather:')
# if weather=='sunny':
#     print('play')
# elif weather=='rainy':
#     print('video game')
# else:
#     print('Go for a Walk')


# #AND operator
# weather=input('How is Weather:')
# Time=input('What is Time:')
# if weather=='sunny':
#     print('play')
# elif weather=='rainy':
#     print('video game')
# elif weather=='snowy' and Time=='night':
#     print('Bonfire')
# elif weather=='snowy' and Time=='morning':
#     print('work')
# else:
#     print('Go for a Walk')


# # Nested if statements
# weather=input('How is Weather:')
# Time=input('What is Time:')
# if weather=='sunny':
#     if Time=='morning':
#         print('play cricket')
#     elif Time=='Mid Day':
#         print('go for a walk')
#     else:
#         print('do nothing')
# elif weather=='rainy':
#     if Time=='morning':
#         print('Get an Umbrella')
#     elif Time=='Mid Day':
#         print('Do not go outside')
#     else:
#         print('stay at home')  
# else:
#     print('Go for a Walk')    

    






# #SIMPLE CALCULATOR
# number_a=int(input('Give 1st number:'))
# number_b=int(input('Give 2nd number:'))
# operator=input('Give an operator:')
# if operator=='+':
#     print(f'addition:{number_a+number_b}')
# elif operator=='-':
#     print(f'subtraction:{number_a-number_b}')
# elif operator=='*':
#     print(f'multiplication:{number_a*number_b}')
# elif operator=='/':
#     print(f'division:{number_a/number_b}')
# else:
#     print('Invalid operator')









# # STRINGS

# name=input('Enter your name:')
# #name='SREENU'
# print(name[-3])


# #STRING SLICING
# #string_indexing=[start:stop:step]
# #start=starting element=0
# #stop=ending element+1 =last index+1
# #step=increment/decrement

# name=input('Give name:')
# #print(name[:10])
# #print(name[0:])
# #print(name[:-1])
# #print(name[0:12:2])
# #print(name[::2])
# #print(name[0::2])
# #print(name[::-1])     # TO PRINT IN REVERSE ORDER
# #print(name[:0:-1])





# #STRING CONCATENATION = combining two strings

# first_name=input('Your First Name:')
# last_name=input('Your Last Name:')
# Details=f'Name:{first_name+last_name}'
# print(Details)




# #STRING LENGTH
# name='Sai Sreenivas Reddy'
# print(len(name))





# #STRING METHODS

# #Changing Lower case to Upper case = s.upper()

# name='Sai SreenivaS!'

# #print(name.upper()) #changing upper to lower

# #print(name.lower()) #changing lower to upper

# #print(name.strip()) #removing white spaces

# #print(name.replace('S','v')) #replacing letters

# #print(name.count('S')) #COUNTING how many times letter came


# #Taking Input from user

# name=input('Your Name:')
# letter=input('Which Letter:')

# #print(name.count(letter))

# result=name.replace(letter,letter.upper())
# print(result)

# #
# result=name.replace(letter,letter.lower())
# print(result)
# #
# #
# result=name.count(letter)
# print(result)
# #
# #
# change=input('Replace Which Letter:')
# result=name.replace(letter,change)
# print(result)
# #





# #STRING FORMATTING

# #  % formatting , str.format()  , f-strings

# name=input('What is Your Name:')
# age=int(input('Your Age:'))

# # % formatting

# result=('my name is %s , i am %d years old.'%(name,age))
# print(result)

# #  str.format

# result=('my name is {} , i am {}years old.'.format(name,age))
# print(result)

# # f-strings

# result=(f'my name is {name} , i am {age} years old.')
# print(result)





# # Escape Sequence   uses \ to escape

# car='sai\'s car'
# print(car)

# # uses \n to print in next line
# names='sai sreenivas \nsreenu reddy'   
# print(names)







# #  PROBLEMS ON STRINGS

# # 1)write a program to print a string input and , how many vowels in it.

# Input=input('Give a Word:')
# Input1=Input.lower()
# a=Input1.count('a')
# e=Input1.count('e')
# i=Input1.count('i')
# o=Input1.count('o')
# u=Input1.count('u')
# print(f'Number of vowels:{a+e+i+o+u}')



# # 2) Grade calculator

# maths=int(input('Marks in Maths:'))
# science=int(input('Marks in Science:'))
# english=int(input('Marks in English:'))
# total=maths+science+english
# #print(f'Total:{total}')
# percentage=(total/300)*100
# #print(f'Percentage:{percentage}')
# average=total/3
# #print(f'Average:{average}')
# if average>=90:
#     Grade='A'
#     #print('Grade:A')
# elif average>=80:
#     Grade='B'
#     #print(' Grade:B')
# elif average>=70:
#     Grade='C'
#     #print(' Grade:C')
# elif average>=60:
#     Grade='D'
#     #print(' Grade:D')
# else:
#     Grade='FAIL'
#     #print('FAIL')
# print(f'Total Marks:{total} \nPercentage:{percentage} \naverage:{average} \nGrade:{Grade}')


# # 3) Palindrome Checker
# word=input('Give a Word:')
# reverse=word[::-1]
# if word==reverse:
#     print('It is a Palindrome')
# else:
#     print('It is not a palindrome')


# # 4) Finding Largest Number

# numbers=input('Give Numbers:')
# a,b,c=numbers.split(',')
# a=int(a)
# b=int(b)
# c=int(c)

# if a>b and a>c:
#     print(f'Largest Number is:{a}')
# elif b>a and b>c:
#     print(f'Largest Number is:{b}')
# else:
#     print(f'Largest Number is:{c}')



# # 5) Leap Year Checker

# year=int(input('Give a Year:'))

# # 1)
# if year%4==0 and (year%100==0 or year%400!=0):
#     print(f'{year} is a Leap Year')
# else:
#     print('Mistake')


# # 2)
# if year%4==0:
#     print(f'{year} is a leap year')
# elif year%100==0 and year%400!=0:
#     print(f'{year} is not a leap year')
# else:
#     print(f'{year}is not a leap year')


# # 6) Temperature Converter
# temperature=int(input('Enter Temperature:'))
# unit=input('Enter unitsL:')
# if unit==('c'):
#     print(f'{temperature} C \n{(temperature*9/5)+32} F \n{temperature+273} k')
# elif unit==('f'):
#     print(f'{temperature} F \n{(temperature-32)*9/5} C \n{((temperature-32)*9/5)+273} k')
# else:
#     print(f'{temperature} K \n{(temperature-273)} C \n{((temperature-273)*9/5)+32} F')








# # LOOPS 

# # Loops are 2 Types
# # 1) For Loop
# # 2) While Loop


# # WHILE LOOP

# candies=int(input('How many candies you have:'))


# #if candies>0:
# #    print('Given to Friend1!')
# #    candies-=1
# #    print(candies)
# #if candies>0:
# #    print('Given to Friend2!')
# #    candies-=1
# #    print(candies)

# while candies>0:
#     print('given to friend!')
#     candies-=1
# print(f'remaining candies:{candies}')




# # FOR LOOPS

# candies=int(input('How Many Candies you have:'))
# for i in range(1,candies+1):
#     print(f'given to friend:{i}')
#     candies-=1
#     print(f'remaining candies:{candies}')


# # FOR LOOP FOR SEQUENCE

# message=input('Message:')


# #for i in message:
# #  print(i)



# length=len(message)
# for i in range(length):
#     print(message)





# #  NESTED LOOPS

# # printing TABLES from 1 to 5

# for i in range(1,6):
#     for j in range(1,11):
#         print(f'{i}*{j}={i*j}')

        



# # BREAK STATEMENT

# candies=10
# for i in range(candies):
#     print('given to friends!')
#     if i==5:

# #   if candies-i==5:

#         print('candies are low to 5!')
#         break


        




# # CONTINUE STATEMENT

# candies=10
# for i in range(candies):
#     if i==4:
#         print('special candy')
#         continue
#     print('giving candy to friends!')



    




# # PROBLEMS ON LOOPS

# # 1) printing numbers from 1 to N

# number=int(input('N:'))

# for i in range(1,number+1):
#     print(i)

# #i=1
# #while i<=number:
# #    print(i)
# #    i+=1
# print('done')




# # 2) calculating sum of N natural numbers

# number=int(input('N:'))
# i=1
# sum=0

# while i<=number:
#     i+=1
#     sum+=i
# #   sum=i   wrong
# print(sum)





# # 3) PRINT EVEN and ODD NUMBER IN GIVEN STRING

# number=int(input('Give a Number:'))
# i=1
# while i<=number:

# #    if i%2==0:       #  For EVEN NUMBERS

#     if not (i%2==0):  #  FOR ODD NUMBERS 
#         print(i)
#     i+=1




# # 4) MULTIPLICATION TABLE OF A GIVEN NUMBER

# n=int(input('Give a Number:'))

# for i in range(1,11):             # USING FOR LOOP
#     print(f'{n} * {i} = {n*i}')


# i=1                            # USING WHILE LOOP
# while i<=10: 
#     print(f'{n} x {i}={n*i}')
#     i+=1




# # 5) FINDING FACTORIAL OF A NUMBER             N!=N*N-1*N-2*.........1

# number=int(input('Give a Number:'))
# i=1
# #for n in range(1,number+i):         # FOR LOOP
# #    i=i*n

# #while number>0:                     # WHILE LOOP
# #    i=number*i
# #    number-=1
# print(i)


# # 6) FINDING PRIME NUMBERS

# prime = int(input("Give a Number:"))

# print(f"Prime numbers up to {prime} are:")

# for n in range(2, prime + 1):
#     is_prime = True
#     for i in range(2, int(n ** 0.5) + 1):
#         if n % i == 0:
#             is_prime = False
#             break
#     if is_prime:
#         print(n)


        

# i=1
# while i<=100:
#     print("Hello:",i)
#     i+=1


# # printing numbers 


# #forward

# i=int(input('Give a Number:'))
# while i<=100:
#     print(i)
#     i+=1
# print('loop ended')


# # reverse

# i=int(input('Give a Number:'))
# while i>=1:
#     print(i)
#     i-=1
# print('loop ended')




# multiplication of a given number

# table=int(input('Give a Number:'))
# i=1
# while i<=10: 
# #for i in range(1,10):
#     print(f'{table}x{i}={table*i}')
#     i+=1








# FUNCTIONS

# 1) PRE DEFINED AND FUNCTIONS    2) USER DEFINED FUNCTIONS

# def function_name(parameters):

# FUNCTION CALL

# FUNCTION_NAME(ARGUMENTS)

# RECURSION FUNCTION
# A FUNCTION CALL ITSELF
# USED FOR FIBONACCI SERIES
# BASE CASE AND RECURSIVE CASE

# LAMBDA FUNCTION
# SMALL FUNCTION DEFINED WITHIN A LARGER FUNCTION
# USED FOR SMALL TASKS
# USED FOR MAP, FILTER, REDUCE
# USED FOR ANONYMOUS FUNCTION

# lambda arguments:expression

# adding 2 numbers
# x,y=input('Give Numbers:').split(',')
# x,y=int(x),int(y)
# add=lambda x,y:x+y
# result=add(x,y)
# print(result)

# squaring a number
# x=int(input('Give a Number:'))
# square=lambda x:x**2
# result=square(x)
# print(f'Square of {x}={result}')




# PROBLEMS USING FUNCTIONS

# 1)  ADDING GIVEN 2 NUMBERS

# def add2numbers(a,b):
#     print(f'addition is: {a+b}')
# a=int(input('Give a Number:'))
# b=int(input('Give b Number:'))
# add2numbers(a,b)


# 2) AREA OF A CIRCLE

# def area(r):
#     return 3.14*r**2
# radius=int(input('Give Radius:'))
# a=area(radius)
# print(f'Area of Circle is: {a}')


# 3) SOLVING QUADRATIC EQUATIONS

# def calculateroots(a,b,c):
#     d=((b**2)-4*a*c)
#     root1=(-b +(d**0.5))/2*a
#     root2=(-b -(d**0.5))/2*a
#     print(f'Root1={root1},root2={root2}')
# a=int(input('Give a:'))
# b=int(input('Give b:'))
# c=int(input('Give c:'))
# calculateroots(a,b,c)


# 4) Swapping variables without using temp value

# def Swapping(a,b):
#     a=a+b
#     b=a-b
#     a=a-b
#     print(f'After Swapping:{a},{b}')
# a=int(input('Give a Number:'))
# b=int(input('Give b Number:'))
# Swapping(a,b)


# 5) CONVERTING TEMPERATURE

# def temp(a,b):
#     if unit==('c'):
#         print(f'temperature:{temperature}{unit}, {(temperature*9/5)+32}f, {temperature+273}k')
#     elif unit==('f'):
#         print(f'temperature:{temperature}{unit}, {(temperature-32)*9/5}c, {((temperature*9/5)-32)+273}k')
#     elif unit==('k'):
#         print(f'temperature:{temperature}{unit}, {temperature-273}c, {((temperature-273)*9/5)+32}')
# temperature=int(input('current temperature:'))
# unit=input('Give unit:')
# temp(temperature,unit)


# LISTS

# LISTS ARE MUTABLE 
# LIST IS A COLLECTION OF ITEMS WHICH CAN BE OF ANY DATA TYPE
# LIST IS DEFINED BY SQUARE BRACKETS
# LIST IS INDEXED
# LIST IS ORDERED

# list=[]
# list=[1,2,3,4,5]
# list=[1.23,2.34,3.45,4.56]
# list=['apple','banana','grape','orange']
# list=[1,2,3,1.23,2.34,'sai','veeru']


# print(list)
# print(list[0])
# print(list[4])
# print(list[5])
# print(list[-1])


# LIST SLICING

# list=[1,2,3,1.23,2.34,'sai','veeru']

# print(list[0:7])
# print(list[0:7:2])
# print(list[0:-1])
# print(list[:-1])
# print(list[::-1])     # to print in reverse order



# LIST MODIFYING

# list=[1,2,3,1.23,2.34,'sai','veeru']
# list[0]='sreenivas'
# list[6]='putta'
# print(list)


# METHODS IN LIST



# LIST COMPREHENSION            (it can converts string number to integer number)

# l=input('Give a List of Numbers:').split(',')
# # list=[int(item) for item in l]
# # list=[int(item)**2 for item in l]        # for squaring given number
# list=[int(item)**(int(input('Give a Number:'))) for item in l]
# print(list)


# append() to add element in list
# list=input('Give the list:').split(',')
# list.append(int(input('Give a Number:')))
# list=[int(item) for item in list]
# print(list)

# insert() to insert an element at particular place
# list=input('Give the List:').split(',')
# list.insert(int(input('where:')),int(input('Give a Number:')))
# list=[int(item) for item in list]
# print(list)

# remove() to remove an element 
# list=input('Give the List:').split(',')
# list.remove(input('Give a Number:'))
# list=[int(item) for item in list]
# print(list)

# pop() to remove an element from particular place
# list=input('Give the List:').split(',')
# list.pop(int(input('Give a Number:')))
# list=[int(item) for item in list]
# print(list)

# index() gives exact place of an element in list
# list=input('Give the List:').split(',')
# index=list.index((input('Give a Number:')))
# list=[int(item) for item in list]
# print(f'index of given number is:{index}')

# count() it counts how many times a number repeated
# list=input('Give the List:').split(',')
# count=list.count((input('Which number:')))
# list=[int(item) for item in list]
# print(count)


# sort() for sorting the given list

# sorting in ascending order which is default
# list=input('Give the List:').split(',')
# list.sort(reverse=False)
# list=[int(item) for item in list]
# print(list)

# sorting in descending order
# list=input('Give the List:').split(',')
# list.sort(reverse=True)
# list=[int(item) for item in list]
# print(list)

# reverse() it reverse print the list
# list=input('Give the List:').split(',')
# list.reverse()
# list=[int(item) for item in list]
# print(list)


# LIST CONCATENATION = ADDING THE TWO LISTS

# list1=input('Give a List:').split(',')
# list2=input('Give a List:').split(',')
# combine=list1+list2
# combine=[int(item) for item in combine]
# print(combine)







# TUPLES

# TUPLES ARE IMMUTABLE
# TUPLES ARE FASTER THAN LISTS
# TUPLES ARE USED WHEN WE NEED TO STORE A FIXED NUMBER OF ITEMS
# TUPLES ARE USED WHEN WE NEED TO STORE A COLLECTION OF ITEMS THAT SHOULD NOT BE CHANGED

# TUPLES USES () BRACKETS  or NOTHING

# TUPLE ACCESSING
# tuple=10,2,3
# print(tuple[0])

# TUPLE SLICING
# tuple=1,2,3,4,5,6,7,8
# print(tuple[0:7:2])


# THERE ARE LIMITED METHODS IN TUPLES COMPARING LISTS

# TUPLES USES TO PRINT CONSTANT VALUES WHICH CANNOT BE CHANGED FURTHER
# EXAMPLE : LATITUDES AND LONGITUDES IN GOOGLE MAPS

# FOR COUNTING THE NUMBER OF TIMES A NUMBER OCCURRED
# tuple=input('Give the tuple:').split(',')
# print(tuple.count(input('Which:')))


# FOR FINDING THE INDEX OF THE NUMBER
# tuple=input('Give the Tuple:').split(',')
# print(tuple.index(input('Which:')))







#  SETS
# SETS ARE UNORDERED AND COLLECTION OF UNIQUE ELEMENTS  (CAN'T INSERT REPEATED OR DUPLICATE  ELEMENTS)
# SETS ARE USED WHEN WE NEED TO STORE A COLLECTION OF ITEMS WITHOUT DUPLICATES
# SETS WILL AUTOMATICALLY REMOVES DUPLICATE ELEMENTS
# SETS ARE USED WHEN WE NEED TO STORE A COLLECTION OF ITEMS THAT NEED TO BE QUICKLY
# SET USES {} BRACKETS OR set()
# SETS ARE MUTABLE


# CREATING SETS

# EMPTY SET
# empty_set=set()

# SET WITH ELEMENTS
# empty_set={'sai','sreenu','sreenivas'}

# CREATING A SET WITH LIST
# numbers=set([1,2,3,4,5,6])

# ADDING AN ELEMENT IN SETS
# numbers={1,2,3,4,5}
# numbers.add(6)
# print(numbers)


# REMOVING AN ELEMENT FROM SET
# numbers={1,2,3,4,5}
# numbers.remove(4)
# print(numbers)



# SET OPERATIONS

# 1)SET UNION
# set1={1,2,3,4,5}
# set2={'sai','sreenu','sreenivas'}
# sets=set1.union(set2)
# print(sets)


# 2)SET INTERSECTION
# set1={1,2,3,4,5,'sai','sreenu'}
# set2={'sai','sreenu','sreenivas',1,2}
# sets=set1.intersection(set2)
# print(sets)


# 3)DIFFERENCE
# set1={1,2,3,4,'sai'}
# set2={1,3,'sreenu'}
# sets=set1.difference(set2)
# # sets=set2.difference(set1)
# print(sets)


# 4)SYMMETRIC DIFFERENCE
# set1={1,2,3,4,'sai'}
# set2={1,3,'sreenu'}
# sets=set1.symmetric_difference(set2)
# print(sets)




# SET MEMBERSHIP
# set1={1,2,3,4,'sai','sreenu'}
# print(2 in set1)            # IF ELEMENT IS PRESENT = TRUE
# print('sreenivas' in set1)    # IF ELEMENT IS NOT PRESENT = FALSE



# SET LENGTH = TO FIND HOW MANY ELEMENTS IN GIVEN SET
# set1={1,2,3,4,5,'sai','sreenu'}
# print(len(set1))


# FROZEN SET = IT IS IMMUTABLE
# set1={1,2,3,4,5,'sai','sreenu'}
# frozen=frozenset(set1)
# print(frozen)


# SET COMPREHENSION 
# set1={x**2 for x in range(1,10)}
# print(set1)

# SET CLEAR() , SET COPY() , SET POP() , SET UPDATE()







# DICTIONARY
# USES IN DATABASES
# ASSIGNING A VALUE TO A KEY
# UNORDERED COLLECTION OF KEY-VALUE PAIRS
# TO STORE THE DATA IN KEY-VALUE PAIRS
# USES {} BRACKETS
# KEY MUST BE UNIQUE
# KEY CAN BE ANY DATA TYPE
# VALUE CAN BE ANY DATA TYPE
# KEY AND VALUE CAN BE SAME
# DICTIONARY IS MUTABLE
# DICTIONARY IS INDEXED
# DICTIONARY IS DYNAMIC


# CREATING DICTIONARY

# my_dict={f'Name':'Sai Sreenivas', 'Age':'20', 'School':'LPU'}
# print(my_dict)


# ACCESSING THE VALUES

# my_dict={'Name':'Sai','Age':'20','School':'LPU'}
# name_value=my_dict['Name']
# age_value=[my_dict['Age']]
# school_value=my_dict['School']
# print(name_value)
# print(age_value)
# print(school_value)


# ADDING THE VALUES INTO DICTIONARY

# my_dict={'Name':'Sai','Age':'20','School':'LPU'}
# my_dict['Gender']='Male'
# print(my_dict)


# METHODS IN DICTIONARY

# get()- USES TO KNOW THE VALUE OF GIVEN KEY
# my_dict={'Name':'Sai','Age':'20','School':'LPU'}
# print(my_dict.get('Name'))


# pop()- USES TO DELETE THE KAY-VALUE IN DICTIONARY
# my_dict={'Name':'Sai','Age':'20','School':'LPU'}
# print(my_dict.pop('Age'))
# print(my_dict)


# items()- USES TO KNOW THE DATA IN DICTIONARY
# my_dict={'Name':'Sai','Age':'20','School':'LPU'}
# print(my_dict.items())


# values()- USES TO KNOW THE ONLY VALUES IN DICTIONARY
# my_dict={'Name':'Sai','Age':'20','School':'LPU'}
# print(my_dict.values())


# keys()- USES TO KNOW KEYS IN DICTIONARY
# my_dict={'Name':'Sai','Age':'20','School':'LPU'}
# print(my_dict.keys())




# LOOPING -  USING LOOPS TO ITERATE IN DICTIONARY
# my_dict={'Name':'Sai','Age':'20','School':'LPU'}

# TO PRINT ONLY VALUES

# for values in my_dict.values():
#     print(values)

# TO PRINT ONLY KEYS
# for keys in my_dict.keys():
#     print(keys)

# TO PRINT BOTH KEYS AND VALUES COMBINE
# for i,j in my_dict.items():
#     print(f'{i}:{j}')


# COMPREHENSION IN DICTIONARY
# Comprehensions allow you to write more readable and expressive code compared to traditional loops.
# squares={x:x**2 for x in range(1,11)}
# for i,j in squares.items():
#     print(f'{i}:{j}')






# PROBLEMS 

# 1) FINDING THE SUM OF ALL NUMBERS GIVEN IN LIST
# l=input('Give the Number List:').split(',')
# l=[int(item) for item in l]
# sum=0
# for i in l:
#     sum+=i
# print(sum)

# i=0
# length=len(l)
# while i<length:
#     sum=sum+l[i]
#     i+=1
# print(sum)


# 2) FINDING THE MAXIMUM AND MINIMUM VALUES IN LIST OF NUMBERS

# TAKING USER INPUT [LIST] BY USING COMPREHENSION

# BY SORTING THE LIST

# l=[1,3,2,4,6,7,8,5]
# l.sort()
# print(f'MIN:{l[0]}  and  MAX:{l[-1]}')


# BY TAKING INPUT FROM USER

# list1=input('Give the List of Numbers:').split(',')
# list1=[int(item) for item in list1]
# list1.sort()
# print(f'MIN:{list1[0]} and MAX:{list1[-1]}')


# BY USING LOOP

# list1=input('Give the Numbers List:').split(',')
# list1=[int(item) for item in list1]
# MIN=list1[0]
# MAX=list1[0]
# for i in list1:
#     if i>MAX:
#         MAX=i
#     if i<MIN:
#         MIN=i
# print(f'MIN:{MIN} and MAX:{MAX}')




# 3) REMOVING DUPLICATE ELEMENTS FROM LIST TO CREATE A NEW LIST

# USING LOOP
# list1=input('Give a List of Numbers:').split(',')
# list1=[int(item) for item in list1]
# new_list=[]
# for i in list1:
#     if i in new_list:
#         continue
#     else:
#         new_list.append(i)
# print(f'New List:{new_list}')


# CONVERTING LIST INTO A SET
# list1=input('Give a List of Number:').split(',')
# list1=[int(a) for a in list1]
# list2=set(list1)
# list2=list(list2)
# print(f'New List:{list2}')



# 4)COUNTING THE NUMBER OF OCCURRENCES OF A SPECIFIC ELEMENT IN LIST

# USING LOOP
# list1=[int(a) for a in input('Give a List of Numbers:').split(',')]
# number=int(input('Which Number:'))
# count=0
# for i in list1:
#     if i==number:
#         count+=1
# print(f'{count} Times')



# USING COUNT() 
# list1=[int(a) for a in input('Give the List of Numbers:').split(',')]
# number=int(input('Which Number:'))
# number_count=list1.count(number)
# print(number_count)



# 5)FINDING INTERSECTION AND UNION OF TWO SETS


# set1={int(a) for a in input('Give 1st Set Numbers:').split(',')}
# set2={int(a) for a in input('Give 2nd Set Numbers:').split(',')}
# set_union=set1.union(set2)
# set_intersection=set1.intersection(set2)
# print(f'Union of Sets:{set_union} \nIntersection of Sets:{set_intersection}')




# 5)CREATE A DICTIONARY AND ACCESS VALUES AND UPDATE VALUES AND ITERATE THROUGH KEY-VALUE PAIRS

# TAKING INPUT FROM USER FOR DICTIONARY

# my_dict={}
# name=input('Name:')
# age=input('Age:')
# gender=input('Gender:')
# place=input('Place:')

# my_dict['Name']=name
# my_dict['Age']=age
# my_dict['Gender']=gender
# my_dict['Place']=place
# # print(my_dict)

# # FOR ITERATION USING LOOP
# for i,j in my_dict.items():
#     print(f'{i}:{j}')











