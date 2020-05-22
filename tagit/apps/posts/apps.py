from django.apps import AppConfig


class PostsConfig(AppConfig):
    name = 'posts'

    def ready(self):
        # import signal handlers
        import tagit.apps.posts.signals
