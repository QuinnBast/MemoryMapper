# MemoryMapper Server
The MemoryMapper server is a python FastAPI server which facilitates storing user data. Most data is stored in minio as object storage, however, other data needs to be stored.
The server supports two methods of storage and can be configured through environment variables.

# Configuration

| Variable | Description | Default | Values |
| --- | --- | ---
| DATABASE_MODE | If the server should store data to a database or a file. | Database | `Database | File | MEMORY` |
| DATABASE_TYPE | If the server is storing to a database, the database provider | SQLITE | TODO: `None | SQL | SQLITE | REDIS` |
| MM_PORT | The port to expose the server on | 9000 | Int |


# Developing

The MemoryMapper server is a python server that uses FastAPI. To setup a development environment for the Server, [install Python](https://www.python.org/downloads/) on your machine. Once installed, create a virtual environment and install the requirements with:
```
cd Server
python -m venv ./venv
pip install -r requirements.txt
```

Start the API server and enable hot-reloads with the following command:
```
cd src
uvicorn main:app --reload --port 8000
```

For a production build, simply run `python main.py`