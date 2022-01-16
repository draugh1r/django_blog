from django.shortcuts import render
from django.views import generic
from .models import Post
# Create your views here.

class IndexView(generic.ListView):
    template_name = 'posts/index.html'
    context_object_name = 'latest_post'

    def get_queryset(self):
        """Return the last five published posts."""
        return Post.objects.order_by('-published_date')[:5]
    
class DetailView(generic.DetailView):
    model = Post
    template_name = 'posts/post_detail.html'