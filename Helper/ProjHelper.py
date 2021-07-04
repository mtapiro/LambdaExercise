import json

def prepreJsonResponse(top5CountryObj):
#Transform list on objects to valid json string

    jsonTemplate = '"$countryName$": {"countryname": "$countryName$","val": "$val$"}'
    i = 1
    jsonRes = '{'
    for item in top5CountryObj:

        tmp = jsonTemplate.replace("$countryName$", item.countryname).replace('$val$', str(item.val))
        if len(top5CountryObj) != i:
            jsonRes += f'{tmp},'
        else:
            jsonRes += tmp + '}'
        i += 1

    return jsonRes