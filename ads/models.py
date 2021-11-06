from django.db import models

class Platform(models.Model):
    publisher_id = models.CharField(max_length=255)
    snippet_type = models.CharField(max_length=255, default='adsense', choices=(
        ('adsense', 'Google adsense'),
    ))

    def __str__(self) -> str:
        return self.publisher_id

    def generate_snippet(self):
        return ('''
        <script
            data-ad-client="ca-pub-%(publisher_id)s"
            async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>
        ''' % {
            'publisher_id': self.publisher_id,
        }).strip()
