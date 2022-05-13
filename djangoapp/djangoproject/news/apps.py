from django.apps import AppConfig
from .tasks import generate_a_message

class NewsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'news'
