from django.shortcuts import render, HttpResponse, redirect
from firstapp.models import Article, Comment
from django.template import context, Template

from firstapp.form import CommentForm
# ⬇view视图逻辑层只负责页面逻辑判断，所以把下面⬇的表单类单独写成一个form.py再引入到view层
# from django import forms
# # 创建表单类
# class CommentForm(forms.Form):
# 	name = forms.CharField(max_length=50)
# 	comment = forms.CharField()


# Create your views here.
# 在 View 中获取 Model 中的数据：创建视图函数
# 引用 models.py 里面写好的文章列表，然后去渲染文章列表
def index(request):
	# 通过打印，简单了解request原理
	# print(request)
	# print('==='*20)
	# print(dir(request))
	# print('==='*20)
	# print(type(request))
	# print('==='*20)

	# ====================================================
	# 1⃣用 Get 方法实现文章分类tag功能（文字分类功能）
	# ====================================================
	# Django 的 MVT 模式
	# 1. Model 层：需要多少数据字段？
	# 2. View 层：根据什么请求，返回什么结果？
	# 3. Template 层：如何与用户交互？

	# 客户端与服务器之间的数据交互过程理解：
	# T - M - V - U - T  （记忆技巧：Time Will Tell）
	# 看到数据的网页Template层 - Model模型层操作数据 - View层写视图（页面）逻辑 - Url分配地址 - 微调 Template层细节逻辑（如添加字数过滤器）
	queryset = request.GET.get('tag')
	# 有参（tag标签）查询／无参查询
	if queryset:
		article_list = Article.objects.filter(tag=queryset)
	else:
		# 使用数据库查询方法object.all()方法从Artic类的数据表中获取数据，放到变量artcle_list中
	    article_list = Article.objects.all()
	
	# 创建一个空的字典
	context = {} 
	# 把数据装载进字典（把article_list值放进context['name']键中），字典的key-value建议相同
	context['article_list'] = article_list 
	# 使用render函数进行渲染，接收三个参数：请求、模板名称、上下文
	index_page = render(request, 'first_web_2.html', context)
	return index_page


# def detail(request):
# 	context = {}
# 	comment_list = Comment.objects.all()
# 	context['comment_list'] = comment_list
# 	# 使用render函数进行渲染，接收三个参数：请求、评论页面名称、上下文
# 	return render(request, 'article_detail.html', context)

# ============================================================
# 2⃣用 Post 方法实现 Django 表单（文章评论功能）
# ============================================================
# 1. 渲染表单（通过引入Django的form模块渲染成表单样式）
# 2. 绑定表单（向服务器提交数据，在view视图层进行表单用户名是否合法等校验）
# 3. 返回校验结果（储存在变量中返回到模板中渲染出来）

def detail(request):
	# 渲染表单：把表单传递到Template模板层，通过get方法获得页面的同时表单也渲染成功了
	# 绑定表单：通过渲染成功的表单通过post方法提交数据
	# 问题：一个视图（页面）接收2种不同的方法
	# 方案：在view视图逻辑层做逻辑（条件）分离
	if request.method == 'GET':
		form = CommentForm
	if request.method == 'POST':
		form = CommentForm(request.POST) # 把request.POST的数据装载到CommentForm中
		# 上面绑定表单后，使用is_valid()方法判断绑定到数据检验是否通过，如果通过，if form.is_valid()为True
		if form.is_valid():
			# 通过验证的数据会储存在字典cleaned_data的中，从中取出名为name的post提交的信息，储存在name变量中
			name = form.cleaned_data['name']
			comment  = form.cleaned_data['comment']
			# 把上面2个变量放在Comment模型中，c为Comment模型的实例
			c = Comment(name=name, comment=comment)
			# 储存实例c到数据库中
			c.save()
			# 跳出该循环，跳（重定向）到urls.py中定义的detail评论页面
			return redirect(to='detail')
	context = {}
	comment_list = Comment.objects.all()
	context['comment_list'] = comment_list
	context['form'] = form # 把表单装进context中
	# 使用render函数进行渲染，接收三个参数：请求、评论页面名称、上下文
	return render(request, 'article_detail.html', context)