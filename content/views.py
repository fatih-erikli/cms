from string import whitespace
from django.http.response import HttpResponse
from django.shortcuts import render

from content.models import CONTENT_TYPE_ANCHOR, MASTER_PAGE_CONTENT, Page

CONTENT_START = '<!--page-content-start-->'
CONTENT_END = '<!--page-content-end-->'
CONTENT_OBJECT = None

empty_string = str
def build_attributes_string(attributes) -> str:
    parts = ['%(key)s="%(value)s"' % {'key': key, 'value': attributes[key]} for key in attributes]
    [space, *_] = whitespace
    return space + space.join(parts) if parts else empty_string()

def dispatch(request, path=None):
    page = Page.objects.get(path=path, master_page__isnull=False)
    master_page = page.master_page
    rows = []

    for content in master_page.content.order_by('order'):
        if content.content_type == MASTER_PAGE_CONTENT:
            rows.append(CONTENT_START)
            CONTENT_OBJECT = content
            for content in page.content.order_by('order'):
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
            if row.content_type == CONTENT_TYPE_ANCHOR:
                if row.linked_page:
                    title = row.linked_page.name
                    attributes = {
                        'href': row.linked_page.url(),
                        'title': title,
                    }
                    text = row.text or title
                else:
                    attributes = {
                        'href': row.external_url,
                        'title': 'External link',
                    }
                    text = row.text
            else:
                attributes = {}
                text = row.text

            built.append(('''
            <%(html_tag)s style="%(styles)s"%(extra_attributes)s>%(child)s</%(html_tag)s>
            ''' % {
                'html_tag': row.html_tag,
                'child': text,
                'styles': row.cascade_styles(),
                'extra_attributes': build_attributes_string(attributes)
            }).strip())
    return HttpResponse('\n'.join(built))
