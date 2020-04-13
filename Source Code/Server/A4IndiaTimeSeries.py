# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 22:43:14 2020

@author: rohith
"""
import requests
import json
import csv
india_series_list=['Date','dailyconfirmed','dailydeceased','dailyrecovered','totalconfirmed','totaldeceased','totalrecovered']
templist=[]
india_series=requests.get(url="https://api.covid19india.org/data.json")
data=india_series.json()
for i in data['cases_time_series']:
    lst=[]
    lst.append(i['date'])
    lst.append(int(i['dailyconfirmed']))
    lst.append(int(i['dailydeceased']))
    lst.append(int(i['dailyrecovered']))
    lst.append(int(i['totalconfirmed']))
    lst.append(int(i['totaldeceased']))
    lst.append(int(i['totalrecovered']))
    templist.append(lst)
with open('Data/2_India_TimeSeries.csv', 'w',newline='') as csvfile:  
    # creating a csv writer object  
    csvwriter = csv.writer(csvfile)  
        
    # writing the fields  
    csvwriter.writerow(india_series_list)  
        
    # writing the data rows  
    csvwriter.writerows(templist) 
