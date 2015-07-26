1、django-admin.py startproject QQGroupCrawler
2、在setting.py中修改数据库DATABASES信息
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'dbqqgroup',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '3306'
    }
}
3、python manage.py startapp QQGroupDatabase，并拷贝QQGroupDatabase到QQGroupCrawler目录下
4、在setting.py中
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'QQGroupCrawler.QQGroupDatabase'
)
5、models.py中添加数据表信息
6、检查语法：python manage.py validate
7、先在MySql中创建数据库create database dbQQGroup，然后运行manage.py makemigrations，然后python manage.py migrate，如果models.py中信息更改，也执行这2条命令
