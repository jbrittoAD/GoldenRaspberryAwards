import unittest
import csv
import json
from unittest.mock import patch
from app import create_app
from services.user_service import get_producers_with_intervals
from models import Movie

class TestRoutes(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()
        
        # Carrega os filmes do CSV
        self.mocked_movies = self.load_mocked_data("tests/mocked_movies.csv")
        
        # Carrega a resposta mockada da API do JSON
        with open("tests/mocked_response.json", "r") as f:
            self.mocked_response = json.load(f)

    def load_mocked_data(self, file_path):
        """Carrega os dados mockados do CSV e converte para uma lista de objetos Movie"""
        movies = []
        with open(file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=';')
            for row in reader:
                movies.append(Movie(
                    year=int(row["year"]),
                    title=row["title"],
                    studios=row["studios"],
                    producers=row["producers"],
                    winner=row["winner"].lower() == "yes"
                ))
        return movies

    @patch("services.user_service.get_producers_with_intervals")
    def test_producers_intervals(self, mock_service):
        """Testa a rota /producers sem depender do banco de dados"""

        # Simula a resposta do serviço baseado nos dados mockados do JSON
        mock_service.return_value = self.mocked_response

        response = self.client.get('/producers')
        data = response.get_json()

        # Exibe as diferenças se o teste falhar
        print("Esperado:", self.mocked_response)
        print("Recebido:", data)

        # Testa se a resposta é a esperada
        self.assertEqual(data, self.mocked_response)

        # Testa se a API retorna status 200
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
