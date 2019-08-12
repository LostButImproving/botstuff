import requests, bs4


def makesearchterm(searchstring):
  searchterms = searchstring.split(' ')
  return "&".join(searchterms)
  
def findthedocs(searchterms):
  searchstring = searchterms
  searchterms = makesearchterm(searchstring)
  res = requests.get('https://docs.readthedocs.io/en/stable/search.html?q='+searchterms)
  soup = bs4.BeautifulSoup(res.text, 'html.parser')
  linkElem = soup.find_all('a')
  for a in linkElem[0:min(3, len(linkElem))]:
    print("Found the URL:", a['href'])

findthedocs('Build and pie')

