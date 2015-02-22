from bs4 import BeautifulSoup
import urllib2
from urllib import urlopen


url = 'http://www.premierleague.com/en-gb/kids/clubs.html'
page = urllib2.urlopen(url)
print page 
soup = BeautifulSoup(page)

f = open("new.txt", "w")
for match in soup.select(".clublist .clubs-module"):
    match1 = match.get_text()
    f.write(match1)
    words = match1.split()
    list1 = [word for word in words if 'nickname' in word]
    print list1 


f.close()

