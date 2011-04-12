#from django.http import HttpResponse
from django.shortcuts import render_to_response
from movies.models import Area

def index(request):
    #return HttpResponse("Hello, world. You're at the movie index.")
    areaList = Area.objects.all()
    for a in areaList:
        print a.chtName.encode('utf8')
    return render_to_response('base.html',locals())