from django.urls import  path
from .views import  PostDetailView, PostLike,AddPostDataset,CreatePostView, PostListView
urlpatterns = [
    
    path('postcreate/', CreatePostView.as_view()),
    path('list/', PostListView.as_view() ),
    path('list/<int:id>/',  PostDetailView.as_view()),
    path('list/<int:id>/like/',  PostLike.as_view()),
    path('create/<int:post>',AddPostDataset.as_view()),
   
    #path('category/', CategoryCreateView.as_view()),
 


]