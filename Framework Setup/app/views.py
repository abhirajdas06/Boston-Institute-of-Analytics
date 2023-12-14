from django.shortcuts import render
from django.http import HttpResponse


# #HttpResponse
# def home(request):
#     ''' View to return HttpResponse'''
#     return HttpResponse("Hello, Django!")


# Template Response
def home(request):
    ''' View to return Template Response'''
    return render(request, 'home/index.html')
