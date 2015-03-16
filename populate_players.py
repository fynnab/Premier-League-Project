import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "epl.settings")

import json
import urllib2
from urllib import urlopen
import sys
import httplib 
import django
django.setup()

# from django.conf import settings 
# settings.configure(DEBUG=True, TEMPLATE_DEBUG=True,
#     TEMPLATE_DIRS=('/home/web-apps/teams', '/home/web-apps/base'))

from teams.models import clubs, players

club1 = "Queens Park Rangers"

club2 = clubs.objects.get(name = club1);

def add_players(name, position, born, nationality, club, active=True):
	# run the script per club
	
	p = players.objects.get_or_create(name=name, position=position, born=born, nationality=nationality, club=club)
	return p



txdata = None
txheaders = {   
    'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',
    'Accept-Language': 'en-us',
    'Accept-Encoding': 'gzip, deflate, compress;q=0.9',
    'Keep-Alive': '300',
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'X-Auth-Token': '9547fbfd97d943c09f38e0321a6b73ad'
}


url = "http://api.football-data.org/alpha/teams/69/players"
req = urllib2.Request(url, txdata, txheaders)
Arsenal = json.load(urllib2.urlopen(req))

def populate():
	for team in Arsenal['players']:
		name1 = team['name']
		position1 = team['position']
		born1 = team['dateOfBirth']
		nationality1 = team['nationality'] 
		
		add_players(
			name = name1,
			position = position1,
			born = born1,
			nationality = nationality1,
			club = club2
			) 


				

if __name__ == '__main__':
	print "Starting player population script..."
	django.setup()
	populate()
	print players.objects.all()

# # add_players(name='',
# 		club = '',
# 		position = '', # list
# 		born = '',
# 		height = '',
# 		weight = '',
# 		nationality = ''
# 		)