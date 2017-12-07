
# coding: utf-8

# # Assignment 2

# ## Normalizing a Corpus

# 1) Write a program to insert < s > and < /s > tags to delimit sentences. You can start from the tokenization and modify it. Use a simple heuristics such as: a sentence starts with a capital letter and ends with a period. Estimate roughly the accuracy of your program. 

# In[9]:

import regex as re
import sys

text = "Säg, att ni inte har gjort det!"

def tokanize(text):
    text = re.sub('\s+',' ', text) 
    text = re.sub('\s*(\p{P})\s*',r'\1', text)
    text = re.sub('([A-ZÅÄÖa-zöäå0-9][\p{L}\"\:,\- ]+[\.\!\?])', '<s>' + r' \1 ' + '</s>\n', text).lower()
    text = re.sub('[^\P{P}\/]',"", text)
    return text



if __name__ == "__main__":
    #text = sys.stdin.read()
    text = tokanize(text)
    print(text)
           
    


# In[ ]:



