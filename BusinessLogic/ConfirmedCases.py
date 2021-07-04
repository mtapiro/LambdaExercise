#region import
import json
import math
from datetime import datetime, timedelta
from urllib.request import urlopen
from Helper.LoadFromSiteHelper import get_All_Covid_Cases
#endregion

class avgConfirmedObj (object):
    def __init__(self, countryname, confirmed, totalAreaInKM):
        self.countryname = countryname
        self.confirmed = confirmed
        self.sk_km_area = totalAreaInKM

def avgConfirmedPer100Squar():
    
    casesJsonData = get_All_Covid_Cases()

    avgConfirmedByCountry = []

    print("Start Analyze population..")

    #region Read All Data and fill Confirmed Obj
    for record in casesJsonData:
        if record != "Global":
            country = record
            try:
                confirmed = casesJsonData[record]["All"]["confirmed"]
            except KeyError:
                confirmed='NA'
            try:
                km_area = casesJsonData[record]["All"]["sq_km_area"]
            except KeyError:
                km_area='NA'
            avgConfirmedByCountry.append(avgConfirmedObj(country,confirmed,km_area))
    #endregion

    res_str = ''
    print("avg Confirmed cases per 100KM")

    return calc_CasesPer100kms(avgConfirmedByCountry)
    #return res_str


def calc_CasesPer100kms(CountriesList):

    # region Go Over all Countries, calc cases per 100[skm]

    res_str = ''
    for record in CountriesList:
        try:
            val_100squareKM = record.sk_km_area/100 #need to calc cases per 100skm
            confirmedCasses_Per100KM = int(round(record.confirmed/val_100squareKM))
        except:
            confirmedCasses_Per100KM = "NA"

        if record.countryname == CountriesList[-1].countryname:
            res_str += f'{record.countryname}:  {confirmedCasses_Per100KM} cases/100[skm]'
        else:
            res_str += f'{record.countryname}:  {confirmedCasses_Per100KM} cases/100[skm]\n'


    return res_str
    # endregion