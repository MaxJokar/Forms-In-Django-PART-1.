from django.apps import AppConfig


class FormtestConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.formtest'





from django.apps import AppConfig

class BlogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.blog'