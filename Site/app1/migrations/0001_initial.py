# Generated by Django 3.1.5 on 2021-06-22 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stream',
            fields=[
                ('id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('link', models.CharField(max_length=300)),
                ('title', models.CharField(max_length=300)),
            ],
        ),
    ]
