#region import
import json
from json import JSONEncoder
import math
from datetime import datetime, timedelta
from urllib.request import urlopen
from Helper.LoadFromSiteHelper import get_All_Covid_Cases,get_HistoryRecoverd_ByAllCountries
from Helper.ProjHelper import prepreJsonResponse
from Helper.SQLHelper import Open_SQL_InsertRecords
#endregion

class MostRecoveredObj (object):
    def __init__(self, countryname, recovered):
        self.val = recovered
        self.countryname = countryname

def sortMyRecoveredList(my5ObjList, record2check):

    if record2check.val == "NA":
        return my5ObjList

    minRecord = my5ObjList[-1] #min record in top5 list
    if minRecord.val > record2check.val: #if nothing need to replace
        return my5ObjList
    else:
        my5ObjList.remove(minRecord)
        my5ObjList.append(record2check)
        func = lambda x: x.val
        my5ObjList = sorted(my5ObjList, key=func, reverse = True)

        return my5ObjList

def calc_RecoveredLast10Days(record_Recovered,record_CasesData, lastXdays):

    try:
        Today_Recovered = record_CasesData["All"]["recovered"]

        N_DAYS_AGO = lastXdays
        LastXDays_Date = datetime.today() - timedelta(days=N_DAYS_AGO)
        LastXDays_Date = LastXDays_Date.strftime("%Y-%m-%d")
        LastXDays_Recovered = record_Recovered["All"]["dates"][LastXDays_Date]

    except:
        totalXDays_Recovered = "NA"
        return totalXDays_Recovered

    totalXDays_Recovered = Today_Recovered - LastXDays_Recovered
    return totalXDays_Recovered

def X_MostRecoveredCountry(TopX_Country,lastX_Days,isGrafical):

    casesJsonData = get_All_Covid_Cases()

    myRecoveredJsonData = get_HistoryRecoverd_ByAllCountries()

    topX_Country = []

    print("Start Analyze population..")

    for record in myRecoveredJsonData:
        if record != "Global":
            val = calc_RecoveredLast10Days(myRecoveredJsonData[record],casesJsonData[record],lastX_Days)

            if len(topX_Country) < TopX_Country:
                candidateRecord = MostRecoveredObj(record, val)
                topX_Country.append(candidateRecord)
                topX_Country = sortMyRecoveredList(topX_Country, candidateRecord)

            elif len(topX_Country) == TopX_Country:
                candidateRecord = MostRecoveredObj(record, val)
                topX_Country = sortMyRecoveredList(topX_Country, candidateRecord)

    if isGrafical:
        Open_SQL_InsertRecords(topX_Country)


    return (prepreJsonResponse(topX_Country))


