# Generated by Django 2.1.2 on 2019-08-16 07:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BlogManager', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='commenttr',
            old_name='topic_id',
            new_name='topic',
        ),
        migrations.RenameField(
            model_name='mediatr',
            old_name='topic_id',
            new_name='topic',
        ),
    ]
