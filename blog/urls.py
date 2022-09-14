from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='home'),
    path('post_list/', views.PostList.as_view(), name='post_list')
]