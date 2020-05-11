from django.db import models
import uuid
def image_upload_to(instance, filename):
    return 'upload/{uuid}/{filename}'.format(uuid=uuid.uuid4().hex, filename=filename)
# Create your models here..
class UserInfo(models.Model):
    # 用户名列，字符串类型，长度为32
    username=models.CharField(max_length=32,null=False)
    password=models.CharField(max_length=64,null=False)
    img = models.ImageField(upload_to=image_upload_to, verbose_name="图片路径",default='')
