from django.conf.urls import url,re_path
from django.views.static import serve
from tiaozao_shop import settings
from . import views

app_name = 'df_goods'

urlpatterns = [
    url('^$', views.index, name="index"),
    url('^index/$', views.index, name="index"),
    url('^list(\d+)_(\d+)_(\d+)/$', views.good_list, name="good_list"),
    url('^detail/(\d+)/$', views.detail, name="detail"),
    url('^content/(\d+)/(\d+)/$', views.content, name="content"),
    url(r'^search/', views.ordinary_search, name="ordinary_search"),  # 全文检索
    re_path('^media/(?P<path>.*)/$',serve,{'document_root':settings.MEDIA_ROOT}),
]
