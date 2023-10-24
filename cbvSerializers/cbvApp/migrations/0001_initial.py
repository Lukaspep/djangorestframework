# Generated by Django 4.2.4 on 2023-09-13 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Passenger',
            fields=[
                ('firstName', models.IntegerField(primary_key=True, serialize=False)),
                ('lastName', models.CharField(max_length=20)),
                ('travelPoints', models.DecimalField(decimal_places=3, max_digits=10)),
            ],
        ),
    ]