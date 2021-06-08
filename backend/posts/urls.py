from django.urls import  path
from .views import  PostDetailView, PostLike,AddPostDataset,CreatePostView, PostListView
urlpatterns = [
    
    path('postcreate/', CreatePostView.as_view()), #to add post data like img and content bla
    path('postcreate/<int:id>/',AddPostDataset.as_view()),#to add dataset to be predicted
    path('list/', PostListView.as_view() ), #to list all posts
    path('list/<int:id>/',  PostDetailView.as_view()), #to get post, update and delete 
    path('list/like/<int:id>/',  PostLike.as_view()),
     


]