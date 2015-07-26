#-*- coding:utf-8 -*-
__author__ = 'WigouLau'

import threading
import Queue
import redis
import time
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "QQGroupCrawler.settings")
from QQGroupCrawler.QQGroupDatabase.models import QQGroupDatabase


class TaskList(threading.Thread):
    def __init__(self, r, strKeySeed, strKeyTask):
        threading.Thread.__init__(self)
        self.r = r
        self.strKeySeed = strKeySeed
        self.strKeyTask = strKeyTask

        self.bRunFlag = True;

    def run(self):
        tStartTime = time.time()
        while (self.bRunFlag == True):

            if (time.time() - tStartTime > 100):
                self.bRunFlag = False

            if (self.r.llen(self.strKeySeed) <= 0):
                continue

            seed = self.r.lpop(self.strKeySeed)
            if (seed and QQGroupDatabase.IsHasRecord(seed[0], seed[1]) == False):
                self.r.rpush(self.strKeyTask, seed)
                tStartTime = time.time()

        print "TaskList thread stop."
