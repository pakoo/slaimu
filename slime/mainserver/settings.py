# init logging
import logging
from utils.ansistream import ColorizingStreamHandler
logging.StreamHandler = ColorizingStreamHandler
logging.basicConfig(level=logging.DEBUG,format='[%(asctime)s]%(levelname)s:%(message)s', datefmt='%Y-%m-%d %H:%M:%S')

from configs.common import db_para,cache_para
import mdb
#from mongoengine import *

# init database
if 'initiated' not in globals():
    mdb.mongo_init(db_para)
    #gredis.init(cache_para)
    #connect(db='hoopworld',host=mongo_para['host'],port=mongo_para['port'])
    global initiated
    initiated = True
