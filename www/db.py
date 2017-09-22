#!/usr/bin/env python
# -*- coding:utf-8 -*-
# db.py

import time
import uuid
import functools
import threading
import logging



#数据库引擎对象：
class _Engine(object):
    def __init__(self, connect):
        self._connect = connect

    def connect(self)
        return self._connect()

engine = None

#持有数据库连接的上下文对象：
class _DbCtx(threading.local):
    def __init__(self):
        self.connection = None
        self.transactions = 0



