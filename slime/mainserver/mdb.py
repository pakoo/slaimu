#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import pymongo
import redisco

#mongodb global connection
mcon = None
#redis global connection
rcon = None

def mongo_init(db_para):
    """
    初始化mongodb
    """
    global mcon
    mcon = pymongo.Connection(db_para['host'],db_para['port'],auto_start_request=False)
