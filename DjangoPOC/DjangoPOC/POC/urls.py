from django.conf.urls import include, url
from . import views

urlpatterns = [
        url(r'^$', views.poc_view),
        url(r'^upload/', views.uploadFile_view),
        url(r'^loading/$', views.loadingUpload_view),
        url(r'^result/$', views.result_view),
    ]