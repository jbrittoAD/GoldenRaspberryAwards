# Golden Raspberry Awards

GoldenRaspberryAwards é uma aplicação que fornece informações sobre produtores de filmes vencedores do Golden Raspberry Awards, incluindo intervalos extremos de tempo entre vitórias consecutivas.


## Estrutura do Projeto

```plaintext
GoldenRaspberryAwards/
├── app.py
├── config.py
├── database
│   └── movielist.csv
├── instance
│   ├── config.py
│   └── database.db
├── models.py
├── README.md
├── requirements.txt
├── routes
│   ├── auth.py
│   ├── __init__.py
│   ├── main.py
├── services
│   ├── auth_service.py
│   ├── __init__.py
│   ├── __pycache__
│   └── user_service.py
└── tests
    ├── __init__.py
    ├── test_app.py
    ├── test_models.py
    └── test_routes.py
```

## Instalação

1. Clone o repositório:
    ```bash
    git clone https://github.com/jbrittoAD/GoldenRaspberryAwards.git
    cd GoldenRaspberryAwards
    ```

2. Crie e ative um ambiente virtual:
    ```bash
    python3 -m venv .venv
    source .venv/bin/activate
    ```

3. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

## Configuração (como descrito no projeto, o banco pode ser substituido, então criei esse tópico para customização)

1. Configure o schema do banco de dados conforme necessário em `models.py`.

2. Certifique-se de que o banco de dados está configurado corretamente caso o CSV fornecido (`database/movielist.csv`) foi substituido por outro banco.

## Executando a Aplicação

Para executar a aplicação, utilize o seguinte comando:
```bash
python app.py
```

A aplicação estará disponível em `[http://127.0.0.1:5000/producers]`.

## Pré testes
Caso o banco e o modelo seja modificado, deve-se modificar o json utilizado nos testes, mais exatamente localizado em "tests/test_routes.py"

## Executando Testes

Para executar os testes, utilize o seguinte comando:
```bash
pytest -s
```

## Verificando a Cobertura de Testes

Para verificar a cobertura de testes, utilize o seguinte comando:
```bash
pytest --cov=services --cov-report=term-missing --cov-report=html
```

Um relatório detalhado de cobertura será gerado no diretório `htmlcov`. Abra o arquivo `htmlcov/index.html` no seu navegador para visualizar o relatório.

## Endpoints da API

### `/producers` [GET]

Retorna os produtores com os maiores e menores intervalos entre vitórias consecutivas.

**Exemplo de resposta:**
```json
{
  "min": [
    {
      "producer": "Producer 1",
      "interval": 1,
      "previousWin": 2008,
      "followingWin": 2009
    },
    {
      "producer": "Producer 2",
      "interval": 1,
      "previousWin": 2018,
      "followingWin": 2019
    }
  ],
  "max": [
    {
      "producer": "Producer 3",
      "interval": 99,
      "previousWin": 1900,
      "followingWin": 1999
    },
    {
      "producer": "Producer 4",
      "interval": 99,
      "previousWin": 2000,
      "followingWin": 2099
    }
  ]
}
```

## Licença

Este projeto está licenciado sob os termos da licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

## Contribuição

1. Fork o repositório.
2. Crie uma branch para a sua feature (`git checkout -b feature/nova-feature`).
3. Commit suas mudanças (`git commit -m 'Adiciona nova feature'`).
4. Faça push para a branch (`git push origin feature/nova-feature`).
5. Abra um Pull Request.

---

**Autor:** João Carlos Britto filho

**Contato:** joaocarlosbrittofilho@gmail.com
