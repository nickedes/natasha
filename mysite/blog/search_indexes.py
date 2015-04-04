from haystack.indexes import *
from .models import posts
# from haystack import site


class postIndex(SearchIndex, Indexable):
    text = CharField(document=True, use_template=True)
    title = CharField(model_attr='title')
    content_auto = EdgeNgramField(model_attr='title')

    def get_model(self):
        return posts

    def index_queryset(self, using=None):
        return self.get_model().objects.all()

# site.register(posts, postIndex)
