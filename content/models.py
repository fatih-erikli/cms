from django.db import models

from styles.models import Style


class Page(models.Model):
    name = models.CharField(max_length=255)
    path = models.CharField(max_length=255)
    master_page = models.ForeignKey('self',
                                    null=True,
                                    on_delete=models.SET_NULL,
                                    blank=True)

    def __str__(self) -> str:
        return self.name

    def url(self) -> str:
        return '/%s' % str(self.path)

MASTER_PAGE_CONTENT = 5
CONTENT_TYPE_ANCHOR = 9

class PageContent(models.Model):
    style = models.ForeignKey(
        Style, null=True, blank=True, on_delete=models.SET_NULL)
    page = models.ForeignKey(
        Page, on_delete=models.SET_NULL, null=True, blank=True,
        related_name='content')
    parent = models.ForeignKey(
        'self', null=True, blank=True, on_delete=models.SET_NULL,
        related_name="content")
    is_placeholder = models.BooleanField(default=False)
    content_type = models.IntegerField(choices=(
        (0, ('Header')),
        (1, ('Title')),
        (2, ('Paragraph')),
        (3, ('Image')),
        (4, ('List')),
        (MASTER_PAGE_CONTENT, ('Content')),
        (6, ('Navigation')),
        (7, ('Searchbar')),
        (8, ('Footer')),
        (CONTENT_TYPE_ANCHOR, ('Anchor')),
    ), default=0)
    order = models.IntegerField(default=0)
    text = models.TextField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    html_tag = models.CharField(
        default='div',
        max_length=255,
        choices=(
            ('div', 'div'),
            ('header', 'header'),
            ('aside', 'aside'),
            ('section', 'section'),
            ('footer', 'footer'),
            ('header', 'header'),
            ('p', 'paragraph'),
            ('h1', 'header-1'),
            ('h2', 'header-2'),
            ('h3', 'header-3'),
            ('h4', 'header-4'),
            ('h5', 'header-5'),
            ('a', 'anchor'),
            ('time', 'Datetime'),
        )
    )
    linked_page = models.ForeignKey(Page, on_delete=models.SET_NULL,
        related_name="links", blank=True, null=True)
    external_url = models.CharField(blank=True, null=True, max_length=255)

    def __str__(self) -> str:
        return str(self.pk)

    def cascade_styles(self) -> str:
        style = self.style
        rules = []
        if style:
            for extend in style.extends.all():
                for attribute in extend.attributes.all():
                    rules.append(attribute.rule())

            for attribute in style.attributes.all():
                rules.append(attribute.rule())
        return chr(32).join(rules)
