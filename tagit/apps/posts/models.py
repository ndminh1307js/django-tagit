from django.db import models
from django.conf import settings
from django.urls import reverse


class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             related_name='post_created',
                             on_delete=models.CASCADE)
    caption = models.TextField()
    image = models.ImageField(
        upload_to=f'images/%Y/%m/%d/',
        blank=True
    )
    created = models.DateTimeField(auto_now_add=True,
                                   db_index=True)
    users_like = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                        related_name='images_liked',
                                        blank=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return f"A post with caption '{self.caption}'"

    def get_absolute_url(self):
        return reverse('detail', args=[self.id])


class Comment(models.Model):
    post = models.ForeignKey(Post,
                             related_name='comments',
                             on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             related_name='comment_created',
                             on_delete=models.CASCADE)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True,
                                   db_index=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return self.content
