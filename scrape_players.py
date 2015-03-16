import json
import urllib2
from urllib import urlopen


# with open("new1.txt", "r") as myfile:
# 	# blank
# 	print "test"

test = json.load(urllib2.urlopen("http://api.football-data.org/alpha/soccerseasons/354/teams"))


for team in test['teams']:
	print team['_links']['players']['href'], team['code'], team['name']
	
# print data

# http://stackoverflow.com/questions/18931315/typeerror-string-indices-must-be-integers-not-str-working-with-dict

Arsenal = json.load(urllib2.urlopen("http://api.football-data.org/alpha/teams/57/players"))

for team in Arsenal['players']:
	print team['name'], team['dateOfBirth'], team['nationality'], team['position']
	

