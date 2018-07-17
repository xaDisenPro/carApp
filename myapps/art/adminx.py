#from django.contrib import admin
import xadmin as admin
from xadmin import views

from art.models import Tag, Art

# Register your models here.
class BaseSetting:
    # 主题修改
    enable_themes = True
    use_bootswatch = True


class GlobalSettings:
    # 整体配置
    site_title = '美文后台管理系统'
    site_footer = '千锋教育python项目'
    menu_style = 'accordion'  # 菜单折叠
    # 搜索模型
    global_search_models = [Tag, Art]

    # 模型的图标(参考bootstrap图标插件)
    global_models_icon = {
        Art: "glyphicon glyphicon-book",
        Tag: "glyphicon glyphicon-tags"
    }  # 设置models的全局图标

    # 配置应用的名称(中文)
    apps_label_title = {
        'art': '文章管理'
    }

    # 配置应用的图标
    apps_icons = {
        'art': 'glyphicon glyphicon-th-large',
    }


class TagAdmin:
    # 后台列表显示列
    list_display = ['name', 'modify_time', 'is_top']
    # 后台列表查询条件
    search_fields = ['name']


class ArtAdmin:
    # 后台列表显示列
    list_display = ['title', 'summary', 'content', 'publish_date', 'tag']
    # 后台列表查询条件
    search_fields = ['title', 'summary']
    # 搜索关键字（title或summary）
    # Art.objects.filter(Q(title__contains=key) | Q(summary__contains=key)).all()

    # 设置字段的样式
    style_fields = {
        'content': 'ueditor'
    }


admin.site.register(views.CommAdminView, GlobalSettings)
admin.site.register(views.BaseAdminView, BaseSetting)

admin.site.register(Tag, TagAdmin)
admin.site.register(Art, ArtAdmin)


