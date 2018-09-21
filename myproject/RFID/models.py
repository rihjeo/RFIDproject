from django.db import models

class RfidDB(models.Model):
    name = models.CharField(max_length=10)
    serial = models.CharField(max_length=15)

    def __str__(self):
        return self.name
