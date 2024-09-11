from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from produto import views
from produto.views import lista_produtos


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.home, name='home'),
    path("produtos/", views.lista_produtos, name='lista_produtos'),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
