# Generated by Django 4.0.4 on 2022-05-27 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bussiness_name', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('fuel_type', models.CharField(max_length=255)),
            ],
        ),
    ]
