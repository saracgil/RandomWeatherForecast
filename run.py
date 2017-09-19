# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 21:08:34 2017

@author: ihsan
"""

#import urllib
#from bs4 import BeautifulSoup

import fetch_data
from markov_python.cc_markov import MarkovChain

text = fetch_data.get_forecast()
#print (text)

mc=MarkovChain()
mc.add_string(text)

mctext=mc.generate_text()

#Formatting the text

def formatting(strlist): 
    new_strlist=[]
    days=['monday','tuesday','wednesday','thursday','friday','saturday','sunday']
    ampm=['am','pm']
    no_comma=['to','mph','percent']
    strlist[0]=strlist[0].capitalize() #cap first word
    for item in strlist:
        if item.isdigit()==False: #check if it is a number
            if item in days:  #capitalize days
                new_strlist.append(item.capitalize())
            elif item[-2:] in ampm:
                new_strlist.append(item+",")
            else:
                new_strlist.append(item)
        else:
            item_index=strlist.index(item)
            if strlist[item_index+1] in no_comma:
                new_strlist.append(item)
            else:
                new_strlist.append(item+";")
        new_str=" ".join(new_strlist) 
        new_str="Here is the weather forecast: " + new_str+"."
    return new_str

ftext=formatting(mctext)
print(ftext)

