# pages/views.py
# this views file chua cac noi dung hien thi tren page, urls.py thi xac dinh noi chua content

from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def homePageView(request):
    return HttpResponse('Hello, World!')