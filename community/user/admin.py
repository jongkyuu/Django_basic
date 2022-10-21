from django.contrib import admin
from .models import FcUser

# 관리자에서 사용할 정보를 기입
# Register your models here.

class FcUserAdmin(admin.ModelAdmin):
    pass

admin.site.register(FcUser, FcUserAdmin)