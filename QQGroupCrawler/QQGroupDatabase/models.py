#-*- coding:utf-8 -*-
from django.db import models


# Create your models here.
class TableQQInfo(models.Model):
    qq = models.CharField(u'QQ号码', max_length=25)
    nick = models.CharField(u'昵称', max_length=64)
    sex = models.CharField(u'性别', max_length=20)
    role = models.CharField(u'群角色', max_length=20, help_text=u'群主:管理员:成员')
    group = models.CharField(u'群号码', max_length=25)

    class Meta:
        db_table = "tbQQInfo"

class TableGroupInfo(models.Model):
    group = models.IntegerField(u'群号码')
    name = models.CharField(u"群名称", max_length=64)
    qq = models.CharField(u'QQ号码', max_length=25)
    nick = models.CharField(u'昵称', max_length=64)
    sex = models.CharField(u'性别', max_length=20)
    role = models.CharField(u'群角色', max_length=20, help_text=u'群主:管理员:成员')

    class Meta:
        db_table = "tbGroupInfo"


class QQGroupDatabase:
    def __init__(self):
        pass

    @staticmethod
    def QQInfoSave(info):
        return
        record = TableQQInfo(qq=info.pop("qq"), nick=info.pop("nick"), sex=info.pop("sex"), role=info.pop("role"), group=info.pop("group"))
        record.save()

    @staticmethod
    def GroupInfoSave(info):
        return
        record = TableGroupInfo(group=info.pop("group"), name=info.pop("name"),
                           qq=info.pop("qq"), nick=info.pop("nick"), sex=info.pop("sex"), role=info.pop("role"))
        record.save()

    @staticmethod
    def IsHasRecord(strNumber, type):
        """
        # qq
        if (type == 1):
            TableQQInfo.objects.filter(qq=strNumber)
        # group
        else:
            TableGroupInfo.objects.filter(group=strNumber)
        """

        return False
