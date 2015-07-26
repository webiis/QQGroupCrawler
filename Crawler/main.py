#-*- coding:utf-8 -*-
__author__ = 'WigouLau'

import redis
import Queue
import TaskList
import FetchTask
import SaveTask

def InitSeed(r, Lists, strKey):
    for list in Lists:
        print list
        r.rpush(strKey, list)

def main():
    r = redis.Redis(host='localhost', port=6379, db=0)
    r.flushdb()

    strKeySeed = "SeedList"
    strKeyTask = "TaskList"
    #[qq or group, type], type: 1--qq, 2--group
    SeedList = [[10000, 1], [10000, 2]]
    queueReocrd = Queue.Queue()

    InitSeed(r, SeedList, strKeySeed)

    TaskListThread = TaskList.TaskList(r, strKeySeed, strKeyTask)
    TaskListThread.start()

    FetchThread = FetchTask.FetchTask(r, strKeyTask, queueReocrd)
    FetchThread.start()

    SaveThread = SaveTask.SaveTask(r, strKeySeed, queueReocrd)
    SaveThread.start()

if __name__ == '__main__':
    main()



