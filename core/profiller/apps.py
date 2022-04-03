from django.apps import AppConfig


class ProfillerConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'profiller'

    def ready(self):
        import profiller.signals