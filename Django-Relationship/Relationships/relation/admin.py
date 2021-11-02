from django.contrib import admin

from relation.models import Bank, Phone, Song

# Register your models here.

admin.site.register(Bank)
admin.site.register(Phone)


class SongAdmin(admin.ModelAdmin):
    list_display = ['name','written_by']

admin.site.register(Song,SongAdmin)
