# Generated by Django 2.0.7 on 2018-07-26 03:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='summary',
        ),
        migrations.AddField(
            model_name='project',
            name='goal',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='project',
            name='plan',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='project',
            name='reason',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='creation_time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
