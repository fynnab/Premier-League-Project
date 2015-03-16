import json
import urllib2
from urllib import urlopen


f = open("new1.txt", "w") 

test = json.load(urllib2.urlopen("http://api.football-data.org/alpha/soccerseasons/354/teams"))

with f as file:
	json.dump(test, file, sort_keys = True, indent = 4)

f.close()


# http://www.football-data.co.uk/englandm.php
# http://www.jokecamp.com/blog/guide-to-football-and-soccer-data-and-apis/