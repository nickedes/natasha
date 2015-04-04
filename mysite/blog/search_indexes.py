from haystack.indexes import *
from blog.models import posts


class postIndex(SearchIndex, Indexable):
    text = CharField(document=True, use_template=True)
    pub_date = DateTimeField(model_attr='timestamp')

    content_auto = EdgeNgramField(model_attr='title')

    def get_model(self):
        return posts

    def index_queryset(self, using=None):
        return self.get_model().objects.all()

site.register(posts, postIndex)
