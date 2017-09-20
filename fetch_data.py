# -*- coding: utf-8 -*-
"""
Created on Sun Sep 10 20:40:56 2017

@author: ihsan
"""

import urllib
from bs4 import BeautifulSoup

def get_forecast():
    # first scrape the weather forecast
    path='http://forecast.weather.gov/MapClick.php?'
    req = urllib.request.Request(path+'lat=40.6925&lon=-73.9904')
    # loop over lat and lon to scrape more pages
    with urllib.request.urlopen(req) as response:
        the_page = response.read()
    #define it as BeautifulSoup object
    soup = BeautifulSoup(the_page,'html.parser')
    #Use Chrome Developer Tools to identify the html class and id that contain \
    #useful information.  In this case id = seven-day-forecast and underneath \
    #class = tombstone-container are useful
    seven_day = soup.find(id='seven-day-forecast') 
    forecast_items = seven_day.find_all(class_='tombstone-container') #each day listed
    descriptions=[]
    for item in forecast_items:
        img=item.find('img') 
        descriptions.append(img['title'])
    # Alternative list comprehension method using select (need to higher level)
    #descr = [d['title'] for d in seven_day.select('.tombstone-container img')]
    forecast=" ".join(descriptions) #convert to string 
    return forecast #return the string 

