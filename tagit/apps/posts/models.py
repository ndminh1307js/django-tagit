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
    total_likes = models.PositiveIntegerField(db_index=True,
                                              default=0)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return f"a post with caption: {self.caption[:30]}..."

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
        return f'a comment: {self.content[:30]}... on a post'

    def get_absolute_url(self):
        return f'/posts/{self.post.id}/#comment-{self.id}'
