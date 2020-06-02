from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from . import views

app_name = 'art_app'

urlpatterns = [
    
    path('', views.index, name='index'),
    path('<int:page>/', views.index_page, name='index-page'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
