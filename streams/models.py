from django.db import models


class Stream(models.Model):
    _id = models.AutoField(primary_key=True, editable=False)
    name = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.name
