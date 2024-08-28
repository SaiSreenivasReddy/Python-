# LOOPS
# LOOPS ARE USED TO REPEAT INSTRUCTIONS
# LOOPS ARE OF 2 TYPES - 1) WHILE LOOP AND 2) FOR LOOP
# WHILE LOOP IS USED WHEN WE DON'T KNOW HOW MANY TIMES WE NEED TO REPEAT
# FOR LOOP IS USED WHEN WE KNOW HOW MANY TIMES WE NEED TO REPEAT


# 1) WHILE LOOP

# IT WILL RUN UNTIL THE GIVEN CONDITION IS TRUE
# IT WILL CHECK THE CONDITION AT THE BEGINNING OF EACH ITERATION

# "while condition:"

# EXAMPLE

# count=1 # ITERATOR
# while count<=5: # STOPPING CONDITION
#     print('hello',count)
#     count+=1

# PRINTING NUMBERS FROM 1-5

# i=1
# while i<=5:
#     print(i)
#     i+=1

# PRINTING NUMBER IN REVERSE

# i=10
# while i>=1:
#     print(i)
#     i-=1


# PROBLEMS

# 1) PRINTING NUMBERS FROM 1-100
# count=1
# while count<=100:
#     print(count)
#     count+=1


# 2) PRINTING NUMBERS FROM 100-1
# count=100
# while count>=1:
#     print(count)
#     count-=1


# 3) PRINTING THE MULTIPLICATION OF A NUMBER
# i=int(input('Give a Number:'))
# j=1
# while j<=10:
#     print(f'{i}X{j}={i*j}')
#     j+=1

# 4) PRINTING A LIST USING LOOP
# list=[1,2,3,4,5,6,7,8,9,10]
# index=0
# while index<len(list):
#     print(list[index])
#     index+=1


# 5) PRINTING SQUARES OFF NUMBERS
# list=1
# while list<=10:
#     print(f'{list**2}')
#     list+=1

# 6) SEARCHING FOR A NUMBER IN A GIVEN TUPLE
# tuple=(1,2,3,4,5,6,7,8,9,10)
# number=5
# i=0
# while i<len(tuple):
#     if(tuple[i]==number):
#         print('found at',i)
#     else:
#         print('finding...')
#     i+=1



# BREAK AND CONTINUE

# BREAK - USED TO TERMINATE THE LOOP WHEN ENCOUNTERED

# i=1
# while i<=10:
#     print(i)
#     if(i==5):
#         break
#     i+=1
# print('loop ended')



# SEARCHING FOR A NUMBER IN A GIVEN TUPLE
# tuple=[int(item) for item in input('Give a Tuple:').split(',')]
# number=int(input('which number:'))
# i=0
# while i<len(tuple):
#     if(tuple[i]==number):
#         print('found at',i)
#         break
#     else:
#         print('finding...')
#     i+=1


# CONTINUE - USED TO TERMINATES EXECUTION OF THE CURRENT ITERATION AND CONTINUOUS TO EXECUTE THE NEXT ITERATION


# i=0
# while i <= 10:
#     if(i==5):
#         i+=1
#         continue
#     print(i)
#     i+=1

# PRINTING ONLY ODD NUMBERS FROM 1-100

# i=1
# while i <= 100:
#     if(i%2==0):
#         i+=1
#         continue
#     print(i)
#     i+=1


# PRINTING ONLY even NUMBERS FROM 1-100

# i=1
# while i <= 100:
#     if(i%2!=0):
#         i+=1
#         continue
#     print(i)
#     i+=1




# 2) FOR LOOP


# FOR LOOP IS USED TO ITERATE OVER A SEQUENCE (LIST, TUPLE, STRING,SETS,DICTIONARY ETC..)
# FOR LOOP IS USED TO ITERATE OVER A RANGE OF NUMBERS

# "for element in list:"

# EXAMPLE


# LISTS

# numbers=[1,2,3,4,5,6,7,8,9,10]
# for value in numbers:
#     print(value)


# veggies=['onion','tomato','cucumber','radish']
# for elements in veggies:
#     print(elements)


