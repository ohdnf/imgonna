from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('articles/', include('articles.urls')),
    # path('movies/', include('movies.urls')),
    # path('reviews/', include('reviews.urls')),

    # rest-auth
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/signup/', include('rest_auth.registration.urls')),
]
