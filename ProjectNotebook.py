#!/usr/bin/env python
# coding: utf-8

# # Project Description

# Write a brief description of your project here. 
# 
# Note that projects should be self-sufficient, so make sure to provide enough information and context here for someone to understand what you are doing in your project, and why. 

#    This project was meant to expand on A2 cipher since now with this hopefully improved version our keys will be a little tricky to figure out. The main idea is that it takes in a string to either encode or decode just like A2 but when it comes to the key we have another string that we increment through one by one using the letters ascii value to encrypt/decrypt the message. For the scope of the project I only kept the legitimate inputs to lower case letters because it's harder to do it for all characters and they really aren't necessary for hiding our secret messages. 
#     First I made the cryptMethods module and defined the two isLowerCase functions as they are very important in identifying if our input is formatted correctly. The first implementation takes in one letter and checks then we use the second to handle larger actual strings. Lucky for us if the input does happen to be incorrect these methods will catch it and act accordingly.
#     Then we defined our basic encoder/decoder that just submitted one character by one key similar to A2 implementations, but our cool encoder/decoder allowed us to take our encryption talents to a new level. With our cool functions we use a loop to increment through our strings one by one so the key is not staying the same throughout the process. For example I provided a solution below where it takes josedeleon and cogs as a string and returns the new string lcywfsrwqb
# 

# ## Project Code
# 
# If it makes sense for your project, you can have code and outputs here in the notebook as well.

# In[1]:


from my_module import cryptMethods as cry
#from my_module.classes import ...


# In[5]:


stringP = input("Please enter a string only containing lowercase letters to be encoded/decoded:\n")
keyP = input("Please enter a string only containing lowercase letters to encode/decode by:/n")
desired = input("Would you like to encode or decode. PLease enter either ""encode"" or ""decode"":/n")
if(cry.isLowerCaseS(stringP) == False or cry.isLowerCaseS(keyP) == False 
   + cry.isLowerCaseS(desired) == False):
    print("invalid")
else:
    if(desired == "encode"):
        ans = cry.coolEncode(stringP, keyP)
        print(ans)
    else:
        ans = cry.coolDecode(stringP, keyP)
        print(ans)


# In[3]:


# test it out
assert cry.coolEncode("josedeleon", "cogs") == "lcywfsrwqb" 


# #### Extra Credit (*optional*)
# 
# This class was my first experience with python but I have messed with other languages before this class like java and c.
# I believe I went above the request because I provided more than the required amount of tests and functions. On top of this I was able to expand upon the basic ideas of A2 from scratch making a slighlty better encoder/decoder as explained in the intro.
