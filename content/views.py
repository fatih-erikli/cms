import random
import string
import hashlib
from uuid import uuid4
from string import whitespace
from django.http.response import HttpResponse
from django.shortcuts import render

from content.models import CONTENT_TYPE_ANCHOR, MASTER_PAGE_CONTENT, Page
from settings.models import Seed
from visitors.models import Visitor
from ads.models import Platform

CONTENT_START = '<!--page-content-start-->'
CONTENT_END = '<!--page-content-end-->'
CONTENT_OBJECT = None

empty_string = str
def build_attributes_string(attributes) -> str:
    parts = ['%(key)s="%(value)s"' % {'key': key, 'value': attributes[key]} for key in attributes]
    [space, *_] = whitespace
    return space + space.join(parts) if parts else empty_string()

def build_page(request, meta, built, page, classnames):
    return render(request, 'base.html', {
        'meta': [{
            'html_tag': item.html_tag,
            'name': item.name,
            'value': item.value % {
                'name': page.name,
            },
        } for item in meta.items.all()],
        'built': built,
        'page': page,
        'classnames': classnames,
        'ads_snippets': [platform.generate_snippet() for platform in Platform.objects.all()]
    })

def get_or_create_visitor(request):
    browser_name = request.META.get('HTTP_USER_AGENT')
    ip_address = request.META.get('HTTP_X_FORWARDED_FOR') or request.META.get('REMOTE_ADDR')
    visitor, created = Visitor.objects.get_or_create(
        ip_address=ip_address,
        browser_name=browser_name,
        is_admin=request.user.is_superuser)

    if not created:
        visitor.refresh_count += 1
        visitor.latest_activity_hash = uuid4().hex
        visitor.save()

def dispatch(request, path=None):
    visitor = get_or_create_visitor(request)
    page = Page.objects.get(path=path, master_page__isnull=False)
    master_page = page.master_page
    meta = page.meta
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

    seed = Seed.latest()
    random.seed(seed)

    classnames = {}
    def classify(stylesheet, prefix='block'):
        if not stylesheet.strip():
            return

        for (classname, class_stylesheet) in classnames.items():
            if stylesheet == class_stylesheet:
                return classname

        random_string = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(42))
        unique_classname = '%(prefix)s-%(hash)s' % {
            'prefix': prefix,
            'hash': hashlib.sha256(random_string.encode('utf-8')).hexdigest()
        }
        classnames[unique_classname] = stylesheet
        return unique_classname

    built = []
    for row in rows:
        is_start_tag = row == CONTENT_START
        is_closing_tag = row == CONTENT_END

        if is_start_tag or is_closing_tag:
            row = CONTENT_OBJECT

        if is_start_tag:
            built.append(('''<%(html_tag)s class="%(class)s">%(text)s''' % {
                'html_tag': row.html_tag, 'text': row.render_text(), 'class': classify(row.cascade_styles())}).strip()),
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
                    text = row.render_text() or title
                else:
                    attributes = {
                        'href': row.external_url,
                        'title': 'External link',
                    }
                    text = row.render_text()
            else:
                attributes = {}
                text = row.render_text()

            built.append(('''
            <%(html_tag)s class="%(class)s"%(extra_attributes)s>%(child)s</%(html_tag)s>
            ''' % {
                'html_tag': row.html_tag,
                'child': text,
                'class': classify(row.cascade_styles()),
                'extra_attributes': build_attributes_string(attributes)
            }).strip())
    return build_page(request, meta, built, page, classnames)
