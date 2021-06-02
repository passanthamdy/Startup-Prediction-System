from django.urls import  path
from .views import PostListView,PostDetailView, PostLike
urlpatterns = [
    
    path('list/', PostListView.as_view()),
    path('list/<int:id>/',  PostDetailView.as_view()),
    path('list/<int:id>/like/',  PostLike.as_view()),
   
    #path('category/', CategoryCreateView.as_view()),
 


]