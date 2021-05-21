from django.urls import  path
from .views import PostListView,PostDetailView, CategoryCreateView
urlpatterns = [
    
    path('posts/', PostListView.as_view()),
    path('posts/<slug>/',  PostDetailView.as_view()),
    path('category', CategoryCreateView.as_view()),
 


]