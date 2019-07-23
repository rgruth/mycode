#!/usr/bin/env python3
import urllib.request
import json
neourl = 'https://api.nasa.gov/neo/rest/v1/feed?'
startdate = 'start_date=2018-06-01'
enddate = '&end_date=END_DATE'
mykey = '&api_key=gmVEi8Z3UeV7zJWVFmEfuGnQ1TY8FThdC7YzceEg'
neourl = neourl + startdate + mykey
neourlobj = urllib.request.urlopen(neourl)
neoread = neourlobj.read()
decodeneo = json.loads(neoread.decode('utf-8'))
print("\n\nConverted python data")
print(decodeneo)

