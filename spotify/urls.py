
from django.contrib import admin
from django.urls import path

from music.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HelloAPI.as_view()),
    path('qoshiqchi/<int:pk>/', QoshiqchiApi.as_view()),
    path('albomlar/', AlbomlarApi.as_view()),
    path('albom/<int:pk>/', AlbomApi.as_view()),
    path('qoshiqlar/', QoshiqlarApi.as_view()),
    path('qoshiq/<int:pk>/', QoshiqApi.as_view()),
]
