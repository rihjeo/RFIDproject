from django.db import models

class RfidDB(models.Model):
    serial = models.IntegerField()
    status = models.CharField(max_length=10)

    def __str__(self):
        return str(self.serial)
