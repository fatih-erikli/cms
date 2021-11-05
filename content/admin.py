from django.contrib import admin

from content.models import Page, PageContent

class PageContentInline(admin.StackedInline):
    model = PageContent

class PageAdmin(admin.ModelAdmin):
    inlines = [PageContentInline]

admin.site.register(Page, PageAdmin)
admin.site.register(PageContent)
