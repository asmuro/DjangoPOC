from django.shortcuts import render
from .forms import UploadImageForm
from django import forms
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from POC import generate_npz_process

# Create your views here.
def poc_view(request):
    return render(request, 'POC/poc_view.html', {})

def uploadFile_view(request):
    fs = FileSystemStorage(location=settings.MEDIA_ROOT)
    
    for file in fs.listdir(fs.location)[1]:
        fs.delete(file)
    return render(request, 'POC/uploadFile_view.html', {})

def loadingUpload_view(request):
    if request.method == 'POST':
        form = UploadImageForm(request.POST, request.FILES)
        #if form.is_valid():
        files = request.FILES.getlist('image')
        if len(files) > 5:
            return render(request, 'POC/uploadFile_view.html', {'error_info': 'No se pueden evaluar más de 5 fotos'})
        elif len(files) == 0:
            return render(request, 'POC/uploadFile_view.html', {'error_info': 'Debe seleccionar por lo menos una imagen'})
        index = 1
        paths = []
        for f in files:
            fs = FileSystemStorage()
            filename = fs.save(f.name, f)
            if index == 1:
                uploaded_file_url_1 = fs.url(filename)
            elif index == 2:
                uploaded_file_url_2 = fs.url(filename)
            paths.append(settings.MEDIA_ROOT + '\\' + f.name)
            index = index + 1

        generate_npz_process.generate_npz_process.createNPZ(paths, settings.MEDIA_ROOT)
        return render(request, 'POC/result_view.html', {'uploaded_file_url_1': uploaded_file_url_1, 'uploaded_file_url_2': uploaded_file_url_2})
            
    else:
        return HttpResponseForbidden('allowed only via POST')
    return render(request, 'POC/result_view.html', {'form': form})

def result_view(request):
    return render(request, 'POC/result_view.html', {})
