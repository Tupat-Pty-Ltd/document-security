from django.apps import AppConfig as DjangoAppConfig


class AppConfig(DjangoAppConfig):
    """
    """
    name = 'document_security'
    verbose_name = "Document Security"

    def ready(self):
        pass
