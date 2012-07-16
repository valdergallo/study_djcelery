from django.db import models


class Log(models.Model):
    level = models.CharField(max_length=128)
    msg = models.TextField()
    source = models.CharField(max_length=128, blank=True)
    host = models.CharField(max_length=200, blank=True, null=True)
    created_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.level
