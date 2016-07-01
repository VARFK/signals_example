from django.apps import AppConfig

class SignalsExampleConfig(AppConfig):
    name = 'signals_example'
    verbose_name = 'Django Signals Example'

    def ready(self):
        import signals_example.signals
