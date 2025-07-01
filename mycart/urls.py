from django.contrib import admin
from django.urls import include, path
from shopy import views
from django.conf.urls.static import static 
from django.conf import settings 
from account import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('shopy.urls')),
    path('accounts/',include('account.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)