# Generated by Django 2.1.2 on 2019-08-26 02:15

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CommentTr',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('author', models.CharField(default='guest', max_length=128)),
                ('text', models.TextField(null=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='MediaTr',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('file', models.FileField(upload_to='uploads/%Y/%m/%d/', validators=[django.core.validators.FileExtensionValidator(['png', 'jpeg', 'jpg'])], verbose_name='画像ファイル')),
            ],
        ),
        migrations.CreateModel(
            name='TopicsTr',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(default='no title', max_length=128)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('last_update', models.DateTimeField(default=django.utils.timezone.now)),
                ('isdraft', models.BooleanField(default=False)),
                ('thumbnail', models.BigIntegerField(default=0)),
                ('text', models.TextField(null=True)),
                ('likes', models.IntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='commenttr',
            name='topic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BlogManager.TopicsTr'),
        ),
    ]
