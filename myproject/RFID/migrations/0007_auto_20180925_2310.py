# Generated by Django 2.1.1 on 2018-09-25 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RFID', '0006_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='status',
            name='time',
        ),
        migrations.AddField(
            model_name='rfiddb',
            name='time',
            field=models.CharField(default=0, max_length=20),
        ),
    ]