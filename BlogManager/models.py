# coding: utf-8
import uuid
from django.utils import timezone
from django.db import models
from django.core.validators import FileExtensionValidator

# 記事情報
class TopicsTr(models.Model):
    id              = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title           = models.CharField(max_length=128, default='no title', null=False)
    created_at      = models.DateTimeField(default=timezone.now, null=False)
    last_update     = models.DateTimeField(default=timezone.now, null=False)
    isdraft         = models.BooleanField(default=False, null=False)
    thumbnail       = models.BigIntegerField(default=0, null=False)
    text            = models.TextField(null=True)
    likes           = models.IntegerField(default=0, null=False)

# メディア情報
class MediaTr(models.Model):
    id              = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    topic_id        = models.ForeignKey(TopicsTr, to_field='id', on_delete=models.CASCADE)
    file            = models.FileField(
                        upload_to='uploads/%Y/%m/%d/',
                        verbose_name='画像ファイル',
                        validators=[FileExtensionValidator(['png','jpeg','jpg', ])],
                    )

# コメント情報
class CommentTr(models.Model):
    id              = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    topic_id        = models.ForeignKey(TopicsTr, to_field='id', on_delete=models.CASCADE)
    author          = models.CharField(max_length=128, default='no title', null=False)
    text            = models.TextField(null=True)
    created_at      = models.DateTimeField(default=timezone.now, null=False)

