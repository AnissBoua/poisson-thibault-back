from django.apps import AppConfig


class QuickstartConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'quickstart'

    def ready(self):
        import quickstart.model
        import quickstart.serializer
        import quickstart.view
        import quickstart.urls