# TUPLES

# tup=(1,2,3,4,5,6,7,8,9,10)
# for value in tup:
#     print(value)


# SETS

# sets={1,2,3,1,2,3,4,5,6,4,5,6,7,8,9,7,8,9}
# for value in sets:
#     print(value)


# STRING

# string='sreenivas'
# for char in string:
#     print(char)


# ELSE USING WITH FOR LOOP           (NOT MANDATORY)
# ELSE IS USED TO EXECUTE A BLOCK OF CODE WHEN THE LOOP DOESN'T BREAK

# sets={1,2,3,4,5,6,7,8,9,10}
# for value in sets:
#     print(value)
# else:
#     print('loop ended')


# USING BREAK STATEMENT

# string='sai sreenivas'
# for char in string:
#     if(char=='v'):
#         print('v found')
#         break
#     print(char)
# else:
#     print('loop ended')



# PROBLEMS

# 1) PRINT THE ELEMENTS OF THE GIVEN LIST
# lists=[int(i) for i in input('Give a list:').split(',')]
# # lists=[1,2,3,4,5,6,7,8,9,10]
# for i in lists:
#     print(i)


# 2) SEARCH FOR A NUMBER IN GIVEN TUPLE 

# tup=[int(item) for item in input('Give a tuple:').split(',')]
# num=int(input('which number:'))
# index=0
# for i in tup:
#     if i==num:
#         print('found at ',index)
#     index+=1



# RANGE() 

# range() IS USED TO GENERATE A SEQUENCE OF NUMBERS
# IT IS USED WITH FOR LOOP
# IT IS USED TO GENERATE A SEQUENCE OF NUMBERS


# range(start,stop,step)

# PRINTING NUMBERS 

# for i in range(10):        # range(stop)
#     print(i)


# for i in range(2,10):      # range(start,stop)
#     print(i)


# for i in range(1,10,2):   # range(start,stop,step)
#     print(i)


# PRINTING EVEN AND ODD NUMBERS

# for i in range(2,101,2):     # FOR EVEN NUMBERS
# for i in range(1,100,2):       # FOR ODD  NUMBERS
    # print(i)




# PROBLEMS

# 1) WAP FOR PRINTING NUMBERS FROM 1-100

# for i in range(1,101):
#     print(i)


# 2) WAP FOR PRINTING NUMBERS FORM 100-1

# for i in range(100,0,-1):
#     print(i)


# 3) PRINT MULTIPLICATION OF GIVEN NUMBER

# num=int(input('Give a Number:'))
# for i in range(1,11):
#     print(i*num)



# PASS STATEMENT

# PASS IS A NULL STATEMENT THAT DOES NOTHING.IT IS USED AS PLACEHOLDER FOR FUTURE CODE
# IT IS USED WHEN WE WANT TO EXECUTE A BLOCK OF CODE WITHOUT DOING ANYTHING
# IT IS USED WHEN WE WANT TO IGNORE A BLOCK OF CODE
# IT IS USED WHEN WE WANT TO EXECUTE A BLOCK OF CODE WITHOUT RAISING ANY ERROR


# for i in range(5):
#     pass
# print('Hello World')











# PROBLEMS

# 1) WAP TO FIND THE SUM OF FIRST N NATURAL NUMBERS

# USING WHILE LOOP

# num=int(input('Give a Number:'))
# sum=0
# i=1
# while i<=num:
#     sum+=num
#     i+=1
# print(sum)


# USING FOR LOOP

# num=int(input('give a number:'))
# sum=0
# for i in range(1,num+1):
#     sum+=i
# print(sum)


# 2) WAP TO FIND FACTORIAL OF FIRST N NATURAL NUMBERS

# USING WHILE LOOP

# number=int(input('Give a number'))
# fact=1
# i=1
# while i<=number:
#     fact*=i
#     i+=1
# print(fact)


# USING FOR LOOP

# num=int(input('Give a Number:'))
# fact=1
# for i in range(1,num+1):
#     fact*=i
# print(fact)







