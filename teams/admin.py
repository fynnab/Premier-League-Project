from django.contrib import admin
from teams.models import clubs, players 

# # Register your models here.




class clubsAdmin(admin.ModelAdmin):
	list_display = ['name', 'manager', 'stadium', 'active'] # league position
	list_filter = ['name', 'active']
	#prepopulated_fields

class playersAdmin(admin.ModelAdmin):
	list_display = ['name', 'club', 'nationality', 'position', 'played', 'scored', 'active']
	list_filter = ['name', 'club', 'nationality', 'position', 'played', 'scored', 'active']
	prepopulated_fields = {"slug": ("name",)}

admin.site.register(clubs, clubsAdmin)
admin.site.register(players, playersAdmin)
# admin.site.register(matches)