from django.conf import settings
from django.conf.urls.static import static

from django.urls import path
from . import views

urlpatterns = [
    path('women_outerwear', views.catalog, name='women_outerwear'),
    path('mens_outerwear', views.catalog, name='mens_outerwear'),
    path('women_accessories', views.catalog, name='women_accessories'),
    path('mens_accessories', views.catalog, name='mens_accessories'),
    path('ask_Men', views.ask_Men, name='ask_Men'),
    path('ask_Women', views.ask_Women, name='ask_Women'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)