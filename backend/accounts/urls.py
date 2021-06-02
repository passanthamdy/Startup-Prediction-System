from django.urls import path,include
from rest_framework_simplejwt import views as jwt_views
from .views import ObtainTokenPairWithColorView ,CreateCustomUser,HelloWorldView,CheckEmailExisting
from rest_framework.routers import DefaultRouter

router = DefaultRouter(trailing_slash=False)
#router.register("profile", UserProfileView)

urlpatterns = [
    path('', include(router.urls)),
    path('sign_up/email/',CheckEmailExisting.as_view(),name="emailexisting"),
    path('users/create/', CreateCustomUser.as_view(), name="create_user"),
    path('token/obtain/', ObtainTokenPairWithColorView.as_view(), name='token_create'),  
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('hello/', HelloWorldView.as_view(), name='hello_world'),
]