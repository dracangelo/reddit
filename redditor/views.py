from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required





@login_required
def landing(request):
    
  
    return render(request,'index.html')