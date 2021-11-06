from django.contrib import admin

from content.models import Page, PageContent, Meta, MetaItem

class PageContentInline(admin.StackedInline):
    model = PageContent
    fk_name = 'page'

class MetaItemInline(admin.TabularInline):
    model = MetaItem

class PageAdmin(admin.ModelAdmin):
    inlines = [PageContentInline]

class MetaAdmin(admin.ModelAdmin):
    inlines = [MetaItemInline]

admin.site.register(Page, PageAdmin)
admin.site.register(PageContent)
admin.site.register(Meta, MetaAdmin)
admin.site.register(MetaItem)
