from bs4 import BeautifulSoup
import urllib2
from urllib import urlopen


url = 'http://www.premierleague.com/en-gb/kids/clubs.html'
page = urllib2.urlopen(url)
print page 
soup = BeautifulSoup(page)
# print soup 

for match in soup.select(".clublist .clubs-module"):
	print match 

