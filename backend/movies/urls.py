from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('', views.movie_list),
    path('<int:movie_pk>/', views.movie_detail),
    path('<int:movie_pk>/rating/', views.rating_get_create),
    path('<int:movie_pk>/rating/<int:rating_pk>/', views.rating_update_delete),
]