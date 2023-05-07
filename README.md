# Python_Django_sqlite_ershou
基于Python+Django+Sqlite校园二手交易跳蚤市场网站设计毕业源码案例设计

## 基于python的跳蚤市场：二手交易市场网站，基于Python3.x和Django2.x

## 项目尽量使用Django内部提供的API，后台管理为Django自带的管理系统django-admin。适合Django的小型实战项目。

## 功能简介：
商品浏览：商品的图片，售价，种类，简介以及库存等信息。
商品评论：用户在购买了商品后才会出现商品评论的文本框。
全文检索：支持对商品种类以及商品名称，简介的检索。
登录注册：用户的登录与注册，重置密码，密码发送到注册邮箱。
跳蚤使用协议：协议签属才能使用。
用户中心：支持用户个人信息，收货地址，修改密码，发布商品，修改个人信息，实名认证，等信息的更新，商品加入购物车，订单生成。
消息中心：支持用户回复商家信息。
卖家中心：在商品详细信息中通过联系卖家或则在评论区通过用户头像进入。
商品下单：在支付接口和企业资质的支持下可完成商品的下单功能，按照原子事务处理，下单异常则终止此次下单过程。
后台管理：支持后台管理功能，商品及用户信息的增加，更新与删除，可自定制样式与功能，日志，以及权限的管理和分配。

可以通过命令创建管理员 python manage.py createsuperuser
我创建的管理员账号密码： admin/admin123

用户既可以是买家也可以当卖家，自行注册即可！