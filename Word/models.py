from django.db import models

class Word(models.Model):
    eng = models.TextField()
    kor = models.TextField()
    day = models.IntegerField()
    isDone = models.BooleanField(default=False)

    class Meta:
        db_table = 'Word'