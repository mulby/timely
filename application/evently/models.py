from django.db import models


class Source(models.Model):
    description = models.CharField(max_length=256)

    def __unicode__(self):
        return self.description


class Event(models.Model):
    timestamp = models.DateTimeField('detection date')
    description = models.CharField(max_length=1024)
    source = models.ForeignKey(Source)

    def __unicode__(self):
        return self.description
