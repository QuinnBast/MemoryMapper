# MemoryMapper
A website to upload your memories and keep track of the moments that matter the most.

# Running a server
Hosting memory mapper is as simple as running our docker containers. MemoryMapper uses two docker containers, minio to store the uploaded images, and the MemoryMapper server.
If you have docker-compose, you can run MemoryMapper using docker-compose. Simply copy the `docker-compose.yaml` file to your machine and run a `docker compose up -d` to run MemoryMapper.

If you do not have docker-compose, you can alternatively start the docker containers individually. The following commands will start both of the containers:

```
docker run -p 9000:9000 -p 9001:9001 minio/minio server /data --console-address ":9001"
docker run ...
```

## Using a different object store

Minio is a ojbect store that is compatible with Amazon S3 cloud storage APIs. If you would prefer to use an AWS S3 bucket to host your files, this can also be done. To do this, the MemoryMapper config will need to be updated

# Development

## Server

The MemoryMapper server is a python server that uses FastAPI. To setup a development environment for the Server, [install Python](https://www.python.org/downloads/) on your machine. Once installed, create a virtual environment and install the requirements with:
```
cd Server
python -m venv .
pip install -r requirements.txt
```

Start the API server with. By default the server is exposed on port 8000.
```
uvicorn main:app --reload
```