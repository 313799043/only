from django.contrib import admin

# Register your models here.
# from TestModel.models import Test

#首页轮播图
from .models import Banner
#用户
from .models import UserProfile




admin.site.register(Banner)
admin.site.register(UserProfile)