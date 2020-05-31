import datetime

from django.db import models
from django.core.validators import FileExtensionValidator
from django.utils import timezone

ALLOWED_EXTS = ['png', 'jpg', 'jpeg', 'webm', 'gif']

class Tag(models.TextChoices):
    SHARING = 'SH', 'Sharing'
    DISCOVERY = 'DI', 'Discovery'
    PHOTO = 'PH', 'Photo'
    TECHNOLOGY = 'TE', 'Technology'
    SPEECH = 'SP', 'Speech'
    COPACETIC = 'CO', 'Copacetic'
    BEAUTY = 'BE', 'Beauty'
    AESTHETIC = 'AE', 'Aesthetic'
    PROBABILITY = 'PR', 'Probability'
    PURSUIT = 'PU', 'Pursuit'
    INQUIRY = 'IN', 'Inquiry'
    EMOTION = 'EM', 'Emotion'
    TRAVEL = 'TR', 'Travel'

class ModelMethods:
    @staticmethod
    def is_week_old(pub_date):
        return (pub_date <= (timezone.now() - datetime.timedelta(days=7)))


class Post(models.Model):
    post_text = models.CharField(max_length=2048, null=True)
    post_media = models.ImageField(upload_to='uploads/',
                                blank=True,
                                validators=[FileExtensionValidator(allowed_extensions=ALLOWED_EXTS)],
                                null=True,
    )
    post_author = models.CharField(max_length=32, null=True)
    post_pub_date = models.DateTimeField('date published', null=True)
    post_tag = models.CharField(
        max_length=2,
        choices=Tag.choices,
        default=Tag.SHARING,
        blank=False,
        null=True,
    )

    def __str__(self):
        return f"text: {self.post_text}, author: {self.post_author}, pub_date: {self.post_pub_date}"

    def is_week_old(self):
        return ModelMethods.is_week_old(self.post_pub_date)

class Comment(models.Model):
    comment_post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)
    
    comment_text = models.CharField(max_length=2048, null=True)
    comment_media = models.ImageField(upload_to='uploads/',
                                blank=True,
                                validators=[FileExtensionValidator(allowed_extensions=ALLOWED_EXTS)],
                                null=True,
    )
    comment_author = models.CharField(max_length=32, null=True)
    comment_pub_date = models.DateTimeField('date published', null=True)
    comment_tag = models.CharField(
        max_length=2,
        choices=Tag.choices,
        default=Tag.SHARING,
        blank=False,
        null=True
    )

    def __str__(self):
        return f"text: {self.comment_text}, author: {self.comment_author}, pub_date: {self.comment_pub_date}"

    def is_week_old(self):
        return ModelMethods.is_week_old(self.comment_pub_date)
