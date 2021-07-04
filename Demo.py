from lambda_function import Covid19_handler
import json

event1 = '{"function": "Top5MostRecoveredCountry"}'
event2 = '{"function": "avgConfirmedPer100Squar"}'
event3 = '{"function": "Top10RecoveredCountry4Graph"}'
event4 = '{"function": "NotExistFunc"}'

jsonEvent = json.loads(event3)

demoResponse = Covid19_handler(jsonEvent, "ff")
print(demoResponse)
end = ''