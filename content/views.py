from django.http.response import HttpResponse
from django.shortcuts import render

from content.models import Page, MASTER_PAGE_CONTENT

def dispatch(request):
    page = Page.objects.get(path=request.path, master_page__isnull=False)
    master_page = page.master_page
    rows = []

    for content in master_page.content.all():
        if content.content_type == MASTER_PAGE_CONTENT:
            for content in page.content.all():
                rows.append(content)    
        else:
            rows.append(content)
    raise Exception([i.get_content_type_display() for i in rows])
    return HttpResponse()
