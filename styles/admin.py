from django.contrib import admin

from styles.models import Attribute, Style

class AttributesInline(admin.TabularInline):
    model = Attribute

class StylesAdmin(admin.ModelAdmin):
    inlines = [AttributesInline]

admin.site.register(Style, StylesAdmin)
admin.site.register(Attribute)
