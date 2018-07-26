
from django.conf.urls import url
from art import views

urlpatterns = [
    url(r'^list/', views.list_art),
    url(r'^show/(\d+)/', views.show),
    url(r'^topRead/(\d+)/', views.topReadArt),
    url(r'^reading/(\d+)/', views.topReadArtResult),
]
