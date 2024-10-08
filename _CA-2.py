#!/usr/bin/env python
# coding: utf-8

# # CA-2 INT-565
Jasthi Lakshmi Narayana
Registration number: 12401996
section:K24ML
Roll no: 29
# Scenario: Dictionary Lookup Tool
# Design a program that allows users to look up definitions of terms in a dictionary. Handle cases where the term does not exist in the dictionary (KeyError) and provide a suggestion for similar terms if possible.
# Objective: Manage KeyError with meaningful error messages and suggestions.
# 

# In[17]:


import difflib

difflib is a module for comparing sequences of lines of text, and producing human-readable differences or deltas
# In[19]:


#creating dictionary
book={"python":"a programming langauge",
            "variable":"variables are containers used to store data",
            "list":"used to store group of elements"}

Here "book" is a dictionary which stores words and its definations as keys and values
# In[20]:


#creating a function name Looup to perform operation
def Lookup(word):
    try:
        definition= book[word]
        print(f"Definition of '{word}' is : {definition}")
    except KeyError:
        print(f" '{word}' which you have searched is not present in book")
        suggestion = difflib.get_close_matches(word, book.keys())
        if suggestion:
            print(f"may be you are searching for the word: {', '.join(suggestion)}?")
        else:
            print("No similar words are there.")

KeyError: KeyError is raised when we try to access a key from dict, which doesn't exist.
difflib.get_close_matches: Return a list of the best “good enough” matches. word is a sequence for which close matches are desired (typically a string), and possibilities is a list of sequences against which to match word (typically a list of strings).
# ### Test case:1

# In[23]:


#asking user to enter the word to search
user_input = input("Enter a term to look up: ")

#calling function
Lookup(user_input)


# ### Test case:2

# In[24]:


#asking user to enter the word to search
user_input = input("Enter a term to look up: ")

#calling function
Lookup(user_input)


# ### Test case:3

# In[25]:


#asking user to enter the word to search
user_input = input("Enter a term to look up: ")

#calling function
Lookup(user_input)


# In[ ]:




