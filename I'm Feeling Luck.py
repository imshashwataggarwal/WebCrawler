#! python
# I'm Feeling Lucky.py - Opens several Google search results.

import sys, requests, webbrowser, bs4, pyperclip
print 'Googling...'

if len(sys.argv) > 1:
    # Get address from command line.
    address = ' '.join(sys.argv[1:])

else:
    #Get address from clipboard.
    address = pyperclip.paste()
    
res  = requests.get('http://google.com/search?q=' + address)
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text,"html.parser")
links = soup.select('.r a')

tabs = min(5,len(links))
for i in xrange(tabs):
    webbrowser.open('http://google.com' + links[i].get('href'))
