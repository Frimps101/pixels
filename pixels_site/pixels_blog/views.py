from django.shortcuts import render
from .models import Post

# Create your views here.
def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'pixels_blog/home.html', context)

def about(request):
    return render(request, 'pixels_blog/about.html', {'title': 'About'})