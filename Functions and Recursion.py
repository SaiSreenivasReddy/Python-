# FUNCTIONS
# BLOCK OF STATEMENT THAT PERFORMS SPECIFIC TASKS
# FUNCTIONS ARE REUSABLE CODE BLOCKS
# FUNCTIONS CAN TAKE ARGUMENTS AND RETURN VALUES
# USED TO DECREASE REPEATED NESS OR REDUNDANCY OF CODE


# EXAMPLE  -  SUM OF 2 NUMBERS

# FUNCTION ARGUMENTS
# def sum_numbers(a,b): # PARAMETERS
#     sum=a+b
#     print(sum)
#     return
# a,b=[int(item) for item in  input('Give a and b:').split(',')]  # FUNCTION CALL : ARGUMENTS
# sum_numbers(a,b)
# # n NUMBER OF LINES OF CODE   AND

# sum_numbers(a,b) # FUNCTION CALL : ARGUMENTS


# # # n NUMBERS OF LINES OF CODE AND

# sum_numbers(a,b) # FUNCTION CALL : ARGUMENTS




# EXAMPLE - PRINTING HELLOWORLD

# def hello_world():
#     message=input('Give Message:')
#     times=int(input('How many times:'))
#     for i in range(times):
#         print(message)
# hello_world() # DEFAULT PARAMETER


# EXAMPLE  -  FINDING AVERAGE OF NUMBERS

# FOR 3 NUMBERS
# def num_avg(a,b,c):
#     sum=a+b+c
#     avg=sum/3
#     print(avg)
#     return avg
# a,b,c=[int(item) for item in input('Give a,b,c:').split(',')]
# num_avg(a,b,c) # DEFAULT PARAMETER


# FOR N NUMBER OF VARIABLES
# def sum_avg(*numbers):
#     total=sum(numbers)
#     avg=total/len(numbers)
#     print(avg)
#     return
# numbers=[int(item) for item in input('Give Numbers:').split(',')]
# sum_avg(*numbers) # DEFAULT PARAMETER




# FUNCTIONS IN PYTHON ARE OF TWO TYPES

# 1. BUILT IN FUNCTIONS
# PRINT() , LEN() , TYPE() , RANGE()


# 2. USER DEFINED FUNCTIONS
# FUNCTIONS THAT USER DEFINE'S 





# PROBLEMS IN FUNCTIONS

# 1)WAP TO CALCULATE LENGTH OF THE LIST

#  FOR ONLY ONE LIST

# def list_length(heros,names):
#     # list=[int(item) for item in input('Give the list:').split(',')]
#     list=input('Give the list:').split(',')
#     length=len(list)
#     print()
#     return(length)
# list_length(input('Give a input:'))



# FOR MULTIPLE LISTS

# heros=[item.strip() for item in input('Give heros list:').split(',')]
# names=[item.strip() for item in input('Give names list:').split(',')]
# def list_length(lists):
#     if lists=='heros':
#         heros_length=len(heros)
#         print(f'heros length:{heros_length}')
#     elif lists=='names':
#         names_length=len(names)
#         print(f'names list:{names_length}')
#     else:
#         print('Invalid input')
#         return
# lists=input('Give list to check length:')
# list_length(lists)



# 2) WAP TO PRINT THE ELEMENTS OF A LIST IN A SINGLE LINE

# WHEN LIST IS PRE GIVEN
# heros=['Clark Kent', 'Bruce Wayne', 'Diana Prince']
# def print_list(heros):
#     for hero in heros:
#         print(hero)
#     return
# print_list(heros)



# WHEN USER IS GIVING LIST INPUT

# list prints in on line

# def print_list(*list):
# # def print_list(list):
#     list=[item.strip() for item in input('Give a list:').split(',')]
#     print(list)
#     return
# print_list()
# # print_list(list)


# LIST PRINTS IN DIFFERENT LINES

# def print_list(list):
#     list=[item.strip() for item in list]
#     for i in list:
#         print(i)
#     return
# list=input('Give the list:').split(',')
# print_list(list)




# 3) WAP TO FIND A FACTORIAL OF A GIVEN NUMBER

# def cal_fact(n):
#     fact=1
#     for i in range(1,n+1):
#         fact*=i
#     print(fact)
#     return
# n=int(input('Give a Number:'))
# cal_fact(n)
    



# 4) WAP TO COVERT USD TO INR

# def inr_conv(usd):
#     inr=usd*83
#     print(usd,'USD =',inr,'INR')
#     return
# usd=float(input('Give USD:'))
# inr_conv(usd)



# 5) WAP IF GIVEN INPUT IS EVEN OR ODD

# def even_odd(number):
#     if  number%2==0:
#         print(number,'is EVEN')
#     elif number%2!=0:
#         print(number,'is ODD')
#     else:
#         print('invalid input')
#         return
# number=int(input('Give a Number:'))
# even_odd(number)









#  RECURSION

# A FUNCTION CALLS ITSELF
# RECURSION IS USED TO SOLVE PROBLEMS THAT CAN BE BROKEN DOWN INTO SIMILAR AND DUB-PROBLEMS
# RECURSION IS USED TO SOLVE PROBLEMS THAT HAVE THE FOLLOWING PROPERTIES
# 1) A PROBLEM CAN BE BROKEN DOWN INTO SIMILAR SUB-PROBLEMS
# 2) THE SOLUTION TO THE OVERALL PROBLEM CAN BE OBTAINED BY COMBINATION OF THE SOLUTIONS OF ITS SUB-PROBLEMS
# 3) THE SUB-PROBLEMS SHOULD BE SMALLER IN SIZE THAN THE ORIGINAL PROBLEM

# RECURSION IS SIMILAR TO LOOPS
# RECURSION IS USED WHEN THE PROBLEM SIZE IS SMALL


# EXAMPLE  -  PRINT NUMBERS FROM GIVEN NUMBER TO 1

# def print_numbers(number):
#     # if number==0: # FOR UPTO 1
#     if number==-1:  # FOR UPTO 0
#         return
#     print(number)
#     print_numbers(number-1)
# number=int(input('Give a Number:'))
# print_numbers(number)




# EXAMPLE  -  FINDING FACTORIAL OF GIVEN INPUT

# def number(n):
#     if(n==0 or n==1):
#         return 1
#     else:
#         return number(n-1)*n
# n=int(input('Give a Number:'))
# print(number(n))


# PROBLEMS

# 1) WAP TO CALCULATE THE SUM OF FIRST N NATURAL NUMBERS

# def natural_numbers(n):
#     if n==1:
#         return 1
#     else:
#         return n+natural_numbers(n-1)
# n=int(input('Give a Number:'))
# print(natural_numbers(n))

# 2) WAP TO PRINT ALL ELEMENTS IN A LIST
# def print_list(list,index):
#     if index==len(list):
#         return
#     print(list[index])
#     print_list(list,index+1)
# fruits=input('Give a List:').split(',')
# print_list(fruits,0)
    