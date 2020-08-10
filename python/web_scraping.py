#import webbrowser
import sys
import requests
import bs4


#webbrowser.open('https://antenneakiba.podigee.io/about')
sys.argv
res = requests.get('https://antenneakiba.podigee.io/about')
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text, 'html.parser')
elems = soup.select('#blog > div.section-main > div')
print(elems[0].text.strip())
