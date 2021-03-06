from django.db import models


class Style(models.Model):
    name = models.CharField(max_length=255)
    extends = models.ManyToManyField('self', blank=True)

    def __str__(self) -> str:
        return self.name


class Attribute(models.Model):
    style = models.ForeignKey(
        'style', on_delete=models.SET_NULL, null=True, related_name='attributes')
    name = models.CharField(max_length=255,
                            choices=(
                                ('margin', 'margin'),
                                ('padding', 'padding'),
                                ('font-family', 'font-family'),
                                ('font-size', 'font-size'),
                                ('border', 'border'),
                                ('box-sizing', 'box-sizing'),
                                ('background', 'background'),
                                ('color', 'color'),
                                ('width', 'width'),
                                ('max-width', 'max-width'),
                                ('height', 'height'),
                                ('max-height', 'max-height'),
                            ))
    value = models.CharField(max_length=255)
    unit = models.CharField(max_length=255, blank=True, null=True, choices=(
        ('px', 'Pixels'),
        ('em', 'Line-width'),
        ('vw', 'Viewport-width'),
        ('vh', 'Viewport-height'),
        ('%', 'Percent')
    ))

    def __str__(self) -> str:
        return self.rule()

    def rule(self) -> str:
        return '%s: %s%s;' % (self.name, self.value, self.unit or '')
