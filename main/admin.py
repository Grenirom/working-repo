from django.contrib import admin

from main.models import Grammy, Musician, Song

admin.site.register(Song)
admin.site.register(Musician)
admin.site.register(Grammy)
