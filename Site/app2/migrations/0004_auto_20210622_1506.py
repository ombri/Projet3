# Generated by Django 3.1.5 on 2021-06-22 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app2', '0003_auto_20210622_1501'),
    ]

    operations = [
        migrations.AlterField(
            model_name='forum',
            name='content',
            field=models.TextField(max_length=10000),
        ),
    ]
