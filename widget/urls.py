from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^search$', views.Search.as_view(), name='search'),
    url(r'^generator$', views.IDGenerator.as_view(), name='generator'),
    url(r'^$', views.Dashboard.as_view(), name='dashboard'),
]
