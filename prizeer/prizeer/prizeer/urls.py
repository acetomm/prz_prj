from django.contrib import admin
from django.urls import path, include

urlpatterns = [
	path('cprizeer/', include('cprizeer.urls')),
    path('admin/', admin.site.urls),
]
