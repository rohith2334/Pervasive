    # -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 23:33:24 2020

@author: rohith
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 23:12:06 2020

@author: rohith
"""
import requests
import json
import csv
india_series_list=['patientnumber','statecode','statepatientnumber','gender','agebracket','typeoftransmission','dateannounced','contractedfromwhichpatientsuspected','nationality','detectedstate','detectedcity','detecteddistrict',
                   'backupnotes','notes','currentstatus','statuschangedate''estimatedonsetdate',
                   'source1','source2','source3'
                   ]
templist=[]
india_series=requests.get(url="https://api.covid19india.org/raw_data.json")
data=india_series.json()
for i in data['raw_data']:
    lst=[]
    lst.append(i['patientnumber'])
    lst.append(i['statecode'])
    lst.append(i['statepatientnumber'])
    lst.append(i['gender'])
    lst.append(i['agebracket'])
    lst.append(i['typeoftransmission'])
    lst.append(i['dateannounced'])
    lst.append(i['contractedfromwhichpatientsuspected'])
    lst.append(i['nationality'])
    lst.append(i['detectedstate'])
    lst.append(i['detectedcity'])
    lst.append(i['detecteddistrict'])
    lst.append(i['backupnotes'])
    lst.append(i['notes'])
    lst.append(i['currentstatus'])
    lst.append(i['statuschangedate'])
    lst.append(i['estimatedonsetdate'])
    lst.append(i['source1'])
    lst.append(i['source2'])
    lst.append(i['source3'])
    templist.append(lst)
with open('Data/5_Indian_Patients_data.csv', 'w',newline='') as csvfile:  
    # creating a csv writer object  
    csvwriter = csv.writer(csvfile)  
        
    # writing the fields  
    csvwriter.writerow(india_series_list)  
        
    # writing the data rows  
    csvwriter.writerows(templist) 
