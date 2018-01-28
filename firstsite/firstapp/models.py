from django.db import models

# Create your models here.

# 在admin.py中增加数据项Article，并在models.py中定义文章的数据字段
class Article(models.Model):
	headline = models.CharField(null=True, blank=True, max_length=500)
	content = models.TextField(null=True, blank=True)
	# 添加tag分类数据项（元组数据结构，前tech为值并作为传递到Django中参数的值，后Tech为名字并在后台管理界面可见可选）
	TAG_CHOICES = (
        ('tech', 'Tech'),
        ('life', 'Life'),
		)
	tag = models.CharField(null=True, blank=True, max_length=5, choices=TAG_CHOICES)
	# 增加一个直接显示标题名字的函数（ object==>str ）
	def __str__(self):
	    return self.headline

# 添加评论模型（姓名+评论）
class Comment(models.Model):
	name = models.CharField(null=True, blank=True, max_length=50)
	comment = models.CharField(null=True, blank=True, max_length=1000)
	# 增加一个直接显示评论内容的函数（ object==>str ）
	def __str__(self):
	    return self.comment