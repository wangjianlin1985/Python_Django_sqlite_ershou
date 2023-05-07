from django.contrib import admin

from .models import UserInfo, GoodsBrowser


class UserInfoAdmin(admin.ModelAdmin):
    list_display = ["uname", "usex","uage","upersonInf", "uemail", "ulogo","ushou", "uaddress", "uyoubian", "uphone", "urealname", "uzhengjian_type", "uzhengjian_tel", "uzhengjian_img", "ucheck_passOrfail","uname_passOrfail"]
    list_per_page = 5
    list_filter = ["uname", "uyoubian"]
    search_fields = ["uname", "uyoubian"]
    # 详情页面的只读字段
    readonly_fields = ["uname"]
    # 在列表页可以编辑的字段
    # list_editable = ["ucheck_passOrfail"]


class GoodsBrowserAdmin(admin.ModelAdmin):
    list_display = ["user", "good"]
    list_per_page = 50
    list_filter = ["user__uname", "good__gtitle"]
    search_fields = ["user__uname", "good__gtitle"]
    readonly_fields = ["user", "good"]
    refresh_times = [3, 5]


admin.site.site_header = '跳蚤市场后台管理系统'
admin.site.site_title = '跳蚤市场后台管理系统'

admin.site.register(UserInfo, UserInfoAdmin)
admin.site.register(GoodsBrowser, GoodsBrowserAdmin)