from django.db import models


class Job(models.Model):
    value = models.CharField(max_length=10, null=True, blank=True)
    created_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return (self.value, self.created_at)
