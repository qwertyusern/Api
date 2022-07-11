
from django.contrib import admin
from django.urls import path, include

from music.views import *
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)




# router=DefaultRouter()
# router.register("qoshiqchilar", QoshiqchilarVS)
# router.register("albomlar", AlbomlarVS)
# router.register("qoshiqlar", AlbomlarVS)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('qoshiqchilar/', QoshiqchilarListCreate),
    path('qoshiqchi/<int:pk>/', Qoshiqchi),
    path('albomlar/', AlbomlarListCreate),
    path('albom/<int:pk>/', Albom),
    # path('', include(router.urls)),
    # path('token-ber', TokenObtainPairView.as_view(), name='token_olish'),
    # path('token-yangila', TokenRefreshView.as_view(), name='token_yangilash'),
]

