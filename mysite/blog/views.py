from django.shortcuts import render_to_response

from blog.models import posts
from haystack.query import SearchQuerySet
# Create your views here.


def home(request):
    enteries = posts.objects.all()
    return render_to_response('index.html', {'posts': enteries})

def search_titles(request):
	post = SearchQuerySet().autocomplete(content_auto=request.POST.get('search_text', ''))

	return render_to_response('index.html', {'posts': posts})