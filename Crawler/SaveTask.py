#-*- coding=utf-8 -*-
__author__ = 'WigouLau'
import redis
import threading
import time
import Queue
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "QQGroupCrawler.settings")
from QQGroupCrawler.QQGroupDatabase.models import QQGroupDatabase


class SaveTask(threading.Thread):
    def __init__(self, r, strKeySeed, queueRecord):
        threading.Thread.__init__(self)
        self.r = r
        self.strKeySeed = strKeySeed
        self.queueRecord = queueRecord
        self.bRunFlag = True

    def run(self):
        tStartTime = time.time()
        while (self.bRunFlag == True):
            if ((time.time() - tStartTime) > 10):
                self.bRunFlag == False

            if (not self.queueRecord.empty()):
                dictInfo = self.queueRecord.get()
                #print "dictinfo", dictInfo
                if (dictInfo.has_key("type") and dictInfo["type"] == 1):
                    self.r.rpush(self.strKeySeed, [int(dictInfo["group"]), 2])
                    QQGroupDatabase.QQInfoSave(dictInfo)
                elif (dictInfo.has_key("type") and dictInfo["type"] == 2):
                    self.r.rpush(self.strKeySeed, [int(dictInfo["qq"]), 1])
                    QQGroupDatabase.GroupInfoSave(dictInfo)

