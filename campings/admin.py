from django.contrib import admin

from .models import Camping, CampingItemCategory


@admin.register(Camping)
class CampingAdmin(admin.ModelAdmin):
    pass


@admin.register(CampingItemCategory)
class CampingItemCategory(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
