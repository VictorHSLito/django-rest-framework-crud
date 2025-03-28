from django.contrib import admin
from django.urls import include, path

from movies import views

# urls
urlpatterns = [
    path('api/v1/movies/', include('movies.urls')),
    path('api/v1/auth/', include('authentication.urls')),
    path('admin/', admin.site.urls),
    path("", views.index_page, name="index"),
    path("/movies", views.movies_view, name="movies-catalog")
]