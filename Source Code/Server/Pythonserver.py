import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import requests
import json
import csv
cred = credentials.Certificate(
    'testcloudfunction-39eee-firebase-adminsdk-vyrui-64fb286917.json')
firebase_admin.initialize_app(cred)


def Countrypush(data):
    country_ref = db.collection('Country')
    for i in data:
        country_ref.document(i['country']).set({
            'updated': i['updated'],
            'country': i['country'],
            'countryInfo': i['countryInfo'],
            'lat': i['countryInfo']['lat']	,
            'long': i['countryInfo']['long'],
            'flag': i['countryInfo']['flag'],
            'cases': i['cases']	,
            'todayCases': i['todayCases']	,
            'deaths': i['deaths']	,
            'todayDeaths': i['todayDeaths'],
            'recovered': i['recovered'],
            'active': i['active'],
            'critical': i['critical'],
            'casesPerOneMillion': i['casesPerOneMillion'],
            'deathsPerOneMillion': i['deathsPerOneMillion'],
            'tests': i['tests'],
            'testsPerOneMillion': i['testsPerOneMillion'],
        })


def Statepush(data):
    State_ref = db.collection('Country').document('India').collection('States')
    for i in data:
        State_ref.document(i['state']).set({
            'active': str(i['active']),
            'confirmed': str(i['confirmed'])	,
            'deaths': str(i['deaths']),
            'deltaconfirmed': str(i['deltaconfirmed']),
            'deltadeaths': str(i['deltadeaths'])	,
            'deltarecovered': str(i['deltarecovered']),
            'lastupdatedtime': str(i['lastupdatedtime'])	,
            'recovered': str(i['recovered']),
            'statecode': str(i['statecode'])
        })


def Districtpush(data):
    State_ref = db.collection('Country').document('India').collection('States')
    for st in data:
        for i in st['districtData']:
            State_ref.document(st['state']).collection(i['district']).add({
                'confirmed': i['confirmed'],
                'todayconfirmed': i['delta']['confirmed']
            })


def Worldpush(data):
    World_ref = db.collection('Country').document('World')
    World_ref.set({
        'updated':data['updated'],
        'cases':data['cases'],	
        'todayCases':data['todayCases'],
        'deaths':data['deaths'],
        'todayDeaths':data['todayDeaths'],
        'recovered':data['recovered'],
        'active':data['active'],
        'critical':data['critical'],	
        'casesPerOneMillion':data['casesPerOneMillion'],
        'deathsPerOneMillion':data['deathsPerOneMillion'],
        'tests':data['tests'],
        'testsPerOneMillion':data['testsPerOneMillion'],
        'affectedCountries':data['affectedCountries'],
    })

def WorldTimeSeriesPush(data):
    World_time_ref=db.collection('Country')
    for i in data:
        if(i!='India'):
            for j in data[i]:
                World_time_ref.document(i).collection('Timeseries').document(j['date']).set({
                    'date':j['date'],
                    'confirmed':j['confirmed'],
                    'deaths':j['deaths'],
                    'recovered':j['recovered']
            })
def IndianTimeSeriesPush(data):
    indian_time_ref=db.collection('Country').document('India')
    for i in data:
        indian_time_ref.collection('timeSeries').document(i['date']).set({
            'dailyconfirmed':i['dailyconfirmed'],
            'dailydeceased':i['dailydeceased'],
            'dailyrecovered':i['dailyrecovered'],
            'date':i['date'],
            'totalconfirmed':i['totalconfirmed'],
            'totaldeceased':i['totaldeceased'],
            'totalrecovered':i['totalrecovered']
        })

db = firestore.client()
World_data = requests.get(url='https://corona.lmao.ninja/all')
Countries_data = requests.get(url="https://corona.lmao.ninja/countries")
States_Data = requests.get(url="https://api.covid19india.org/data.json")
district_Data = requests.get(url="https://api.covid19india.org/v2/state_district_wise.json")
World_time_series=requests.get(url="https://pomber.github.io/covid19/timeseries.json")
World_data = World_data.json()
Worldpush(World_data)
Country_data = Countries_data.json()
Countrypush(Country_data)
State_data = States_Data.json()
Statepush(State_data['statewise'])
district_Data = district_Data.json()
Districtpush(district_Data)
World_time_series = World_time_series.json()
WorldTimeSeriesPush(World_time_series)
IndianTimeSeriesPush(State_data['cases_time_series'])
