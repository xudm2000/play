from django.db import models


class Image(models.Model):
    img_id = models.IntegerField(verbose_name='图片ID', null=True)
    img_name = models.CharField(max_length=50, verbose_name='图片名称')
    img_content = models.ImageField(verbose_name='图片内容')

    def __str__(self):
        return self.img_name
