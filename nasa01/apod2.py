#!/usr/bin/env python3
import urllib.request
import json
import webbrowser
from pprint import pprint as pp
NASAAPI = 'https://api.nasa.gov/planetary/apod?'
MYKEY = 'api_key=gmVEi8Z3UeV7zJWVFmEfuGnQ1TY8FThdC7YzceEg'
def main():
    nasaapiobj = urllib.request.urlopen(NASAAPI + MYKEY) 
    nasaread = nasaapiobj.read()
    convertedjson = json.loads(nasaread.decode('utf-8'))
    print(convertedjson)
    input('\nThis is converted json. Press ENTER to continue.')
    pp(convertedjson)
    input('\nThis is pretty printed JSON. Press ENTER to continue.')
    print(convertedjson['explanation'])
    input('\nPress ENTER to view this photo of the day')
    webbrowser.open(converted.json['hdurl'])
