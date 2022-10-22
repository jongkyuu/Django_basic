from django.contrib import admin
from .models import Fcuser

# 관리자에서 사용할 정보를 기입
# Register your models here.

class FcuserAdmin(admin.ModelAdmin):
    list_display = ('username', 'useremail', 'password', 'registered_dttm')

admin.site.register(Fcuser, FcuserAdmin)