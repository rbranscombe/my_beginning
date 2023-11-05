#!/usr/bin/env python3
#nextbus.py

import sys


#print('Command line options:', sys.argv)
##modify code to read user inputs for the bus number and route number from unix command line #- use sys.argv to do this
##raise SystemExit(0) #stops code from execuing at this point

if len(sys.argv) != 3:       #modify code to add check that user has input all required data for bus route and bus id and file
    raise SystemExit('Usage: nextbus.py route stopid')

route = sys.argv[1]  
stopid = sys.argv[2]

import urllib.request

u = urllib.request.urlopen('http://ctabustracker.com/bustime/map/getStopPredictions.jsp?route={}&stop={}'.format(route,stopid)) #use Chicago city bus tracker stop prediction software to query user input stop and route using format() method

data = u.read()   #get back raw data which is a xml fragment
#print('Response:', data) #used for debugging

from xml.etree.ElementTree import XML  #import XML handler to breakout data from raw code 
doc = XML(data)

#import pdb; pdb.set_trace() #launch debugger

for pt in doc.findall('.//pt'):   #noticced wait times always prefaced by pt if you use intepreter to look at text
    print(pt.text)

      
