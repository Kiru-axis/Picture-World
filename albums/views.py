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

# search results view function
def search_results(request):

    if 'imagesearch' in request.GET and request.GET["imagesearch"]:
        category = request.GET.get("imagesearch")
        searched_images = Image.search_by_category(category)
        message = f"{category}"
        print(searched_images)
        return render(request, 'albums/search_results.html', {"message": message, "images": searched_images})
    else:
        message = "You haven't searched for any image category"
        return render(request, 'albums/search_results.html', {"message": message})