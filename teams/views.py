from django.shortcuts import render
from teams.models import clubs, players

# Create your views here.

def viewClubs(request):
	clubs_list = []
	clubs_obj = clubs.objects.all()

	for club1 in clubs_obj:
		clubs_dict = {}

		clubs_dict['name'] = club1.name
		clubs_dict['nickname'] = club1.nickname
		clubs_dict['stadium'] = club1.stadium
		clubs_dict['manager'] = club1.manager

		clubs_list.append(clubs_dict)

		return render(request, 'clubs.html', {'clubs_list': clubs_list})


def viewPlayers(request):
	players_list = []
	players_obj = players.objects.all()

	for players1 in players_obj:
		players_dict = {}

		players_dict['name'] = players1.name
		players_dict['club'] = players1.club
		players_dict['position'] = players1.position
		players_dict['born'] = players1.born
		players_dict['nationality'] = players1.nationality

		players_list.append(players_dict)

	return render(request, 'players.html', {'players_list': players_list})





