from django.contrib import admin
from .models import Camping


@admin.register(Camping)
class CampingAdmin(admin.ModelAdmin):
    pass
