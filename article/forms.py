# 引入表单类
from django import forms
# 引入文章模型
from .models import ArticlePost


class ArticlePostForm(forms.ModelForm):
    class Meta:
        # 指明数据模型来源
        model = ArticlePost
        # TODO:为什么不用指定author，且author没指定default
        # 定义表单包含的字段
        fields = ('title', 'body')
