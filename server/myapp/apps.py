from django.apps import AppConfig


# 应用配置类
class MyappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'myapp'  # 应用程序名称
