from django.contrib import admin
from visitors.models import Visitor

class VisitorAdmin(admin.ModelAdmin):
    ordering = ('-date_latest_activity',)
    list_display = ('ip_address', 'date_creation', 'date_latest_activity', 'browser_name', 'refresh_count')

admin.site.register(Visitor, VisitorAdmin)
