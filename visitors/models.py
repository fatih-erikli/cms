from django.db import models

class Visitor(models.Model):
    ip_address = models.GenericIPAddressField()
    date_creation = models.DateTimeField(auto_now_add=True)
    date_latest_activity = models.DateTimeField(auto_now=True)
    latest_activity_hash = models.CharField(max_length=255)
    is_admin = models.BooleanField(default=False)
    browser_name = models.CharField(max_length=255, null=True, blank=True)
    refresh_count = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.ip_address
