import json
import urllib2
from urllib import urlopen
import mechanize 

br = mechanize.Browser()
br.open("http://api.football-data.org")
request = br.request
print request.header_items()


# test = json.load(urllib2.urlopen("http://api.football-data.org/alpha/soccerseasons/354/teams"))

# Dict = {}
# for team in test['teams']:
# 	# print team['_links']['players']['href'], team['name']

# 	Dict['url'] = team['_links']['players']['href']
# 	Dict['name'] = team['name']

# print Dict