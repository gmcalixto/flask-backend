# Flask CRUD com SQLite

Este projeto implementa uma API REST em Flask integrada com um banco de dados SQLite para gerenciar registros de pessoas.

## Tecnologias Utilizadas

- Python 3
- Flask
- Flask-CORS
- SQLite3

## Instalação

1. Clone o repositório:
   ```sh
   git clone https://github.com/seu-usuario/seu-repositorio.git
   cd seu-repositorio
   ```

2. Crie um ambiente virtual (opcional, mas recomendado):
   ```sh
   python -m venv venv
   source venv/bin/activate  # No Windows: venv\Scripts\activate
   ```

3. Instale as dependências:
   ```sh
   pip install flask flask-cors
   ```

4. Crie o banco de dados e a tabela:
   ```sh
   python
   >>> import sqlite3
   >>> conn = sqlite3.connect('crud.db')
   >>> cursor = conn.cursor()
   >>> cursor.execute('''CREATE TABLE pessoa (
   ... nome TEXT NOT NULL,
   ... sobrenome TEXT NOT NULL,
   ... cpf TEXT PRIMARY KEY,
   ... data_nascimento TEXT NOT NULL
   ... )''')
   >>> conn.commit()
   >>> conn.close()
   ```

## Como Executar

1. Inicie o servidor Flask:
   ```sh
   python app.py
   ```

2. O servidor estará rodando em:
   ```
   http://localhost:5000
   ```

## Endpoints

### Listar todas as pessoas
- **Rota:** `/pessoas`
- **Método:** `GET`
- **Resposta:**
  ```json
  [
    {
      "nome": "João",
      "sobrenome": "Silva",
      "cpf": "12345678900",
      "data_nascimento": "1990-01-01"
    }
  ]
  ```

### Buscar uma pessoa pelo CPF
- **Rota:** `/pessoa/<cpf>`
- **Método:** `GET`
- **Resposta:**
  ```json
  {
    "nome": "João",
    "sobrenome": "Silva",
    "cpf": "12345678900",
    "data_nascimento": "1990-01-01"
  }
  ```

### Inserir ou Atualizar uma pessoa
- **Rota:** `/pessoa`
- **Método:** `POST`
- **Corpo da requisição:**
  ```json
  {
    "nome": "Maria",
    "sobrenome": "Oliveira",
    "cpf": "98765432100",
    "data_nascimento": "1985-05-20"
  }
  ```
- **Resposta:**
  ```json
  { "success": "Pessoa inserida com sucesso" }
  ```

### Remover uma pessoa pelo CPF
- **Rota:** `/pessoa/<cpf>`
- **Método:** `DELETE`
- **Resposta:**
  ```json
  { "success": "Pessoa deletada com sucesso" }
  ```

## Autor

Seu Nome - [LinkedIn](https://www.linkedin.com/in/seu-perfil/)
