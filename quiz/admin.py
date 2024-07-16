from django.contrib import admin
from .models import Quiz

# Register your models here.
admin.site.register(Quiz) 
# 관리자 페이지에 Quiz 모델을 
# register하여 관리하도록 설정