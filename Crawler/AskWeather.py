#! python 2
'''
   Weather.py - Launches a weather website in the browser
   depending upon user choice.
'''

import webbrowser,sys,os

while True:
    place = raw_input('>>> Enter Place : ')
    address = 'https://www.google.co.in/?gws_rd=ssl#q=weather+in+'+place
    print ' 1.) Google Weather'
    print ' 2.) Exit'
    choice = input('>>> Enter your Chice : ')
    if choice == 2:
        sys.exit()
    print
    webbrowser.open(address)
    os.system('cls')
    
