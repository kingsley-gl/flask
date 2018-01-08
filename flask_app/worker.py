#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2017/11/23
# @Author  : kingsley kwong
# @Site    :
# @File    : worker.py
# @Software: flask_app
# @Function:

import threading
import time
from flask_app.api import FileDequeue
from flask_app import app,logger
from flask_app import _mongo
import os
import gc
thread_pool = []
worker_pool = []


class SaveFileWorker(threading.Thread):
    def __init__(self,file):
        super(SaveFileWorker,self).__init__()
        self.file = file

    def read_file(self,fileobj,chunksize):  #读取文件
        try:
            fileobj.seek(0)
            while True:
                pos = fileobj.tell()
                line = fileobj.read(chunksize)
                if line:
                    yield line
                if pos == fileobj.tell():
                    break
        except Exception as e:
            print(e)
        finally:
            fileobj.close()
            os.remove(fileobj.name)
    @logger
    def run(self):
        with app.app_context():
            try:
                grid_in=self.file['bucket'].open_upload_stream(
                    filename=self.file['filename'],
                    chunk_size_bytes=261120,
                    metadata={"contentType": self.file['contentType']})
                lines = []
                for line in self.read_file(self.file['fileobj'],261120):
                    lines.append(line)
                grid_in.writelines(lines)
                print('save success')
            except Exception as e:
                print(e)
            finally:
                grid_in.close()


@logger
def save_file_thread():
    # print('save file thread start')
    #储存事件
    @logger
    def save_event(dequeue):
        file = FileDequeue.pop()
        t = SaveFileWorker(file)
        t.start()
        worker_pool.append(t) #线程生产

    #删除并回收无用线程
    @logger
    def delworker_event(worker):
        del worker
        print('...begin collect')
        _unreachable = gc.collect()
        print('_unreachable object num:%s'%_unreachable)
        print('garbage object num:%s'%len(gc.garbage))

    #开启监听
    while True:
        if FileDequeue:
            save_event(FileDequeue)
        if worker_pool:
            for worker in worker_pool:
                if not worker.is_alive():
                    worker_pool.remove(worker)
                    delworker_event(worker)
        time.sleep(0)

thread_pool.append(threading.Thread(target=save_file_thread))