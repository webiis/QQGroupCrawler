1��django-admin.py startproject QQGroupCrawler
2����setting.py���޸����ݿ�DATABASES��Ϣ
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
3��python manage.py startapp QQGroupDatabase��������QQGroupDatabase��QQGroupCrawlerĿ¼��
4����setting.py��
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'QQGroupCrawler.QQGroupDatabase'
)
5��models.py��������ݱ���Ϣ
6������﷨��python manage.py validate
7������MySql�д������ݿ�create database dbQQGroup��Ȼ������manage.py makemigrations��Ȼ��python manage.py migrate�����models.py����Ϣ���ģ�Ҳִ����2������
