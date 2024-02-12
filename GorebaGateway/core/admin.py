from django.contrib import admin

from core.models import Core


class CoreAdmin(admin.ModelAdmin):
    list_display = [
        'business_name', 'company', 'icon', 'status', 'updated_at'
    ]


admin.site.register(Core, CoreAdmin)
