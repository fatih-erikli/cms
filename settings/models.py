from django.db import models
from datetime import datetime
from uuid import uuid4

class Seed(models.Model):
    value = models.CharField(max_length=255, editable=False)
    date = models.DateTimeField(default=datetime.now)

    class Meta:
        get_latest_by = 'date'

    def save(self):
        self.value = uuid4().hex
        return super(Seed, self).save()

    def __str__(self) -> str:
        return self.value

    @classmethod
    def latest(klass):
        return klass.objects.latest()
