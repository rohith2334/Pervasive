# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 10:11:06 2020

@author: rohith
"""
import requests
import json
import csv
columns=['country','todayCases','todayDeaths','cases','active','recovered',
         'critical','deaths','totalTests','casesPerOneMillion',
         'deathsPerOneMillion','testsPerOneMillion']
templist=[]
india_series=requests.get(url="https://coronavirus-19-api.herokuapp.com/countries")
data=india_series.json()
for i in data:
    lst=[]
    lst.append(i['country'])
    lst.append(i['todayCases'])
    lst.append(i['todayDeaths'])
    lst.append(i['cases'])
    lst.append(i['active'])
    lst.append(i['recovered'])
    lst.append(i['critical'])
    lst.append(i['deaths'])
    lst.append(i['totalTests'])
    lst.append(i['casesPerOneMillion'])
    lst.append(i['deathsPerOneMillion'])
    lst.append(i['testsPerOneMillion'])
    templist.append(lst)
with open('Data/1_All_Countries_Data.csv', 'w',newline='') as csvfile:  
    # creating a csv writer object  
    csvwriter = csv.writer(csvfile)  
        
    # writing the fields  
    csvwriter.writerow(columns)  
        
    # writing the data rows  
    csvwriter.writerows(templist) 