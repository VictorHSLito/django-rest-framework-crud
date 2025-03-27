# Projeto de teste em Python usando pytest

Este projeto em python utiliza o Django REST Framework para criar uma API CRUD(Create,read,update,delete).
Nesse projeto adicionamos o pytest para testar as models, serializers e endpoints.


Rodar todos os testes utiliza o comando:
pytest


# INTRODUCAO AOS TESTES
Este projeto utiliza testes automatizados para garantir a funcionalidade e confiabilidade.



# PLANEJAMENTO DE TESTES
Objetivo:Garantir que o modelo Movie funciona de forma correta e retorne o resultado desejado.
Ferramentas:Utilizamos o framework de testes do Django para configurar e validar os testes.


# DESCRICAO DOS CASOS DE TESTES

°Models
O arquivo Teste.models.py no codigo tem como objetivo verificar a funcionalidade do modelo Movie dentro do projeto Django.Ele verifica a criacao do modelo Movie e representação em string


# DETALHES DOS TESTES e CODIGO

Nome do arquivo  **test.models.py**

from django.test import TestCase  # Teste base do Django
from movies.models import Movie  # Modelo Movie
from django.contrib.auth.models import User  # Modelo User

class MovieModelTest(TestCase):  # Classe de teste para Movie
def setUp(self):  # Configuracao inicial
self.user = User.objects.create_user(username="user", password="password")  # Cria um usuario
self.movie = Movie.objects.create(  # Cria um filme associado ao usuário
title="Filme de Teste",  # Título do filme
genre="Comedy",         # Gênero do filme
year=2024,              # Ano do filme
creator=self.user       # Criador do filme
        )

def test_movie_creation(self):  # Testa criação do filme
self.assertEqual(self.movie.title, "Filme de Teste")  # Verifica titulo
self.assertEqual(self.movie.genre, "Comedy")          # Verifica genero
self.assertEqual(self.movie.year, 2024)               # Verifica ano
self.assertEqual(self.movie.creator, self.user)       # Verifica criador

def test_movie_str_representation(self):  # Testa representacao em string
self.assertEqual(str(self.movie), "Filme de Teste")  # Retorno esperado
