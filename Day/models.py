from django.db import models

# Create your models here.
class Day(models.Model):
    day = models.IntegerField()

    class Meta:
        db_table = 'Day'