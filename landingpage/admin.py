from django.contrib import admin
from .models import Estimate, OverallImage, DetailImage

class OverallImageInline(admin.TabularInline):
    model = OverallImage

class DetailImageInline(admin.TabularInline):
    model = DetailImage

class EstimateAdmin(admin.ModelAdmin):
    inlines = (OverallImageInline, DetailImageInline)
    search_fields = ['id']
    list_display = ['id', 'create_date', 'is_done' ]


admin.site.register(Estimate, EstimateAdmin)
admin.site.register(OverallImage)
admin.site.register(DetailImage)