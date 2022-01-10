from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('calculadora/', include('calculadora.urls')),
    path('admin/', admin.site.urls),
]
