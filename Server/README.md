# MemoryMapper Server
The MemoryMapper server is a python FastAPI server which facilitates storing user data. Most data is stored in minio as object storage, however, other data needs to be stored.
The server supports two methods of storage and can be configured through environment variables.

# Configuration

| Variable         | Description                                                                                      | Default                     | Values                        |
|------------------|--------------------------------------------------------------------------------------------------|-----------------------------|-------------------------------|
| MM_DATABASE_MODE | If the server should store data to a database or a file.                                         | Database                    | `Database,File`        |
| MM_PORT          | The port to expose the server on                                                                 | 8000                        | Int                           |
| MM_DBAPI_STRING  | A database connection string to connect via DBAPI. [Supported dialects](https://docs.sqlalchemy.org/en/14/dialects/). Defaults to use an in memory sqlite database. | sqlite+pysqlite:///:memory: | String                        | 


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