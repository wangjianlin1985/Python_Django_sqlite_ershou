from django.contrib import admin

from .models import CartInfo


@admin.register(CartInfo)
class CartInfoAdmin(admin.ModelAdmin):
    list_display = ['user', 'goods', 'count']
    list_per_page = 5
    list_filter = ['user', 'goods', 'count']
    search_fields = ['user__uname', 'goods__gtitle']#问题就在这里'user','goods'这两个是ForeignKey字段，应用跨表去取ForeignKey表里面的字
    readonly_fields = ['user', 'goods', 'count']