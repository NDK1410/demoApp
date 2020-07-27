from django.db import models
 
from django.http import HttpResponse
from .forms import UploadFileForm
from django.shortcuts import render, get_object_or_404
 
def UploaderView(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            upload(request.FILES['file'])
            return HttpResponse("<h2>File uploaded successful!</h2>")
        else:
            return HttpResponse("<h2>File uploaded not successful!</h2>")
 
    form = UploadFileForm()
    return render(request, 'uploader.html', {'form':form})
  
def upload(f): 
    file = open(f.name, 'wb+') 
    for chunk in f.chunks():
        file.write(chunk)