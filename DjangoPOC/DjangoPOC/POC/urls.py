from django.conf.urls import include, url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
        url(r'^$', views.poc_view),
        url(r'^upload/', views.uploadFile_view),
        url(r'^loading/$', views.loadingUpload_view),
        url(r'^result/$', views.result_view),
        
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

