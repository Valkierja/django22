from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class ArirticlePost(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=64)
    body = models.TextField()
    createdTime = models.DateTimeField(default=timezone.now)#初始化时写入默认值为当前时间
    updatedTime = models.DateTimeField(auto_now=True)#每次access时自动修改为当前时间
    class Meta:
        ordering = ('-createdTime',)
    def __str__(self):
        return self.title
