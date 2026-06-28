from django.contrib import admin
from .models import Stock, StockDailyData


@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    list_display = ['code', 'name', 'industry']
    search_fields = ['code', 'name']


@admin.register(StockDailyData)
class StockDailyDataAdmin(admin.ModelAdmin):
    list_display = ['stock_code', 'trade_date', 'open_price', 'close_price',
                     'high_price', 'low_price', 'volume']
    list_filter = ['trade_date', 'stock_code']
    search_fields = ['stock_code__code']
