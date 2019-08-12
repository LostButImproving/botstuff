import requests, bs4

  #konvertere til søgestreng som kan bruges i GET requests 
def makesearchterm(searchstring):
  searchterms = searchstring.split(' ')
  return "&".join(searchterms)
  
 
def findthedocs(searchterms):
  searchstring = searchterms
  searchterms = makesearchterm(searchstring)
   #udfører GET requests og scraper
  res = requests.get('https://docs.readthedocs.io/en/stable/search.html?q='+searchterms)
  

  soup = bs4.BeautifulSoup(res.text, 'html.parser')
  #Kan ikke ramme elementet som indeholder søgeresultater, få hjælp
  linkElem = soup.find_all('a')
  #printer maks 3 resultater
  for a in linkElem[0:min(3, len(linkElem))]:
    print("Found the URL:", a.get_text(), a['href'])

findthedocs('Build and pie')

