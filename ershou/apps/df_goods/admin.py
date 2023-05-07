# superuser: root 123123...
from django.contrib import admin
from .models import TypeInfo, GoodsInfo,GoodsContent


# 注册模型类  普通方法
class TypeInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'ttitle']
    list_per_page = 10
    search_fields = ['ttitle']
    list_display_links = ['ttitle']


class GoodsInfoAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_display = ['id', 'gtitle', 'gunit','gclick', 'gprice', 'gpic', 'gkucun', 'gjianjie']
    list_editable = ['gkucun', ]
    readonly_fields = ['gclick']
    search_fields = ['gtitle', 'gcontent', 'gjianjie']
    # 在列表页显示的字段中,可以链接到change_form页面的字段
    list_display_links = ['gtitle']

class GoodsContentAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_display = ['id', 'ctitle', 'cpic','cusername', 'clogo', 'cuser_content', 'date_publish', 'cgoodsname']
    readonly_fields = ['cuser_content']
    search_fields = ['ctitle', 'cusername', 'cgoodsname']
    list_display_links = ['ctitle']

admin.site.register(TypeInfo, TypeInfoAdmin)
admin.site.register(GoodsInfo, GoodsInfoAdmin)
admin.site.register(GoodsContent, GoodsContentAdmin)
