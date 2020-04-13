import pandas as pd
df = pd.read_csv('http://api.covid19india.org/states_daily_csv/confirmed.csv')   
df.to_csv('Data/3.1_State_Confirmed_cases.csv')
df = pd.read_csv('https://api.covid19india.org/states_daily_csv/deceased.csv')   
df.to_csv('Data/3.3_State_Deceased_cases.csv')
df = pd.read_csv('https://api.covid19india.org/states_daily_csv/recovered.csv')   
df.to_csv('Data/3.2_State_Recovered_cases.csv')