"""
Models for stock application.

股票数据模型定义
"""

from django.db import models


class Stock(models.Model):
    """股票基本信息表"""
    code = models.CharField('股票代码', max_length=20, unique=True)
    name = models.CharField('股票名称', max_length=50)
    industry = models.CharField('所属行业', max_length=50, blank=True)

    class Meta:
        verbose_name = '股票'
        verbose_name_plural = '股票列表'

    def __str__(self):
        return f'{self.code} {self.name}'


class StockDailyData(models.Model):
    """股票日K线数据表"""
    stock_code = models.ForeignKey(Stock, on_delete=models.CASCADE,
                                   related_name='daily_data',
                                   verbose_name='股票代码')
    trade_date = models.DateField('交易日期')
    open_price = models.DecimalField('开盘价', max_digits=10, decimal_places=2)
    close_price = models.DecimalField('收盘价', max_digits=10, decimal_places=2)
    high_price = models.DecimalField('最高价', max_digits=10, decimal_places=2)
    low_price = models.DecimalField('最低价', max_digits=10, decimal_places=2)
    volume = models.BigIntegerField('成交量')
    turnover = models.DecimalField('成交额', max_digits=18, decimal_places=2,
                                   null=True, blank=True)
    created_at = models.DateTimeField('创建时间', auto_now_add=True)

    class Meta:
        verbose_name = '日K线数据'
        verbose_name_plural = '日K线数据列表'
        ordering = ['-trade_date']
        unique_together = [['stock_code', 'trade_date']]

    def __str__(self):
        return f'{self.stock_code.code} - {self.trade_date}'
