# 用Django框架开发网页功能（分类&评论）

开发环境：
- macOS 10.12.6
- Python3.6
- Python框架：Django 1.11.7
- 前端框架：[Semantic UI](http://www.semantic-ui.cn/)
- 开发工具：Sublime Text 3

---

![Django_admin01.png](https://github.com/FatliTalk/Django_Demo01/blob/master/pagesPictures/Django_admin01.png?raw=true)

<br>

## 一、用 Get 方法实现文章分类功能
### Django 的 MVT 模式
1. Model 层：需要多少数据字段？
2. View 层：根据什么请求，返回什么结果？
3. Template 层：如何与用户交互？

### 客户端与服务器之间的数据交互过程理解：
T - M - V - U - T  （记忆技巧：Time Will Tell）

看到数据的网页Template层 - Model模型层操作数据 - View层写视图（页面）逻辑 - Url分配地址 - 微调 Template层细节逻辑（如添加字数过滤器）

<br>

![文章标签分类-Get方法.png](https://github.com/FatliTalk/Django_Demo01/blob/master/pagesPictures/%E6%96%87%E7%AB%A0%E6%A0%87%E7%AD%BE%E5%88%86%E7%B1%BB-Get%E6%96%B9%E6%B3%95.png?raw=true)

<br>
<br>

## 二、用 Post 方法实现 Django 表单
1. 渲染表单（通过引入Django的form模块渲染成表单样式）
2. 绑定表单（向服务器提交数据，在view视图层进行表单用户名是否合法等校验）
3. 返回校验结果（储存在变量中返回到模板中渲染出来）

- 渲染表单：把表单传递到Template模板层，通过get方法获得页面的同时表单也渲染成功了
- 绑定表单：通过渲染成功的表单通过post方法提交数据
- 问题：一个视图（页面）接收2种不同的方法
- 方案：在view视图逻辑层做逻辑（条件）分离

表单数据储存：
1. 绑定表单后，使用is_valid()方法判断绑定到表单的数据是否通过校验
2. 使用save()方法储存数据（具体见views.py代码注释）

<br>

![文章评论页-Post方法.png](https://github.com/FatliTalk/Django_Demo01/blob/master/pagesPictures/%E6%96%87%E7%AB%A0%E8%AF%84%E8%AE%BA%E9%A1%B5-Post%E6%96%B9%E6%B3%95.png?raw=true)

<br>

## 三、用 URL 正则实现文章链接跳转

### 不够多的URL怎么办？（自动设置URL文章页数）

思路：在urls.py写URL的正则式，在视图层views.py获取，在模板层呈现

- ^detail$：精确模式
- 限定三位数字：例子 `/detail/(\d){3}`
- 限定多位数：例子`/detail/(\d+)`



![url自动获取页数01.png](https://github.com/FatliTalk/Django_Demo01/blob/master/pagesPictures/url%E8%87%AA%E5%8A%A8%E8%8E%B7%E5%8F%96%E9%A1%B5%E6%95%B001.png?raw=true)

![url自动获取页数02.png](https://github.com/FatliTalk/Django_Demo01/blob/master/pagesPictures/url%E8%87%AA%E5%8A%A8%E8%8E%B7%E5%8F%96%E9%A1%B5%E6%95%B002.png?raw=true)

<br>

### 怎样让评论只属于一篇文章？（多对一关系）

完成上述第二点的用 Post 方法实现 Django 表单（评论功能）， 原来的views.py中的`comment_list = Comment.objects.all()` 、 `context['comment_list'] = comment_list` 会让所有评论在所有文章下都会同样显示。

需要改成多对一（Django没有一对多关系）关系：让多条评论只属于对应的一篇文章。

> **关系：**关系数据库的威力体现在表之间的相互关联。 Django 提供了三种最常见的数据库关系：多对一（django.db.models.ForeignKey）、多对多（ManyToManyField）、一对一（OneToOneField），用法和其他 Field 字段类型一样：在模型中做为一个类属性包含进来。


![文章评论页_多对一关系和best_comment.png](https://github.com/FatliTalk/Django_Demo01/blob/master/pagesPictures/%E6%96%87%E7%AB%A0%E8%AF%84%E8%AE%BA%E9%A1%B5_%E5%A4%9A%E5%AF%B9%E4%B8%80%E5%85%B3%E7%B3%BB%E5%92%8Cbest_comment.png?raw=true)

<br>

### 一图多表怎么办？（文章视图和评论表单视图分离）

`def detail( ... ):`

分离后：

`def detail( ... ):` ➕ `def detail_comment( ... ):`

<br>

---

<br>

> 附：解决 tab or space 的问题：
https://www.python.org/dev/peps/pep-0008/#tabs-or-spaces

方法：
1. 把原来的 tab 替换为 space ：在 Sublime Text 3 （此处使用的代码编辑器是 Sublime Text 3 ）中，find tab 全部替换为4个空格（原来 1 个 tab = 8 个 space ，并且 py 文件中 tab 和 space 共存造成混乱）

2. 在 Sublime Text 3 中 Preferences -> Settings 配置
    ```
    {
        // 显示空格
        "draw_white_space": "all",
        // 设置tab=4space（针对Python）
        "tab_size": 4,
        "translate_tabs_to_spaces": true,
    }
    ```
