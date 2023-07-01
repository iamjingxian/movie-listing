from django.shortcuts import render
from django.http import HttpResponse

# def index(request):
#     return HttpResponse("Hello world! Fill in Russell's part here.")

def index(request):
    return render(request,'about-us.html')
