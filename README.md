# DevOps Apprenticeship: Project Exercise

## Documentation - Diagrams

To read the diagrams located in diagrams.md either install Java and  the [Markdown Preview Enhanced](https://github.com/shd101wyy/vscode-markdown-preview-enhanced) extension for VSCode or cut and paste the code between the PUML code delimiters to the [PlantUML Webserver](http://www.plantuml.com/plantuml/uml/SyfFKj2rKt3CoKnELR1Io4ZDoSa70000)
For ease I have also added a PNG version in the documentation folder.

## System Requirements

The project uses poetry for Python to create an isolated environment and manage package dependencies. To prepare your system, ensure you have an official distribution of Python version 3.7+ and install poetry using one of the following commands (as instructed by the [poetry documentation](https://python-poetry.org/docs/#system-requirements)):

### Poetry installation (Bash)

Local
Installed by Vagrant
Doc

## Dependencies

All dependencies will be deployed into the VM by vagrant or into the container by docker

## Running the App

### With Vagrant creating a VM

Simply run kick vagrant into life with

``` bash
$ vagrant up
$ vagrant ssh
```

### As a docker

Remove all stopped docker containers with `docker rm $(docker ps -a -q)`

#### Development

Build the image with  
`docker build --target dev --tag todo:dev .`  
Run the container with  
`docker run -p 1000:5000 --env-file .env --mount type=bind,source="$(pwd)"/todoapp,target=/todoapp todo:dev`
The development site will now be available at [`http://localhost:1000/`](http://localhost:9000/)

#### Testing

Build the image with  
`docker build --target test --tag todo:test .`  
Run the container with  
`docker run -p 2000:5000 --env-file .env --mount type=bind,source="$(pwd)"/todoapp,target=/todoapp todo:test todoapp`
The development site will now be available at [`http://localhost:2000/`](http://localhost:9000/)

#### Production

Build the image with  
`docker build --target prod --tag todo:prod .`  
Run the container with  
`docker run -p 8000:8000 --env-file .env todo:prod`

The production site will now be available at [`http://localhost:8000/`](http://localhost:8000/)

You should see python installing and output similar to the following:

```bash
 * Serving Flask app "app" (lazy loading)
 * Environment: development
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with fsevents reloader
 * Debugger is active!
 * Debugger PIN: 226-556-590
```

Now visit [`http://localhost:5000/`](http://localhost:5000/) in your web browser to view the app.

### Notes

The `.env` file is used by flask to set environment variables when running `flask run`. This enables things like development mode (which also enables features like hot reloading when you make a file change).

There's also a [SECRET_KEY](https://flask.palletsprojects.com/en/1.1.x/config/#SECRET_KEY) variable which is used to encrypt the flask session cookie.

Create the .env file for the first time by running `cp .env.template .env`

.env file should contain the following keys that are excluded from the git synch by .gitignore
 
 - FLASK_APP
 - FLASK_ENV
 - SECRET_KEY
 - TRELLO_KEY
 - TRELLO_TOKEN
 - TRELLO_TODO
 - TRELLO_DOING
 - TRELLO_DONE


