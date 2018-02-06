from django.contrib import admin
from firstapp.models import Article, Comment # 增加 Article、Comment 的引入

# Register your models here.
admin.site.register(Article) # 增加数据项Article，并models.py中定义文章的数据字段
admin.site.register(Comment) # 增加数据项Comment，并在models.py中定义评论的数据字段