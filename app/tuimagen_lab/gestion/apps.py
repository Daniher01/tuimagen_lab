from django.apps import AppConfig

class GestionConfig(AppConfig):
    name = 'gestion'

    def ready(self):
        from . import initial_data
        from django.db.models.signals import post_migrate
        post_migrate.connect(initial_data.create_initial_piezas, sender=self)
        post_migrate.connect(initial_data.create_initial_materiales, sender=self)
