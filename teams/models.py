from django.db import models

# Create your models here.

class clubs(models.Model):
	name = models.CharField(max_length=64)
	nickname = models.CharField(max_length=64)
	logo = models.ImageField(blank=True)
	manager = models.CharField(max_length=128)
	established = models.IntegerField()
	stadium = models.CharField(max_length=64)
	active = models.BooleanField(default=True)

	# Fixtures, form, league position?

	def __unicode__(self):
		return self.name 


class players(models.Model):
	GOALKEEPER = 'GK'
	DEFENDER = 'DEF'
	MIDFIELDER = 'MID'
	FORWARD = 'FWD'
	POSITION_CHOICES = (
		(GOALKEEPER, 'Goalkeeper'),
		(DEFENDER, 'Defender'),
		(MIDFIELDER, 'Midfielder'),
		(FORWARD, 'Forward'),
		)

	name = models.CharField(max_length=64)
	club = models.OneToOneField('clubs', related_name= "team")
	position = models.CharField(max_length=64, choices=POSITION_CHOICES, default=GOALKEEPER) # GK, Defender, Midfielder, Attacker -  Field for this? 
	born = models.DateField()
	height = models.DecimalField(max_digits=3, decimal_places=2)
	weight = models.IntegerField() # Field for this?
	nationality = models.CharField(max_length=64) # Choices
	active = models.BooleanField(default=True) # active = current epl player
	slug = models.SlugField()

	def __unicode__(self):
		return self.name 


	
# class playerStats(models.Model):
# 	name = models.ManyToManyField('players')
# 	played = models.IntegerField()
# 	clean_sheets = models.IntegerField() 
# 	scored = models.IntegerField()
# 	yellows = models.IntegerField()
# 	reds = models.IntegerField()
# 	active = models.BooleanField(default=True)
# 	

# 	def __unicode__(self):
# 		return self.name

# 	def goals_scored(self):
# 		print name + "has scored this many: "
# 		return self.scored

# class matches(models.Model):
# 	gameweek = models.IntegerField() # max 38
# 	date = models.DateField() #saturday/sunday/monday - possible to do choices?
# 	kickoff = models.TimeField() #choices
# 	home = models.ManyToManyField('clubs', related_name="home_team")
# 	away = models.ManyToManyField('clubs', related_name="away_team")
# 	stadium = models.ManyToManyField('clubs', related_name="stadium") 
# 	home_goals = models.IntegerField()
# 	away_goals = models.IntegerField()
# 	#goal_scorers = models.ForeignKey(players) #Would make it a foreignkey on players, but multiple choices with the same attribute selected more than once?

# 	def __unicode__(self):
# 		return str(self.gameweek)










