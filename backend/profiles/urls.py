from django.urls import path
from .views import UpdateUserProfile, UserPostsView

urlpatterns = [
    
    path('<int:id>/', UpdateUserProfile.as_view()),
    path('posts/<int:user>/', UserPostsView.as_view()),


]