# -*- coding: utf-8 -*-
# Create your views here.
from django.http import HttpResponse
def getParam(request, a , b):
    print a,b
    result = unicode(a) + unicode(b)
    return HttpResponse(result)
