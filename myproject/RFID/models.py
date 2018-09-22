from django.db import models

class RfidDB(models.Model):
    serial = models.IntegerField(default = 0)
    status = models.CharField(max_length=10)

    def __str__(self):
        return str(self.serial)
