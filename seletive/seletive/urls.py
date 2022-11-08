from django.contrib import admin
from django.urls import path, include
# importar include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', include('empresa.urls')),
]
