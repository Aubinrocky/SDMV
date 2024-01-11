from django.contrib import admin
from .models import *


class SportAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


class CityAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


class LevelAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


class TournamentAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ("title", "is_published", "created_at")


admin.site.register(Sport, SportAdmin)
admin.site.register(City, CityAdmin)
admin.site.register(Level, LevelAdmin)
admin.site.register(Tournament, TournamentAdmin)
