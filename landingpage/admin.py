from django.contrib import admin
from .models import Estimate, OverallImage, DetailImage
from import_export import resources, fields
from import_export.admin import ExportActionModelAdmin, ImportExportMixin, ImportMixin

class OverallImageInline(admin.TabularInline):
    model = OverallImage

class DetailImageInline(admin.TabularInline):
    model = DetailImage

class TypeReport(resources.ModelResource):
    class Meta:
       model = Estimate

    product_size = fields.Field(
        attribute='get_type_of_product_display',
        column_name='Type Of Product'
    )

class EstimateAdmin(ImportExportMixin, admin.ModelAdmin):
    inlines = (OverallImageInline, DetailImageInline)
    resource_class = TypeReport
    search_fields = ['id', 'name', 'brand']
    list_display = ['id', 'name', 'brand', 'type_of_product','create_date', 'is_done' ]


admin.site.register(Estimate, EstimateAdmin)
admin.site.register(OverallImage)
admin.site.register(DetailImage)

