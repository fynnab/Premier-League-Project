import os
import sys
import django
from teams.models import clubs

def add_players(name, club, position, born, height, weight, nationality, active=True):
	# run the script per club
	club1 = "Arsenal" 
	club2 = clubs.objects.get(name = club1);
	p = players.objects.get_or_create(name=name, club=club2, position=position, born=born, height=height, weight=weight, nationality=nationality)
	return p

def populate():
	add_players(name='Calum Chambers',
		position = 'DEF', # list
		born = '2015-01-20',
		height = '1.83',
		weight = '65',
		nationality = 'England'
		) 

	for p in players.objects.all():
		print p 


if __name__ == '__main__':
	print "Starting player population script..."
	os.environ.setdefault("DJANGO_SETTINGS_MODULE", "epl.settings")
	django.setup()
	from teams.models import players
	populate()


# # add_players(name='',
# 		club = '',
# 		position = '', # list
# 		born = '',
# 		height = '',
# 		weight = '',
# 		nationality = ''
# 		)