# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 23:03:41 2020

@author: rohith
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 22:43:14 2020

@author: rohith
"""
import requests
import json
import csv
india_series_list=['State','Statecode','confirmed','active','recovered','deaths','today confirmed','today recovered','today death','update time']
templist=[]
india_series=requests.get(url="https://api.covid19india.org/data.json")
data=india_series.json()
for i in data['statewise']:
    lst=[]
    lst.append(i['state'])
    lst.append(i['statecode'])
    lst.append(int(i['confirmed']))
    lst.append(int(i['active']))
    lst.append(int(i['recovered']))
    lst.append(int(i['deaths']))
    lst.append(int(i['deltaconfirmed']))
    lst.append(int(i['deltarecovered']))
    lst.append(int(i['deltadeaths']))
    lst.append(i['lastupdatedtime'])
    templist.append(lst)
with open('Data/3.1_States_Status_Data.csv', 'w',newline='') as csvfile:  
    # creating a csv writer object  
    csvwriter = csv.writer(csvfile)  
        
    # writing the fields  
    csvwriter.writerow(india_series_list)  
        
    # writing the data rows  
    csvwriter.writerows(templist) 
