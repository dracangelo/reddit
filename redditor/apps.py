from django.apps import AppConfig


class RedditorConfig(AppConfig):
    name = 'redditor'

    def ready(self):
        import redditor.signals