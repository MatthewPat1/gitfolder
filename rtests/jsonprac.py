import json
def jsonRun():
    
    jsonString = '{ "key1" : "value1", "key2" : "value2", "key3" : "value3" }'
    jsDict = json.loads(jsonString)
    print(jsDict['key2'])
    with open('C:/Users/Matthew/Desktop/gitfolderT/gitpractice/fileMain/testfiles/text.txt', 'w+') as f:
        jsDump = json.dumps(jsDict)
        json.dump(jsDict, f)
        print(jsDump)
jsonRun()
