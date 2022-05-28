from django.shortcuts import render
from .models import Image, Location

def index(request):
    images = Image.objects.all()
    locations = Location.get_locations()
    return render(request, 'photos/index.html', {'images': images[::-1], 'locations': locations})


def search_results(request):
    if 'imagesearch' in request.GET and request.GET["imagesearch"]:
        category = request.GET.get("imagesearch")
        searched_images = Image.search_by_category(category)
        message = f"{category}"
        return render(request, 'photos/search_results.html', {"message": message, "images": searched_images})
    else:
        message = "You haven't searched for any image category"
        return render(request, 'photos/search_results.html', {"message": message})

def location_img(request, location):
    images = Image.filter_by_location(location)
    return render(request, 'photos/images.html', {'location_images': images})