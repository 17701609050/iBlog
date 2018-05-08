# -*- coding: UTF-8 -*-
import logging
import traceback
import json

from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render_to_response
from django.http.response import HttpResponseRedirect, HttpResponse
from django.template import TemplateDoesNotExist, RequestContext
from .sso import do_login

@csrf_exempt
def login(request):
    if request.method == 'GET':
        return render_to_response('common/login.html',  {}, RequestContext(request))
    else:
        res = {'result': 'error'}
        response = HttpResponse()
        try:
            if request.POST.get('user_name') is not None:
                (result, s,) = do_login(request, True)
                res.update({'result': ('success' if result else 'fail')})
        except Exception as e:
            logging.getLogger('django').error(traceback.print_exc())
            raise e
        finally:
            res.update({'user_token': request.session.session_key})
            response.write(json.dumps(res).encode('utf-8'))
            return response



def logout(request):
    pass