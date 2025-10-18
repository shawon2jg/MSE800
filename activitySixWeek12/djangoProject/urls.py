from django.contrib import admin
from django.urls import path, include

# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('welcomeApp.urls')),  # include our app's URLs
]
