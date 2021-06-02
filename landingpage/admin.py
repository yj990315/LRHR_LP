from django.contrib import admin
from .models import Estimate, Photo

class PhotoInline(admin.TabularInline):
    model = Photo

class EstimateAdmin(admin.ModelAdmin):
    inlines = (PhotoInline,)
    search_fields = ['id']
    list_display = ['id', 'create_date', 'is_done' ]

admin.site.register(Photo)
admin.site.register(Estimate, EstimateAdmin)