from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('finance/', include('finance.urls')),
    path('admin/', admin.site.urls),
]
