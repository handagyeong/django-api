#postApp/admin.py코드
from django.contrib import admin
from .models import Post

# Register your models here.
admin.site.register(Post)