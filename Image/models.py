from django.db import models


class Image(models.Model):
    name = models.TextField(default="default")
    day = models.IntegerField(default=1)
    uuid = models.TextField(unique=True, default="")
    class Meta:
        db_table = "Image"
