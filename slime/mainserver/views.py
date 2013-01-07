# -*- coding: utf-8 -*-
from django.http import HttpResponse , HttpResponseRedirect
from django.shortcuts import render_to_response as render
from mango import database as db, OperationFailure
import datetime



def test(request):
    #print dir(request.session)
    print 'session key:',request.session.session_key
    #print 'asdf:',request.session.get('asdf',0)
    #request.session['asdf']+= 1
    #print 'load:',request.session.load()
    #print 'create:',request.session._get_new_session_key()
    print 'cookie:',request.COOKIES
    #request.session.get_expiry_age()
    print 'cookie expiry time:',request.session.get_expiry_date()
    print 'db:',db.sessions.count()
    return HttpResponse('test')
