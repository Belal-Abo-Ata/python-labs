from django.apps import AppConfig


class HomeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Home'

    def ready(self):     # used for register signals
        from .signals import create_and_assign_isbn
