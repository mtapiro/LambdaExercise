from lambda_function import lambda_handler
import json

event1 = '{"function": "Top5MostRecoveredCountry"}'
event2 = '{"function": "avgConfirmedPer100Squar"}'
event3 = '{"function": "Top10RecoveredCountry4Graph"}'
event4 = '{"function": "NotExistFunc"}'

jsonEvent = json.loads(event4)

demoResponse = lambda_handler(jsonEvent, "ff")
print(demoResponse)
end = ''