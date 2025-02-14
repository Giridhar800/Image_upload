from django.shortcuts import render
from django.http import HttpResponse
from .models import ImageUploadModel
from .forms import ImageUploadForm

# Create your views here.

def upload_file(request):
    if request.method == "POST":
        form = ImageUploadForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse("<h2> Image upload successfully..</h2>")
    else:
        form = ImageUploadForm()
        images = ImageUploadModel.objects.all()
        return render(request,'index.html',{'form':form,'images':images})
