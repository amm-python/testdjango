from django.db import models


class person(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    info=models.TextField()
    class Meta:
        db_table = "person"