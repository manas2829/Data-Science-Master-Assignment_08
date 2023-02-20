#!/usr/bin/env python
# coding: utf-8

# # Assignment_07-02-2023

# ## 1. You are writing code for a company. The requirment of the company is that you create a Python function that will check whether the password entered by the user is correct or not. The function take the password as input and return the string "Valid Password" if the enter password follows the below-given password guide lines else it should "Invaild Password".
# 
# ## Note:
# ## 1.The Password should contain at least two upper letters and at least two lower case letters 
# ## 2. The password should contain at least a number and three Special characters.
# ## 3. The length of the password should be 10  characters long.
# 
# ### Ans:-

# In[1]:


def check_password(password):
    upper_count=0
    lower_count=0
    number_count=0
    special_count=0
    
    for chr in password:
        if chr.isdigit():
            number_count+=1
        elif chr.isupper():
            upper_count+=1
        elif chr.islower():
            lower_count+=1
        elif chr in "@_!#$%^&*()<>?/|}{~:":
            special_count+=1
    if upper_count >=2 and lower_count >=2 and number_count>=1 and special_count>=3 and len(password)>=10:
        return ("Valid password")
    else:
        return ("Password Invalid")

password = input("Enter the Password:  ")
print(check_password(password))


# In[2]:


def check_password(password):
    upper_count=0
    lower_count=0
    number_count=0
    special_count=0
    
    for chr in password:
        if chr.isdigit():
            number_count+=1
        elif chr.isupper():
            upper_count+=1
        elif chr.islower():
            lower_count+=1
        elif chr in "@_!#$%^&*()<>?/|}{~:":
            special_count+=1
    if upper_count >=2 and lower_count >=2 and number_count>=1 and special_count>=3 and len(password)>=10:
        return ("Valid password")
    else:
        return ("Invalid Password")

password = input("Enter the Password:  ")
print(check_password(password))


# ## 2. Solve the below -given question using at least one of the following:
# 
# ## 1. Lambda Function
# ## 2. Filter Function
# ## 3. Map  Function
# ## 4. List   Comprehension
# 
#    ### a- Check if the string starts with a particular letter.
#    ### b- Check if the string is numeric.
#    ### c- sort a list of tuples having function name and their quantity. [("mango",99),("Orange",80),("Grapes",1000)]
#    ### d- Find Squares of number 1 to 10.
#    ### e- Find the cube root of the number 1 to 10.
#    ###  f- Check if a given number is even
#    ### g- Filter odd numbers from the given list. [1,2,3,4,5,6,7,8,9,10]
#    ### h- sort a list of integers into positive and negative integers lists.[1,2,3,4,5,6,-1,-2,-3,-4,-5,0]
# 
# 

# In[3]:


## Check if the string starts with a particular letter by using lambda
str1 = "Manas"
if str1[0]== "M":
    print("The string start with letter")
else:
    print("The string doesnot start with letter")


# In[4]:


starts_with = lambda string,letter:string.startswith(letter)
string = "Manas Ranjan Pandey"
if starts_with(string,"M"):
    print("The string start with {}".format('M'))
else:
    print("The string start with {}".format('M'))
    


# In[5]:


strings = ["Hello World", "Python", "Programming"]
starts_with = lambda string, letter: string.startswith(letter)

result = list(map(starts_with, strings, ["H"] * len(strings)))

print(result)


# In[6]:


starts_with = lambda string, letter: string.startswith(letter)


# In[7]:


string = "Hello World"
if starts_with(string, "H"):
    print("The string starts with H.")
else:
    print("The string does not start with H.")


# In[8]:


## Check if the string is numeric by using lambda function.
string="9826470741"
numeric = lambda string:string.isdigit()
if numeric(string):
    print ("The string is numeric")
else:
    print("The string is not numeric")


# In[9]:


string="Manas"


# In[10]:


numeric = lambda string:string.isdigit()


# In[11]:


if numeric(string):
    print ("The string is numeric")
else:
    print("The string is not numeric")


# In[12]:


##sort a list of tuples having function name and their keys. [("mango",99),("Orange",80),("Grapes",1000)] by using lambda.
fruits = [("mango", 99), ("Orange", 80), ("Grapes", 1000)]

sorted_fruits = sorted(fruits, key=lambda x: x[0])

print(sorted_fruits)


# In[13]:


##sort a list of tuples having function name and their quantity. [("mango",99),("Orange",80),("Grapes",1000)] by using lambda.
fruits = [("mango", 99), ("Orange", 80), ("Grapes", 1000)]

sorted_fruits = sorted(fruits, key=lambda x: x[1])

print(sorted_fruits)


# In[14]:


##Find Squares of number 1 to 10.
for i in range(1,11):
    Sqr = i**2
    print(Sqr,end=",")


# In[15]:


##Find Squares of number 1 to 10 in list comprehension
Squares=[i**2 for i in range(1,11)]
print(Squares)


# In[16]:


##Filter odd numbers from the given list. [1,2,3,4,5,6,7,8,9,10] using Filter function.
list1=[1,2,3,4,5,6,7,8,9,10]
list(filter(lambda x:x%2!=0,list1))


# In[17]:


##Filter even numbers from the given list. [1,2,3,4,5,6,7,8,9,10] using Filter function.
list(filter(lambda x:x%2==0,list1))


# In[18]:


## Find the cube root of the number 1 to 10.
import math
for i in range (1,11):
    cube_root =  math.pow(i,1/3)
    print(cube_root,end=",")


# In[19]:


## Find the cube root of the number 1 to 10 using list comprehension.
import math
cube_root=[math.pow(i,1/3) for i in range(1,11)]
print(cube_root)


# In[20]:


##sort a list of integers into positive and negative integers lists.[1,2,3,4,5,6,-1,-2,-3,-4,-5,0]
numbers= [1,2,3,4,5,6,-1,-2,-3,-4,-5,0]
positive_num=[]
negative_num=[]
for num in numbers:
    if num > 0:
        positive_num.append(num)
    elif num < 0:
        negative_num.append(num)
print("positive numbers",positive_num)
print("negative numbers",negative_num)


# In[21]:


##sort a list of integers into positive and negative integers lists.[1,2,3,4,5,6,-1,-2,-3,-4,-5,0] using filter function.
numbers= [1,2,3,4,5,6,-1,-2,-3,-4,-5,0]
positive_num=list(filter(lambda x:x>0,numbers))
Negative_num=list(filter(lambda x:x<0,numbers))

print("Positve Numbers",positive_num)
print("Negative Numbers",Negative_num)


# In[22]:


from functools import reduce


# In[23]:


##Check if a given number is even by using reduced function.
 
num= int(input("Enter the number:  "))
is_even = reduce(lambda a,b:a and b,[num%2==0])

if is_even:
    print(num," is even number")
else:
    print(num,"is odd number")

