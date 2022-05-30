from django.shortcuts import render
from django.http import HttpResponse
from .models import Image
# Create your views here.


def images(request):
    '''
    function to display the index page
    '''
    images = Image.objects.all()
    return render(request, 'images.html', {"images": images})

def Silicon_Valley(request):
    '''
    function to display the location page
    '''

    images = Image.filter_by_location()
    return render(request, 'Silicon Valley.html', {"imagey": images},)
