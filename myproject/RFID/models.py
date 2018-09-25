from django.db import models

class Status(models.Model):
    serial = models.IntegerField(default = 0)
    status = models.CharField(max_length=10)

    def __str__(self):
        return str(self.serial)

class RfidDB(models.Model):
    serial = models.IntegerField(default = 0)
    status = models.CharField(max_length = 10)
    time = models.CharField(max_length = 20, default = 0)


    def __str__(self):
        return str(self.serial)
