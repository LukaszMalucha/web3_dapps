from django.contrib import admin

from core import models


class ModuleModelAdmin(admin.ModelAdmin):
    ordering = ["phase_title", "week", "month", "year"]
    list_display = ["phase_title", "week", "month", "year"]
    search_fields = ["phase_title", "module_link"]
    list_filter = ("module_brand",)

    class Meta:
        model = models.ModuleModel


admin.site.register(models.MyProfile)
admin.site.register(models.ModuleModel, ModuleModelAdmin)
