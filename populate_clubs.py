import os
import sys
import django

# note - probably a more efficient way to do this here: https://docs.djangoproject.com/en/1.7/howto/custom-management-commands/

# for loop to take data from file and put into add_club function
f = open("new.txt", "r")


f.close()


def add_club(name, nickname, manager, established, stadium, active=True):
	c = clubs.objects.get_or_create(name=name, nickname=nickname, manager=manager, established=established, stadium=stadium, active=active)
	return c

def populate():
	add_club(name = "Aston Villa",
		nickname = "Villans",
		manager = "Tim Sherwood",
		established = "1897",
		stadium = "Villa Park"
		)

	# Print out what was added
	for c in clubs.objects.all():
		print c



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

