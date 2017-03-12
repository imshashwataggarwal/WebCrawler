#! python 2
'''
   Weather.py - Launches a weather website in the browser
   depending upon user choice.
'''

import webbrowser,sys,os
address = {
            1:  'https://www.google.co.in/?gws_rd=ssl#q=weather',
            2:  'http://www.accuweather.com/en/in/delhi/202396/weather-forecast/202396',
            3:  'https://weather.com/en-IN/weather/10day/l/INXX0096:1:IN'
          }
while True:
    print ' 1.) Google Weather'
    print ' 2.) AccuWeather'
    print ' 3.) Weather.com'
    print ' 4.) Exit'
    choice = input('>>> Enter your Chice : ')
    if choice == 4:
        sys.exit()
    if address.get(choice,0) == 0:
        print 'Invalid Choice, Please Try Again.'         
        continue
    webbrowser.open(address[choice])
    os.system('cls')
    
    
