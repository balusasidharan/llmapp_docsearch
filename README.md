# DocSearch LLM App

## Prerequisites

- Python 3.8+
- [PostgreSQL](https://www.postgresql.org/) with [pgvector extension](https://github.com/pgvector/pgvector)
- [Ollama](https://ollama.com/) installed and running (for local LLM inference)
- (Optional) [git](https://git-scm.com/) for cloning the repo

## Setup Instructions

### 1. Clone the Repository
```sh
git clone <your-repo-url>
cd docsearch
```

### 2. Create and Activate a Virtual Environment
```sh
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Python Dependencies
```sh
pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Set Up PostgreSQL with pgvector
- Ensure PostgreSQL is running.
- Create a database (e.g., `docsearch`).
- Enable the `pgvector` extension:
  ```sql
  CREATE EXTENSION IF NOT EXISTS vector;
  ```
- Set the connection string as an environment variable:
  ```sh
  export PGVECTOR_CONNECTION_STRING="postgresql://<user>:<password>@localhost:5432/docsearch"
  ```

### 5. Prepare Ollama and Model
- Install Ollama from [https://ollama.com/](https://ollama.com/)
- Pull the desired model (e.g., deepseek-r1:7b):
  ```sh
  ollama pull deepseek-r1:7b
  ```

### 6. Index Your Documents
- Place your documents (PDFs, text files) in a folder (e.g., `vectordocs/`).
- Run the indexer script to populate the database:
  ```sh
  python postgres_indexer.py
  ```

### 7. Start the FastAPI Application
```sh
uvicorn app:app --reload
```

### 8. Query the API
Send a POST request to `/search/`:
```sh
curl -X POST http://localhost:8000/search/ \
     -H "Content-Type: application/json" \
     -d '{"q":"Your question here"}'
```

## Notes
- Make sure your Postgres user has permission to create extensions and tables.
- The embedding model and Ollama model can be changed in the code as needed.
- For production, configure environment variables and security as appropriate.

## Troubleshooting
- If you see errors about missing columns, ensure your database schema matches the latest code.
- If you see errors about missing Python packages, re-run `pip install -r requirements.txt`.
- For Ollama issues, ensure the Ollama server is running and the model is pulled. 