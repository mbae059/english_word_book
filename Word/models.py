from django.db import models

# Create your models here.

class Word(models.Model):
    eng = models.TextField()
    kor = models.TextField()
    day = models.IntegerField()
    isDone = models.BooleanField(default=False)

    class Meta:
        db_table = 'Word'