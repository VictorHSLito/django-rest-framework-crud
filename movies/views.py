from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from django_filters import rest_framework as filters
from django.shortcuts import render
from .models import Movie
from .permissions import IsOwnerOrReadOnly
from .serializers import MovieSerializer
from .pagination import CustomPagination
from .filters import MovieFilter


class ListCreateMovieAPIView(ListCreateAPIView):
    serializer_class = MovieSerializer
    queryset = Movie.objects.all()
    permission_classes = [IsAuthenticated]
    pagination_class = CustomPagination
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = MovieFilter

    def perform_create(self, serializer):
        # Assign the user who created the movie
        serializer.save(creator=self.request.user)


class RetrieveUpdateDestroyMovieAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = MovieSerializer
    queryset = Movie.objects.all()
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]


def index_page(request):
    return render(request, 'movies_pages/index.html')


def movies_view(request):
    movies = Movie.objects.all()  # Pega todos os objetos filmes registrados no banco
    context = {"movies": movies}  # Cria um dicionário com esses objetos e passa eles para o template/view
    return render(request, "movies_pages/movies.html", context)


def single_movie_view(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    context = {"movie": movie}
    return render(request, "movies_pages/movie.html", context)
