from django.db import models
from datetime import datetime
class Diary(models.Model):
    text = models.TextField(default="my dairy")
    date = models.DateTimeField(default=datetime.now(), blank=True)

    def __str__(self):
        return 'Diary #{}'.format(self.id)

    class Meta:
        verbose_name_plural = "My_Dairy_Entries"