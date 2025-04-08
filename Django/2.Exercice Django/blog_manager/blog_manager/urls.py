from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls_functionnal_views')),
    path('cbv/', include('blog.urls_class_based_views')),
]

