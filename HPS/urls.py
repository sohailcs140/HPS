from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import (handler400,
                              handler404, 
                              handler403, 
                              handler500
                              )
from .import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.HomeView, name='home'),
    path('get-started/', views.Get_Started, name='started'),
    path('accounts/', include('allauth.urls')),
    path('core/', include('core.urls')),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


handler400 = views.get_400
handler404 = views.get_404
handler403 = views.get_403
handler500 = views.get_500