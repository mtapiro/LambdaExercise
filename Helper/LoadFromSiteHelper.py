from urllib.request import urlopen
import json

def get_All_Covid_Cases():

    try:

        url = 'https://covid-api.mmediagroup.fr/v1/cases'
        response = urlopen(url)
        jasonString = response.read().decode('utf-8')
        casesJsonData = json.loads(jasonString)

        return casesJsonData
    except:
        return "Bad response from get_All_Covid_Cases"
    
def get_HistoryRecoverd_ByAllCountries():

    try:

        baseURL4RecoveradeData = 'https://covid-api.mmediagroup.fr/v1/history?country=All&status=Recovered'
        response4Recovered = urlopen(baseURL4RecoveradeData)
        # Convert bytes to string type and string type to dict
        jasonRecoveredString = response4Recovered.read().decode('utf-8')

        myRecoveredJsonData = json.loads(jasonRecoveredString)
        return myRecoveredJsonData
    except:
        return "Bad response from get_HistoryRecoverd_ByAllCountries"