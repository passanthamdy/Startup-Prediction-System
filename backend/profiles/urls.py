from django.urls import path
from .views import UpdateUserProfile, UserPostsView

urlpatterns = [
    
    path('update/', UpdateUserProfile),
    path('posts/<int:user>/', UserPostsView.as_view()),


]