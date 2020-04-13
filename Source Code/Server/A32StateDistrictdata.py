# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 23:12:06 2020

@author: rohith
"""

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
india_series_list=['State','district','total confirmed','today confirmed']
templist=[] 
india_series=requests.get(url="https://api.covid19india.org/v2/state_district_wise.json ")
data=india_series.json()
for st in data:
    for i in st['districtData']:
        lst=[]
        lst.append(st['state'])
        lst.append(i['district'])
        lst.append(int(i['confirmed']))
        lst.append(int(i['delta']['confirmed']))
        templist.append(lst)
with open('Data/4_State_District_data.csv', 'w',newline='') as csvfile:  
    # creating a csv writer object  
    csvwriter = csv.writer(csvfile)  
        
    # writing the fields  
    csvwriter.writerow(india_series_list)  
        
    # writing the data rows  
    csvwriter.writerows(templist) 
