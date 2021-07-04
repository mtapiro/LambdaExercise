import json
from BusinessLogic.CovidRecovered import X_MostRecoveredCountry
from BusinessLogic.ConfirmedCases import avgConfirmedPer100Squar

def lambda_handler(event, context):
   
   #extract parameters from Json or QueryString
   try:
       varFunction2Execute = event['queryStringParameters']['function']
   except:
       varFunction2Execute=event['function']

   myResponse = {}

   myResponse['message'] = FuncDesition(varFunction2Execute)

   responseObj = {}
   responseObj['statusCode'] = 200
   responseObj['headers'] = {}
   #responseObj['headers']['Content-Type'] = 'application/json'
   try:
       responseObj['body'] = myResponse['message']
   except:
        return {
            'statusCode': 400,
            'body': json.dumps('Something bad happened... :( !')
        }

   return responseObj
   
   
def get_5MostRecoveredCountry():
    #first Param = Top X Countries
    #second Param = #Days back
    #Third Param = T/F if need to grafical results
    return X_MostRecoveredCountry(5,10, False)
    
def get_avgConfirmedPer100Squar():
    return avgConfirmedPer100Squar()

def get_10MostRecoveredCountry4Graph():
    # first Param = Top X Countries
    # second Param = #Days back
    # Third Param = T/F if need to grafical results
    return X_MostRecoveredCountry(10, 7, True)

def FuncDesition(funcName):
    errMsg = "This Method is not Supported yet."
    switcher={
        'Top5MostRecoveredCountry': get_5MostRecoveredCountry,
        'avgConfirmedPer100Squar': get_avgConfirmedPer100Squar,
        'Top10RecoveredCountry4Graph': get_10MostRecoveredCountry4Graph
    }
    func = switcher.get(funcName, errMsg)

    if func != errMsg:
        return func()
    else:
        return errMsg


