from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from movies.models import Movie


class MovieAPITest(TestCase):
    def setUp(self):
        # Prepara o ambiente de testes
        self.client = APIClient()
        self.user = User.objects.create_user(username="user", password="password")
        self.client.force_authenticate(user=self.user)

        self.filme = Movie.objects.create(
            title="Filme teste",
            genre="Comedy",
            year=2024,
            creator=self.user
        )

    def test_criar_filme(self):
        """Testa se a API permite criar um novo filme."""
        data = {
            "title": "Filme teste 2",
            "genre": "Comedy",
            "year": 2025
        }
        response = self.client.post("/api/v1/movies/", data)
        self.assertEqual(response.status_code, 201)  # Espera status 201 (Criado)
        self.assertEqual(Movie.objects.count(), 2)  # Agora temos 2 filmes no banco

    def test_listar_filmes(self):
        """Testa se a API retorna a lista de filmes corretamente"""
        response = self.client.get("/api/v1/movies/")
        self.assertEqual(response.status_code, 200)  # Espera status 200 (OK)
        self.assertGreater(len(response.json()), 0)  # Lista deve ter ao menos 1 item

    def test_requisicao_sem_autenticacao(self):
        """Testa se um usuário não autenticado recebe erro 401"""
        client = APIClient()  # Cliente sem autenticação
        response = client.get("/api/v1/movies/")
        self.assertEqual(response.status_code, 401)  # Espera erro 401 (Unauthorized)

    def test_criar_filme_sem_creator(self):
        """Testa se a API retorna erro ao tentar criar um filme sem um criador"""
        client = APIClient()
        data = {
            "title": "Filme sem creator",
            "genre": "Action",
            "year": 2025
        }
        response = client.post("/api/v1/movies/", data)
        self.assertEqual(response.status_code, 401)

    def test_deletar_filme(self):
        """Testa se a API permite deletar um filme existente"""
        response = self.client.delete(f"/api/v1/movies/{self.filme.id}/")
        self.assertEqual(response.status_code, 204)
        self.assertFalse(Movie.objects.filter(id=self.filme.id).exists())

    def test_atualizar_filme(self):
        """Testa se a API permite atualizar um filme existente"""
        data = {
            "title": "Filme Atualizado",
            "genre": "Drama",
            "year": 2023
        }
        response = self.client.put(f"/api/v1/movies/{self.filme.id}/", data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Movie.objects.get(id=self.filme.id).title, "Filme Atualizado")

    def test_detalhar_filme(self):
        """Testa se a API retorna os detalhes de um filme específico"""
        response = self.client.get(f"/api/v1/movies/{self.filme.id}/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["title"], "Filme de Teste")
