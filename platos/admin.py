from django.contrib import admin

# Register your models here.
from .models import Platos


#admin.site.register(Platos)
@admin.register(Platos)
class PlatosAdmin(admin.ModelAdmin):
    list_display = ("nombre","precio",)
