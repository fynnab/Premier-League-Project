import os
import sys
import django
import json
import urllib2
from urllib import urlopen

def add_club(name, active=True):
	c = clubs.objects.get_or_create(name=name, active=active)
	return c

club_object = json.load(urllib2.urlopen("http://api.football-data.org/alpha/soccerseasons/354/teams"))

def populate():
	for club_name in club_object['teams']:
		name1 = club_name['name']

		add_club(name = name1
			)

		# Print out what was added
		print clubs.objects.all()
		



# Start execution
if __name__ == '__main__':
	print "Starting club population script..."
	os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'epl.settings')
	django.setup()
	from teams.models import clubs
	populate()





	# add_club (name="",
	# 	nickname ="",
	# 	manager = "",
	# 	established = "",
	# 	stadium = "",
	# 	active = True )

	# add_club (name='',
	# 	nickname ='',
	# 	manager = '',
	# 	established = '',
	# 	stadium = '',
	# 	active = True )

