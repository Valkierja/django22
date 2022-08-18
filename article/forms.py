# 引入表单类
from django import forms
# 引入文章模型
from .models import ArticlePost


class ArticlePostForm(forms.ModelForm):
    class Meta:
        # 指明数据模型来源
        model = ArticlePost

        # 定义表单包含的字段
        fields = ('title', 'body')
        #这个元组里面的值必须和ArticlePost类里面的项名相同； 虽然不太懂python如何实现字符串反查的， 但是实现起来应该也不会太难
