import urllib.request
import json

#Return HTML 
def connectEthernet():
    url = urllib.request.urlopen('https://github.com')
    if url.getcode() == 200:
        dates = url.read()
        print(dates)


#connectEthernet()        

#Know about earthquakes just after they happen
def manipulationJson():
    address = 'https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson'
    webUrl = urllib.request.urlopen(address)
    if(webUrl.getcode() == 200):
        dados = webUrl.read()
        objJson = json.loads(dados)

        count = objJson['metadata']['count']
        print('Count:' + str(count))

        for location in objJson['features']:
            print(location['properties']['place'])

manipulationJson()            