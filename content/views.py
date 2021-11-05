from django.http.response import HttpResponse
from django.shortcuts import render

from content.models import Page, MASTER_PAGE_CONTENT

CONTENT_START = '<!--page-content-start-->'
CONTENT_END = '<!--page-content-end-->'
CONTENT_OBJECT = None


def dispatch(request):
    page = Page.objects.get(path=request.path, master_page__isnull=False)
    master_page = page.master_page
    rows = []

    for content in master_page.content.all():
        if content.content_type == MASTER_PAGE_CONTENT:
            rows.append(CONTENT_START)
            CONTENT_OBJECT = content
            for content in page.content.all():
                rows.append(content)
            rows.append(CONTENT_END)
        else:
            rows.append(content)

    built = []
    for row in rows:
        is_start_tag = row == CONTENT_START
        is_closing_tag = row == CONTENT_END

        if is_start_tag or is_closing_tag:
            row = CONTENT_OBJECT

        if is_start_tag:
            built.append(('''<%(html_tag)s style="%(styles)s">%(text)s''' % {
                'html_tag': row.html_tag, 'text': row.text, 'styles': row.cascade_styles()}).strip()),
        elif is_closing_tag:
            built.append(('''</%(html_tag)s>''' %
                         {'html_tag': row.html_tag, }).strip())
        else:
            built.append(('''
            <%(html_tag)s style="%(styles)s">%(child)s</%(html_tag)s>
            ''' % {
                'html_tag': row.html_tag,
                'child': row.text,
                'styles': row.cascade_styles(),
            }).strip())
    return HttpResponse('\n'.join(built))
