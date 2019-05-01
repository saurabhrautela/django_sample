from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=12)
    age = models.IntegerField()
    email = models.EmailField()

    def __unicode__(self):
        return self.name
