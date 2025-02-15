from django.contrib import admin

# Register your models here.
# from myapp.models import Classification, Thing, User
from myapp.models import User

# 将模型注册到Django的后台管理模块
# admin.site.register(Classification)
# admin.site.register(Thing)
admin.site.register(User)
