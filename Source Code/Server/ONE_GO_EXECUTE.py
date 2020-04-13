# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 00:17:05 2020

@author: rohith
"""
import A1ALLCountriesData
import A21CountryWiseConfirmed
import A22CountryWiseDead
import A23CountryWiseRecovered
import A31StateStatus
import A32StateDistrictdata
import A4IndiaTimeSeries
import A5StateTimeSeriesChanges
import A6IndianPatientsdata


from datetime import datetime
now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
date="date:\t"+dt_string[:10]+"\n"
time="time:\t"+dt_string[11:]+"\n"
f= open("LastUpdated.txt","w+")
f.write(date)
f.write(time)
f.close()