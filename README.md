# fastapi-postgres-startkit
Using this repository, you can easily start a REST API server.
This server will automatically create an OpenAPI json file and can be checked in [localhost/redoc](localhost/redoc) after startup.
If you want to use this startkit, you need to use [Docker](https://docs.docker.jp/).

## Easy Start
1. Clone this repository and run the command.
  ```sh
  # init start
  docker-compose up --build

  # start after the second time
  docker-compose up
  ```
2. Open your browser and go to [http://localhost/countries?country_id=1](http://localhost/countries?country_id=1).
3. You can get the results of the RESTAPI.

## Directory Structure

### `/pgsql/init`
The directory that contains the SQL file to be executed when the RESTAPI is first started.
Currently, `init.sql` will be executed.
### `/pgsql/data`
It is created when the RESTAPI is first started, and it persists postgres.
### `/fastapi/router`
`router.py` will be the entry point for routing.
The subfile calls `/fastapi/database` to retrieve the data.
### `/fastapi/database`
The directory for executing SQL commands to the database.
### `/fastapi/middleware`
This is the directory that defines the middleware that will be executed when the request is retrieved.
### `/fastapi/openapi`
This is the directory for defining the types to be displayed in OPENAPI.
### `/fastapi/utils`
Other utility directory.