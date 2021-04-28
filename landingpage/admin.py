from django.contrib import admin
from .models import Estimate, Photo

class PhotoInline(admin.TabularInline):
    model = Photo

class RequestInline(admin.ModelAdmin):
    inlines = [PhotoInline, ]

class EstimateAdmin(admin.ModelAdmin):
    search_fields = ['id']

admin.site.register(Photo)
admin.site.register(Estimate, EstimateAdmin)