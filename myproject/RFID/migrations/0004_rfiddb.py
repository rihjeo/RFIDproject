# Generated by Django 2.1.1 on 2018-09-21 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('RFID', '0003_delete_rfid'),
    ]

    operations = [
        migrations.CreateModel(
            name='RfidDB',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('serial', models.CharField(max_length=15)),
            ],
        ),
    ]
