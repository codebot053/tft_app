from django.http import HttpResponse
from django.shortcuts import render

def base_response(request):
    return HttpResponse("test")

def test(request):
    return render(request,"test.html")

def sign_in(request):
    return render(request,"account/signin.html")

def sign_up(request):
    return render(request,"account/signup.html")
