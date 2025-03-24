from django.test import TestCase  # Teste base do Django
from movies.models import Movie  # Modelo Movie
from django.contrib.auth.models import User  # Modelo User


class MovieModelTest(TestCase):  # Classe de teste para Movie
    def setUp(self):  # Configuracao inicial
        self.user = User.objects.create_user(username="user", password="password")  # Cria um usuário
        self.movie = Movie.objects.create(  # Cria um filme associado ao usuário
            title="Filme de Teste",  # Título do filme
            genre="Comedy",  # Gênero do filme
            year=2024,  # Ano do filme
            creator=self.user)  # Criador do filme

    def test_movie_creation(self):  # Testa criação do filme
        self.assertEqual(self.movie.title, "Filme de Teste")  # Verifica titulo
        self.assertEqual(self.movie.genre, "Comedy")  # Verifica genero
        self.assertEqual(self.movie.year, 2024)  # Verifica ano
        self.assertEqual(self.movie.creator, self.user)  # Verifica criador

    def test_movie_str_representation(self):  # Testa representacao em string
        self.assertEqual(str(self.movie.title), "Filme de Teste")  # Retorno esperado