from django.db import models

# Create your models here.

# 在admin.py中增加数据项Article（一个类即一张数据表，一个属性即一个字段），并在models.py中定义文章的数据字段
# 在admin.py中增加的数据项：显示为后台admin管理页面主页的数据项（数据表）
# 在models.py中定义文章的数据字段：显示为后台admin管理页面具体数据项的属性（字段）
class Article(models.Model):
	# 3个参数分别代表：数据库中该字段可以为空null；表单（验证）中可以可为空blank；最大长度为200
	headline = models.CharField(null=True, blank=True, max_length=500)
	content = models.TextField(null=True, blank=True)
	# 添加tag分类数据项（元组数据结构，前tech为值并作为传递到Django中参数的值，后Tech为名字并在后台管理界面可见可选）
	TAG_CHOICES = (
        ('tech', 'Tech'),
        ('life', 'Life'),
		)
	tag = models.CharField(null=True, blank=True, max_length=5, choices=TAG_CHOICES)
	# under_comments =
	# 增加一个直接显示标题名字的函数（ object==>str ）
	def __str__(self):
	    return self.headline

# 在admin.py中添加评论模型（姓名+评论），并在models.py中定义评论的数据字段
class Comment(models.Model):
	name = models.CharField(null=True, blank=True, max_length=50)
	comment = models.CharField(null=True, blank=True, max_length=1000)
	# 怎样让评论只属于一篇文章？
	# 原来的views.py中的comment_list = Comment.objects.all()，会让所有评论在所有文章下都会同样显示。
	# 需要改成多对一关系：让多条评论只属于对应的一篇文章。
	belong_to = models.ForeignKey(to=Article,related_name='under_comments', null=True, blank=True)
	# 最优评论，布尔值默认为False即最优评论不存在
	best_comment = models.BooleanField(default=False)
	# 增加一个直接显示评论内容的函数（ object==>str ）
	def __str__(self):
	    return self.comment