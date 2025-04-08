from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'accounts'

    def ready(self):  # noqa: PLR6301
        # Import the signals module to ensure that the signal handlers are connected
        # when the app is ready.
        # This is a good place to put any app-specific startup code.
        # You can also perform any other initialization tasks here if needed.
        # Example: print a message to the console when the app is ready
        # You can also use logging instead of print if you prefer
        # import logging
        # logger = logging.getLogger(__name__)
        # logger.info("Accounts app is ready!")
        # You can also perform any other initialization tasks here if needed.
        from . import signals  # noqa: F401, PLC0415
