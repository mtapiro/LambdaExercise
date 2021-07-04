# LambdaExercise
This Python project expose AWS Lambda that response back to user with 3 Covid API's:

1. https://prp7sz6w1d.execute-api.us-east-2.amazonaws.com/Test/covidresource?function=Top5MostRecoveredCountry
   Response back with Top(5) countries with most recovered in last 10 Days

2. https://prp7sz6w1d.execute-api.us-east-2.amazonaws.com/Test/covidresource?function=avgConfirmedPer100Squar 
    Response back with avg confirmed cases per 100 square KM per country since pandemic began.

3. https://prp7sz6w1d.execute-api.us-east-2.amazonaws.com/Test/covidresource?function=Top10RecoveredCountry4Graph
    Response back with Top(10) contries recovered cases in the last 7 Days.
