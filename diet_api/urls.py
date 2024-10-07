from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from plan.views import BookViewset

router = DefaultRouter()
router.register(r'books', BookViewset)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
