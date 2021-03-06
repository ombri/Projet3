# Generated by Django 3.1.5 on 2021-06-23 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app2', '0008_auto_20210623_0834'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Forum',
        ),
        migrations.AlterField(
            model_name='forum2',
            name='author',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='forum2',
            name='content',
            field=models.TextField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='forum2',
            name='topic',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
