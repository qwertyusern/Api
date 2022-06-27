
from django.contrib import admin
from django.urls import path, include

from music.views import *
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register("qoshiqchilar", QoshiqchilarVS)
router.register("albomlar", AlbomlarVS)
router.register("qoshiqlar", AlbomlarVS)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('qoshiqchilar', include(router.urls)),
    path('albomlar/', include(router.urls)),
    path('qoshiqlar/', include(router.urls)),

]

