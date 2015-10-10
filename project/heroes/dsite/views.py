from django.shortcuts import render

from django.http import HttpResponse
import MySQLdb

# Create your views here.
def index(request):
    return render(request, 'homepage.html', locals())

def profile(request):
    return render(request, 'profile.html', locals())

def caffe(request):
    return render(request, 'caffe.html', locals())

