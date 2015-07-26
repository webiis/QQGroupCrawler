#-*- coding:utf-8 -*-
__author__ = 'WigouLau'
import threading
import time
import requests
import os


class FetchTask(threading.Thread):
    def __init__(self, r, strKeyTask, queueRecord):
        threading.Thread.__init__(self)
        self.r = r
        self.strKeyTask = strKeyTask
        self.queueRecord = queueRecord
        self.bRunFlag = True

    def run(self):
        tStartTime = time.time()
        session = FetchTask.GetSession(isAjax=True)
        while (self.bRunFlag):
            if (time.time() - tStartTime > 10):
                self.bRunFlag = False
            if (self.r.llen(self.strKeyTask) <= 0):
                continue

            task = self.r.lpop(self.strKeyTask)
            if (task):
                task = task.replace("[", "")
                task = task.replace("]", "")
                task = task.replace(" ", "")
                tasklist = task.split(",")
                #print "tasklist", tasklist, tasklist[0], tasklist[1]
                r = self.Download(session, tasklist[0], tasklist[1])
                if (not r):
                    continue

                Content = r.text.split('\n')
                #print Content
                dictInfo = {}
                for line in Content:
                    if (tasklist[1] == "1"):
                        dictInfo = FetchTask.ParseQQInfo(line)
                        pass
                    elif (tasklist[1] == "2"):
                        dictInfo = FetchTask.ParseGroupInfo(line)

                    if (dictInfo != None):
                        self.queueRecord.put(dictInfo)


                self.SaveFile(Content, tasklist[0], tasklist[1])

                tStartTime = time.time()


        print "FetchTask thread stop"

    def Download(self, session, strNumber, type, timesout = 0):
        if (timesout > 4):
            return None

        try:
            print 'http://qun.col.pw/doquery.php?q=%s&type=%s' % (strNumber, type)
            r = session.get('http://qun.col.pw/doquery.php?q=%s&type=%s' % (strNumber, type))
            return r
        except Exception, e:
            time.sleep(5)
            timesout = timesout + 1
            return self.Download(session, strNumber, type, timesout)

    def SaveFile(self, Content, strNumber, type):
        if (os.path.exists("..\\data") == False):
            os.makedirs("..\\data")
        if (int(type) == 1):
            strFilePath = "..\\data\\" + time.strftime("%Y-%m-%d-%H-%M-%S") + "_QQ_"+strNumber+".txt"
        else:
            strFilePath = "..\\data\\" + time.strftime("%Y-%m-%d-%H-%M-%S") + "_Group_"+strNumber+".txt"
        f = open(strFilePath, mode='w')
        for t in Content:
            f.write(t)
        f.close()

    @staticmethod
    def GetSession(isAjax = False):
        s = requests.session()
        s.headers.update({'Referer': 'http://qun.col.pw/',
                      'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.104 Safari/537.36',
                      'Accept-Encoding': 'gzip,deflate,sdch'})
        s.get('http://qun.col.pw')

        if isAjax:
            s.headers.update({'X-Requested-With': 'XMLHttpRequest'})

        return s

    @staticmethod
    def ParseQQInfo(strInfo):
        dictQQInfo = {"qq":"", "nick":"", "sex":"", "role":"", "group":"", "type":1}
        listQQInfo = strInfo.split(",")
        #print "listQQInfo", listQQInfo
        if (len(listQQInfo) > 5):
            dictQQInfo["qq"] = listQQInfo[1].encode("utf-8")
            dictQQInfo["nick"] = listQQInfo[2].encode("utf-8")
            dictQQInfo["sex"] = listQQInfo[3].encode("utf-8")
            dictQQInfo["role"] = listQQInfo[4].encode("utf-8")
            dictQQInfo["group"] = listQQInfo[5].encode("utf-8")
            return dictQQInfo
        else:
            return None

    @staticmethod
    def ParseGroupInfo(strGroupInfo):
        dictGroupInfo = {"group":"", "name":"", "qq":"", "nick":"", "sex":"", "role":"", "type":2}
        listGroupInfo = strGroupInfo.split(",")
        #print "listGroupInfo", listGroupInfo
        if (len(listGroupInfo) > 6):
            dictGroupInfo["name"] = listGroupInfo[1].encode("utf-8")
            dictGroupInfo["qq"] = listGroupInfo[2].encode("utf-8")
            dictGroupInfo["nick"] = listGroupInfo[3].encode("utf-8")
            dictGroupInfo["sex"] = listGroupInfo[4].encode("utf-8")
            dictGroupInfo["role"] = listGroupInfo[5].encode("utf-8")
            dictGroupInfo["group"] = listGroupInfo[6].encode("utf-8")
            return dictGroupInfo
        else:
            return None
