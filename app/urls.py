from . import views
from django.urls import re_path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    re_path(r'^$', views.images, name='images'),
    re_path(r'^home/$', views.home, name='home'),
    re_path(r'^search/$', views.search_results, name='search_results'),
    re_path(r'^image/(\d+)', views.image, name='image'),
    re_path(r'^Silicon_Valley/', views.Silicon_Valley, name='Silicon_Valley'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)