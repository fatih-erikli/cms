from django.contrib import admin

from content.models import Page, PageContent

class PageContentInline(admin.StackedInline):
    model = PageContent
    fk_name = 'page'

class PageAdmin(admin.ModelAdmin):
    inlines = [PageContentInline]

admin.site.register(Page, PageAdmin)
admin.site.register(PageContent)
