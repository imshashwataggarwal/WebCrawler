#! python
# Amazon Top Search.py - Opens several Google search results.

import sys, requests, webbrowser, bs4, pyperclip
print 'Finding...'

'''
if len(sys.argv) > 1:
    # Get address from command line.
    address = ' '.join(sys.argv[1:])

else:
    #Get address from clipboard.
    address = pyperclip.paste()
'''
address = raw_input()
res  = requests.get('http://www.amazon.in/s/ref=nb_sb_noss_1?url=search-alias%3Daps&field-keywords=' + address)
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text,"html.parser")
links = soup.select('a [class = "a-link-normal s-access-detail-page a-text-normal"]')

tabs = min(5,len(links))
for i in xrange(tabs):
    webbrowser.open(links[i].get('href'))

