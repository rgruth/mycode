#!/usr/bin/env python3
import urllib.request
import json
import webbrowser

apodurl = 'https://api.nasa.gov/planetary/apod?'
mykey = 'api_key=gmVEi8Z3UeV7zJWVFmEfuGnQ1TY8FThdC7YzceEg'
apodurlobj = urllib.request.urlopen(apodurl + mykey)
apodread = apodurlobj.read()
decodeapod = json.loads(apodread.decode('utf-8'))
print("\n\nConverted python data")
print(decodeapod)
input('\nPress Enter to open NASA Picture of the Day in FireFox')
webbrowser.open(decodeapod['url'])

