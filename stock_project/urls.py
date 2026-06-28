"""
URL configuration for stock_project.

股票数据可视化系统 - URL路由配置
"""

from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),           # 首页
    path('stock/', views.stock_chart, name='stock_chart'),  # 股票图表页
    path('data/', views.stock_data, name='stock_data'),     # 数据接口（AJAX）
]
