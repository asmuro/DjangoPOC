from django.shortcuts import render
from .forms import UploadImageForm
from django import forms
from django.core.files.storage import FileSystemStorage

# Create your views here.
def poc_view(request):
        return render(request, 'POC/poc_view.html', {})

def uploadFile_view(request):
    return render(request, 'POC/uploadFile_view.html', {})

def loadingUpload_view(request):
    if request.method == 'POST':
        form = UploadImageForm(request.POST, request.FILES)
        #if form.is_valid():
        files = request.FILES.getlist('image')
        index = 1
        for f in files:
            fs = FileSystemStorage()
            filename = fs.save(f.name, f)
            if index == 1:
                uploaded_file_url_1 = fs.url(filename)
            elif index == 2:
                uploaded_file_url_2 = fs.url(filename)
            index = index + 1
        return render(request, 'POC/result_view.html', {'uploaded_file_url_1': uploaded_file_url_1})
            #m = ExampleModel.objects.get(pk=course_id)
            #m.model_pic = form.cleaned_data['image']
            #m.save()
            #return HttpResponse('image upload success')
            #return render(request, 'POC/result_view.html', {'form': form})
    else:
        return HttpResponseForbidden('allowed only via POST')
    return render(request, 'POC/result_view.html', {'form': form})

def result_view(request):
    return render(request, 'POC/result_view.html', {})
