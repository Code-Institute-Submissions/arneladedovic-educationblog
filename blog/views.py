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


class PostDetail(View):
    """
    Displays detailpost
    """

    def get(self, request, slug, *args, **kwargs):
        """
        Gets detailed post
        """
        queryset = Post.objects
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.order_by("created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )