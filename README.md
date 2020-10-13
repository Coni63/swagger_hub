
# Swagger HUB

This repository is proposing a very basing Django Application which provides a preview and link to multiple swagger definitions stored in the folder `/docs/`

![preview](https://github.com/Coni63/swagger_hub/blob/master/img/preview.png)
![structure](https://github.com/Coni63/swagger_hub/blob/master/img/structure.png)

## Installation

### Setup the environment

First, create in the virtual environment called `venv` and install all libraries in `environment.yml` with:

```
conda create env -f environment.yml
```
### Generate Statics

This is only required for deployment on server but not if you use the runserver command from django

```console
activate ./venv
python manage.py collectstatic
```

### Run the server for test

Everything is now set and you can run the server using:

```console
activate ./venv
python manage.py runserver 0.0.0.0:8000
```
### Access the UI

#### From the same computer as the one running the server
In this case, you can access it from *http://localhost:8000* or *http://127.0.0.1:8000*
#### From another device connected to the same network
In this other case, you can access it by entering the IP of the computer running the server such as *http://192.168.0.XX:8000/*

## Add Swagger

To add project, simply add a folder into `docs`. 
To add a swagger in the project, simply add the yml definition in the project
Refresh the page

## Futurs Updates

- Improve frontend design
- Convert Markdown to html for the rendering of the description

## Warning

- There should be only 1 level of project
- The yml *must* containt at least a `title`, `description` and `version` in the `info` part
