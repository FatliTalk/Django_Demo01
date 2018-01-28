from django import forms
from django.core.exceptions import ValidationError

# 定义一个验证函数
def words_validator(comment):
	if len(comment) < 6:
		raise ValidationError('Not enough words')

# 定义一个验证函数
def  comment_validator(comment):
	if 'fuck' in comment:
	    raise ValidationError('Do not use this word') 

# 创建表单类
class CommentForm(forms.Form):
	name = forms.CharField(max_length=50)
	comment = forms.CharField(
		# 设置表单类型为多行文本输入区Textarea
		widget = forms.Textarea(),
		# 表单验证
		error_messages = {
			'required': 'wow, such words'
			},
		validators = [words_validator, comment_validator]
		)