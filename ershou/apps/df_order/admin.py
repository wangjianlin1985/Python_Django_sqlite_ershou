from django.contrib import admin

from .models import OrderDetailInfo, OrderInfo
from df_user.models import tuihuoInfo


@admin.register(OrderInfo)
class OrderInfoAdmin(admin.ModelAdmin):
    # 在列表页显示的字段,默认会显示所有字段,有对应的方法可以重写
    list_display = ["oid", "user", "odate", "ototal", "oaddress"]
    # 列表页每页展示的条数
    list_per_page = 5
    # 右侧的筛选,必须是字段,可以继承自SimpleListFilter来自定义筛选字段和规则
    list_filter = ["user", "odate", "oaddress"]
    # 在列表页可以模糊搜索的字段
    search_fields = ["user__uname"]
    ordering = ["-odate"]


@admin.register(OrderDetailInfo)
class OrderDetailInfoAdmin(admin.ModelAdmin):

    list_display = ["goods", "order", "price", "count"]
    list_per_page = 5
    list_filter = ["goods"]

@admin.register(tuihuoInfo)
class tuihuoInfoAdmin(admin.ModelAdmin):
    # 在列表页显示的字段,默认会显示所有字段,有对应的方法可以重写
    list_display = ["title", "username", "username1", "person_number", "order_number","kuaidi","kuaidi_number","address","address1","text","passOrdefault","date_publish"]
    # 列表页每页展示的条数
    list_per_page = 5
    # 右侧的筛选,必须是字段,可以继承自SimpleListFilter来自定义筛选字段和规则
    list_filter = ["title", "username", "username1","order_number"]
    # 在列表页可以模糊搜索的字段
    search_fields = ["username"]
    ordering = ["-order_number"]