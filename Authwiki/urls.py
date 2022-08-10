from ast import pattern
from django.urls import path
from .views import Documentation, IndexView, ContactView, Library, Library2
urlpatterns = [
path('', IndexView.as_view(), name='index'),
path('contact-us/', ContactView.as_view(), name='Contact'),
path('library/', Library.as_view(), name='Library'),
path('library/library2/', Library2.as_view(), name='Library2'),
path('Documentation/', Documentation.as_view(), name='Documentation'),
]
