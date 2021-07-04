from django.shortcuts import render
from django.http  import HttpResponse,Http404
from .models import Location,Image

# Create your views here.
def index(request):
    context ={
        "images":Image.objects.all(),
        "locations": Location.get_locations(),
        "title": "Picture World"
    }
    return render(request, 'albums/index.html',context=context)

# view for image location
def image_location(request, location):

    context = {
        "images":Image.filter_by_location(location)
    }
    
    images = Image.filter_by_location(location)
    print(images)
    return render(request, 'albums/location.html', context)
