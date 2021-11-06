from django.contrib import admin
from visitors.models import Visitor

from django.contrib.humanize.templatetags.humanize import naturaltime

class VisitorAdmin(admin.ModelAdmin):
    ordering = ('-date_latest_activity',)
    list_display = ('ip_address', 'date_creation', 'latest_activity', 'browser_name', 'refresh_count')

    def latest_activity(self, object):
        return naturaltime(object.date_latest_activity)

admin.site.register(Visitor, VisitorAdmin)
