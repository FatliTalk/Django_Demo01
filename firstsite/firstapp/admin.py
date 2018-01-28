from django.contrib import admin
from firstapp.models import Article # 增加 Article 的引入

# Register your models here.
admin.site.register(Article)        # 增加数据项Article，并在models.py中定义文章的数据字段