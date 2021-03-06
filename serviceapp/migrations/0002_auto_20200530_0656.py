# Generated by Django 3.0.6 on 2020-05-30 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('serviceapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TruckSchedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('truckId', models.CharField(blank=True, max_length=128, null=True)),
                ('orderId', models.CharField(blank=True, max_length=256, null=True)),
                ('sourceCity', models.CharField(blank=True, max_length=128, null=True)),
                ('destinationCity', models.CharField(blank=True, max_length=128, null=True)),
                ('departureDate', models.CharField(blank=True, max_length=128, null=True)),
                ('arrivalDate', models.CharField(blank=True, max_length=128, null=True)),
                ('scheduledAt', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
            ],
        ),
        migrations.DeleteModel(
            name='Order',
        ),
    ]
