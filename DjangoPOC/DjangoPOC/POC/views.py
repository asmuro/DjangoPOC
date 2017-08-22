from django.shortcuts import render

# Create your views here.
def poc_view(request):
        return render(request, 'POC/poc_view.html', {})