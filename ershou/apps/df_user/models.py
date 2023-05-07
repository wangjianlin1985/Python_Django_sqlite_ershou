from django.db import models

from datetime import datetime
from tinymce.models import HTMLField

from df_goods.models import GoodsInfo



class UserInfo(models.Model):

    uname = models.CharField(max_length=20, verbose_name="用户名", unique=True)
    usex = models.CharField(max_length=10, verbose_name="性别", default="")
    uage = models.CharField(max_length=10, verbose_name="年龄", default="")
    upersonInf = models.CharField(max_length=200, verbose_name="个人简介", default="")
    ulogo= models.FileField(verbose_name="用户头像",upload_to='images', default='default.jpg')
    upwd = models.CharField(max_length=40, verbose_name="用户密码", blank=False)
    uemail = models.EmailField(verbose_name="邮箱", unique=True)
    urealname = models.CharField(max_length=20, default="", verbose_name="真实姓名")
    uzhengjian_type = models.CharField(max_length=20, default="", verbose_name="证件类型")
    uzhengjian_tel = models.CharField(max_length=18, default="", verbose_name="证件号码")
    uzhengjian_img = models.FileField(upload_to='images/zhengjian_img', default="", verbose_name="证件图片")
    ucheck_passOrfail=models.BooleanField(verbose_name="认证审批",default=False)
    ushou = models.CharField(max_length=20, default="", verbose_name="收货名称")
    uaddress = models.CharField(max_length=100, default="", verbose_name="地址")
    uyoubian = models.CharField(max_length=6, default="", verbose_name="邮编")
    uphone = models.CharField(max_length=11, default="", verbose_name="手机号")
    uname_passOrfail = models.BooleanField(verbose_name="允许登录", default=True)
    # default,blank是python层面的约束，不影响数据库表结构，修改时不需要迁移 python manage.py makemigrations

    class Meta:
        verbose_name = "用户信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.uname


class GoodsBrowser(models.Model):

    user = models.ForeignKey(UserInfo, on_delete=models.CASCADE, verbose_name="用户ID")
    good = models.ForeignKey(GoodsInfo, on_delete=models.CASCADE, verbose_name="商品ID")
    browser_time = models.DateTimeField(default=datetime.now, verbose_name="浏览时间")

    class Meta:
        verbose_name = "用户浏览记录"
        verbose_name_plural = verbose_name

    def __str__(self):
        return "{0}浏览记录{1}".format(self.user.uname, self.good.gtitle)
class Information(models.Model):
    # 联系商家
    isDelete = models.BooleanField(default=False)  # 逻辑删除
    ctitle = models.CharField(max_length=20, verbose_name="商品名称")
    cusername = models.CharField(max_length=20, verbose_name="买家昵称")
    cusername1 = models.CharField(max_length=20, verbose_name="卖家昵称")
    ccontent_chart = HTMLField(max_length=200, verbose_name="消息内容")
    ccheck = models.BooleanField(verbose_name="消息是否已读", default=False)
    date_publish = models.DateTimeField(verbose_name="发表时间",default=datetime.now)
    cinformation = models.ForeignKey(UserInfo, on_delete=models.CASCADE, verbose_name="消息")  # 外键关联GoodsContent表

    class Meta:
        verbose_name = "用户消息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.cusername1
class tuihuoInfo(models.Model):
    # 联系商家
    isDelete = models.BooleanField(default=False)  # 逻辑删除
    title = models.CharField(max_length=20, verbose_name="商品名称")
    username = models.CharField(max_length=20, verbose_name="收件人姓名")
    username1 = models.CharField(max_length=20, verbose_name="寄件人姓名")
    person_number = models.CharField(max_length=20, verbose_name="身份证号码")
    order_number = models.CharField(max_length=20, verbose_name="订单号")
    kuaidi = models.CharField(max_length=20, verbose_name="快递类型")
    kuaidi_number = models.CharField(max_length=20, verbose_name="快递单号")
    address = models.CharField(max_length=50, verbose_name="收货地址",default=None)
    address1 = models.CharField(max_length=50, verbose_name="发货地址", default=None)
    text = HTMLField(max_length=200, verbose_name="退货理由",default=None)
    passOrdefault = models.BooleanField(verbose_name="同意退款",default=False)
    date_publish = models.DateTimeField(verbose_name="发表时间",default=datetime.now)

    class Meta:
        verbose_name = "退款订单"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username