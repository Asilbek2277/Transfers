from django.contrib import admin

from .models import *


class ClubAdmin(admin.ModelAdmin):
    list_display = ['nom', 'prezident', 'davlat']
    search_fields = ['nom']
    search_help_text = 'Club nomi boyicha qidirish imkoniyati'
    list_filter = ['davlat']


class PlayerAdmin(admin.ModelAdmin):
    list_display = ['ism', 'club', 'davlat']
    search_fields = ['ism']
    search_help_text = 'Ism boyicha qidirish imkoniyati'
    list_filter = ['club']
    autocomplete_fields = ['club']


class TransferAdmin(admin.ModelAdmin):
    list_display = ['player', 'narx', 'sana']


admin.site.register(Davlat)
admin.site.register(Club, ClubAdmin)
admin.site.register(Player, PlayerAdmin)
admin.site.register(Transfer, TransferAdmin)
