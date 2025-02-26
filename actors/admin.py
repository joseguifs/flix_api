from django.contrib import admin
from actors.models import Actors


@admin.register(Actors)
class AcotorAdmin(admin.ModelAdmin):
    list_display = ('id','name','nationality')
    search_fields = ['name']