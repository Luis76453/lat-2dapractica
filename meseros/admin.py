from django.contrib import admin

# Register your models here.
from .models import Meseros


#admin.site.register(Meseros)
@admin.register(Meseros)
class MeserosAdmin(admin.ModelAdmin):
    list_display = ("nombre","nacionalidad","edad",)