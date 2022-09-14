from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from .models import Post


def index(request):
    """ Returns index.html """
    return render(request, 'index.html')


class PostList(generic.ListView):
    """
    Displays postlist
    """
    model = Post
    queryset = Post.objects.order_by('-created_on')
    template_name = 'post_list.html'
    paginate_by = 6