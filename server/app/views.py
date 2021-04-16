from django.shortcuts import render, redirect
from .models import*
# Create your views here.


def index(request):
    context = {
        'all_files': File.objects.all()
    }
    return render(request, 'index.html', context)


def upload(request):
    uploaded_file = request.FILES
    new_upload = File.objects.create(
        file_name=request.POST['file_name'],
        image=uploaded_file['image']
    )
    return redirect('/')
