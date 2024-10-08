from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from produto import views
from produto.views import Produto


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.home, name='home'),
    path(" ", include('produto.urls')),
    path("cadastro/", include('cadastro.urls')),

]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)