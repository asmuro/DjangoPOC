from django.shortcuts import render
from .forms import UploadFileForm
from django import forms

# Create your views here.
def poc_view(request):
        return render(request, 'POC/poc_view.html', {})

def uploadFile_view(request):
    return render(request, 'POC/uploadFile_view.html', {})

def loadingUpload_view(request):
    if request.method == 'POST':
        a= 2
        #form = UploadFileForm(request.POST, request.FILES)
        #if form.is_valid():
        #    handle_uploaded_file(request.FILES['file'])
        #    return HttpResponseRedirect('/success/url/')
    else:
        form = UploadFileForm()
    return render(request, 'POC/result_view.html', {'form': form})

def result_view(request):
    return render(request, 'POC/result_view.html', {})
