#!/usr/bin/env python3
#ipchk = '192.168.0.1'
ipchk = input('Apply an IP address: ') 
if ipchk: # if any data is provided, this will test true
    print('Looks like the IP address was set: ' + ipchk) # indented under if 
elif ipchk: # if any data is provided, this will test true
    print('Looks like the IP address was set: ' + ipchk) # indented under if
else: # if data is NOT provided
    print('You did not provide input.') # indented under else

