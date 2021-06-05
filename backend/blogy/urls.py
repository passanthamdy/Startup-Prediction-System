from django.contrib import admin
from django.urls import path ,include ,re_path
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.authtoken import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/accounts/', include('accounts.urls')),
    path('summernote/', include('django_summernote.urls')),
    path('api/posts/', include('posts.urls')),
    path('api/profile/', include('profiles.urls')),
    


]
urlpatterns += [re_path(r'^.*', TemplateView.as_view(template_name='index.html'))]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)