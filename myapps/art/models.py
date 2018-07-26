from django.db import models

from DjangoUeditor.models import UEditorField

# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=50,
                            verbose_name='标签名')
    modify_time = models.DateTimeField(auto_now=True,
                                       verbose_name='最后修改')

    is_top = models.BooleanField(default=True,
                                 verbose_name='是否置顶')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '标签分类'
        db_table = 't_tag'
        verbose_name_plural = verbose_name


class Art(models.Model):
    title = models.CharField(max_length=100,
                             verbose_name='标题')
    summary = models.TextField(verbose_name='简介')

    # 内容使用DjangoUeditor富文本字段
    content = UEditorField(verbose_name='内容',
                           width=480,
                           height=360,
                           imagePath='art/u_images/',
                           filePath='art/u_files/',
                           toolbars='full',
                           blank=True,
                           default='')

    publish_date = models.DateTimeField(auto_now_add=True,
                                        blank=True,  # 是否可以为 空
                                        null=True,
                                        verbose_name='发布时间')

    tag = models.ForeignKey(Tag,
                            on_delete=models.SET_NULL,
                            null=True,
                            verbose_name='标签')

    @property
    def tagName(self):
        return self.tag.name

    class Meta:
        db_table = 't_art'
        verbose_name = '文章'
        verbose_name_plural = verbose_name

