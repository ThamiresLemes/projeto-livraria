from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    status = request.GET.get('status')
    return render(request,'index.html', {'status': status})