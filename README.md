# Stock Web - 股票数据可视化系统

基于 Django 框架开发的股票数据可视化平台，集成 MySQL 数据库与 ECharts 图表库。

## 技术栈

| 技术 | 用途 |
|------|------|
| Python 3.x | 后端开发语言 |
| Django 4.x | Web 框架 |
| MySQL | 关系型数据库 |
| ECharts | 前端数据可视化 |
| HTML/CSS/JS | 前端页面 |

## 功能特性

- 股票 K 线图展示（Candlestick Chart）
- 收盘价折线图
- 成交量柱状图
- Django Admin 后台管理
- REST API 数据接口
- MySQL 数据持久化存储

## 快速开始

### 环境要求

- Python 3.8+
- MySQL 5.7+
- pip

### 安装步骤

1. 克隆项目：
```bash
git clone https://github.com/wotonger/wotonger-stock.git
cd wotonger-stock
```

2. 创建虚拟环境并安装依赖：
```bash
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

3. 配置数据库：

编辑 `stock_project/settings.py`，修改数据库配置：
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'stock_db',        # 你的数据库名称
        'USER': 'root',           # 数据库用户名
        'PASSWORD': 'your_password',  # 数据库密码
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

4. 初始化数据库：
```bash
python manage.py makemigrations
python manage.py migrate
```

5. 运行项目：
```bash
python manage.py runserver
```

6. 访问 `http://localhost:8000` 即可查看。

## 项目结构

```
stock_web/
├── stock/                  # 股票应用
│   ├── models.py          # 数据模型
│   ├── views.py           # 视图函数
│   └── admin.py           # 后台管理
├── stock_project/         # 项目配置
│   ├── settings.py        # 全局设置
│   └── urls.py            # URL路由
├── templates/             # HTML模板
│   ├── index.html         # 首页
│   └── stock_chart.html   # 图表页
├── static/                # 静态文件
├── manage.py              # Django管理命令
├── requirements.txt       # Python依赖
└── README.md              # 项目说明
```

## 作者

广东工业大学 · 大数据管理与应用专业  
作者：吴桐

## License

MIT License
