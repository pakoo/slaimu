#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import mdb
from datetime import datetime
from utils.chars import uniform,is_other,is_num_str,md5_str


#########mongo collection structure#########
avatar= {
        'name':'',
        'password':'',
        'game_coin':0,
        'golden_coin':0,
        'total_pay':0,
        'vip_level':0,
        'energy':0,
        'register_info':{
            'register_time':datetime.now(),
            'register_ip':'',
                        }
        'last_login_time':datetime.now(),
        'last_login_ip':'',
        'continuous_login_time':1,
}
############################################

def create_avatar(name,pwd,ip):
    """
    创建用户
    """
    print("name:%s"%name)
    print("pwd:%s"%pwd)
    if name and pwd:  
        if isinstance(name, str):
            name = name.decode('utf-8')
        assert len(name.decode()) <= 10,'用户名长度最多为10'
        assert is_other(uniform(name)) == False,'用户名只能为中文,数字,英文'
        if isinstance(pwd, str):
            pwd = pwd.decode('utf-8')
        assert len(pwd.decode()) <= 10,'密码长度最多为10'
        assert is_num_str(pwd) == True,'密码只能为英文,数字'
        avatar['name'] = name
        avatar['password'] = md5_str(name)
        avatar['register_info']['register_ip'] = ip
        avatar['last_login_ip'] = ip
    else:
        print '>>>>>>>>>>>>>>>>>>>用户名或者密码为空!!!!!!!!!!!!!!'
        


if __name__ == '__main__':
    import settings
    import time
    print 'asdf'
    t = mdb.mcon.slime.t
    at = time.time()
    t.update({'url':1},{'$inc':{'n':1}})
    bt = time.time()
    print 'bt:',time.time()-at
    n = t.find_one({'url':1})['n']
    print 'ct:',time.time()-bt
    print 'you are visitor number %s'%n
     



    
