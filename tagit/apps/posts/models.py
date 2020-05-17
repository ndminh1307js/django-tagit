from django.db import models
from django.conf import settings


class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             related_name='posts_created',
                             on_delete=models.CASCADE)
    caption = models.TextField(blank=True)
    image = models.ImageField(
        upload_to=f'images/%Y/%m/%d/')
    created = models.DateTimeField(auto_now_add=True,
                                   db_index=True)
    users_like = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                        related_name='images_liked',
                                        blank=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return f"A post with caption '{self.caption}'"
