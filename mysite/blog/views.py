from django.shortcuts import render_to_response

from blog.models import posts

# Create your views here.


def home(request):
	
	e = posts.objects.all()[:2]
    return render_to_response('index.html', {'posts' : e})