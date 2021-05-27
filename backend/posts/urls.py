from django.urls import  path
from .views import PostListView,PostDetailView, CategoryCreateView, UserPosts, PostLike
urlpatterns = [
    
    path('list/', PostListView.as_view()),
    path('list/<slug>/',  PostDetailView.as_view()),
    path('list/<slug>/like/',  PostLike.as_view()),
    path('userposts/',UserPosts.as_view()),
    path('category/', CategoryCreateView.as_view()),
 


]