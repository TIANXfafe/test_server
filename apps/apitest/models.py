from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


# Create your models here.
class Project(models.Model):
    """
    项目表
    """
    ProjectType = (
        ('web', 'web'),
        ('app', 'app')
    )
    name = models.CharField(max_length=50, verbose_name="项目名称")
    type = models.CharField(max_length=50, verbose_name="项目类型", choices=ProjectType)
    description = models.CharField(max_length=1024, blank=True, null=True, verbose_name="描述")
    last_update_time = models.DateTimeField(auto_now=True, verbose_name="最近修改时间")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name="创建人")


class Host(models.Model):
    """
    host域名
    """
    name = models.CharField(max_length=50, verbose_name="名称")
    host = models.CharField(max_length=1024, verbose_name="Host地址")
    description = models.CharField(max_length=1024, blank=True, null=True, verbose_name="描述")
    project = models.ForeignKey(Project, on_delete=models.CASCADE, verbose_name="所属项目", related_name="host_list")
