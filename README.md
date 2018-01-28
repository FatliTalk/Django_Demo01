# 用Django框架开发网页功能（分类&评论）

开发环境：
- macOS 10.12.6
- Python3.6
- Python框架：Django 1.11.7
- 前端框架：[Semantic UI](http://www.semantic-ui.cn/)
- 开发工具：Sublime Text

## 一、用 Get 方法实现文章分类功能
### Django 的 MVT 模式
1. Model 层：需要多少数据字段？
2. View 层：根据什么请求，返回什么结果？
3. Template 层：如何与用户交互？

### 客户端与服务器之间的数据交互过程理解：
T - M - V - U - T  （记忆技巧：Time Will Tell）
看到数据的网页Template层 - Model模型层操作数据 - View层写视图（页面）逻辑 - Url分配地址 - 微调 Template层细节逻辑（如添加字数过滤器）

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
