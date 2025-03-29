from django.contrib import admin
from django.urls import include, path, re_path

from movies import views

# urls
urlpatterns = [
    path('api/v1/movies/', include('movies.urls')),
    path('api/v1/auth/', include('authentication.urls')),
    path('admin/', admin.site.urls),
    path("", views.index_page, name="index"),
    path("movies", views.movies_view, name="movies-catalog"),
    re_path(r"^movies/(?P<movie_id>\d+)/$", views.single_movie_view, name="movie-information")  # Para rotas que
    # precisam de parâmetros deve-se usar expressões regulares,
    # leia: https://docs.djangoproject.com/en/5.1/topics/http/urls/#using-regular-expressions
]