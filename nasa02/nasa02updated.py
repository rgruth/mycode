#!/usr/bin/env python2
import requests 
def main():
    neourl = 'https://api.nasa.gov/neo/rest/v1/feed?'
    startdate = 'start_date=2018-06-01'
    enddate = '&end_date=END_DATE'
    mykey = '&api_key=DEMO_KEY'
    neourl = neourl + startdate + mykey
    neojson = (requests.get(neourl)).json()
    print(neojson)
main()
