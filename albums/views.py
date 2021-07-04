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
