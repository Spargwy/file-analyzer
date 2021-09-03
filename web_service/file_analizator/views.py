import os

from django.shortcuts import render

from file_analizator.forms import FileForm
from django.http import JsonResponse

from file_analizator.utils import processing_file


def home_page(request):
    return render(request, 'file_analizator/home.html')


def upload_file(request):
    if request.method == "POST":
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            file = form.save()
            try:
                words = processing_file(file.file.name)
                return JsonResponse(words)
            except Exception as e:
                print("error in processing file: ", e)
                path = os.getcwd() + '/media/'
                os.remove(path + file.file.name)
    form = FileForm()
    return render(request, 'file_analizator/file_upload_page.html', {'form': form})
