import sys
from PyQt4.QtGui import QApplication
from PyQt4.QtCore import QUrl
from PyQt4.QtWebkit import QWwebpage
import bs4
import requests
import urllib.request

class Client(QWebPage):
  def __init__(self, url):
    self.app = QApplication(sys.argv)
    QWebPage.__init__(self)
    self.LoadFinished.connect(self.on_page_load)
    self.mainFrame().load(QUrl(url))
    self.app.exec_()
  
  def on_page_load(self):
    self.app.quit()
url = 'https://pythonprogramming.net/parsememcparseface/'
client_response = Client(url)
source = client_response.mainFrame().toHtml()
soup = bs4.BeautifulSoup(source,'lxml')
js_test = soup.find('p', class_= 'jstest')
print(js_test)


#konvertere til søgestreng som kan bruges i GET requests

#def makesearchterm(searchstring):
#  searchterms = searchstring.split(' ')
#  return "&".join(searchterms)
#  
# 
#def findthedocs(searchterms):
#  searchstring = searchterms
#  searchterms = makesearchterm(searchstring)
#   #udfører GET requests og scraper
#  #res = requests.get('https://docs.readthedocs.io/en/stable/search.html?q='+searchterms)
#  
#
#  soup = bs4.BeautifulSoup(res.text, 'html.parser')
#  #Kan ikke ramme elementet som indeholder søgeresultater, få hjælp
#  linkElem = soup.find_all('a')
#  #printer maks 3 resultater
#  for a in linkElem[0:min(3, len(linkElem))]:
#    print("Found the URL:", a.get_text(), a['href'])
#
#findthedocs('Build and pie')

