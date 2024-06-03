from django.apps import AppConfig


class LchainbotAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'LchainBot_app'
class ChatConfig(AppConfig):
    name = 'chat'

    def ready(self):
        from . import bot
        # Access bot_instance to ensure it's initialized
        bot.bot_instance    