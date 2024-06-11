from django.shortcuts import render

# Create your views here.

def starting_page(request):
    return render(request, "blog/index.html")

def posts(request):
    return render(request, "blog/all-skills.html")

def post_details(request, slug):
    return render(request, "blog/skill-detail.html")
