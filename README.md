
## Movie site app

Site that displays the most popular movies and allows one to search for a movie by entering the name in a search bar.
App created in python/flask.Webpages rendered using HTML,CSS and Jinja2 templating.App uses TheMovieDB API for searching for and displaying information about movies -   https://developers.themoviedb.org/3/getting-started/introduction .To replicate this project you would need an API key from the TheMovieDB site.
![Project Name](https://user-images.githubusercontent.com/67350852/123563921-4dc04300-d785-11eb-87a3-7369ae234e4a.gif)


## Supported Operating Systems
Implementation works with Linux.

## Dependencies for Running Locally
* pip 18.1
* Python >= 3.7.3
* Instructions on creating virtual environments  can be found [here](https://docs.python.org/3/tutorial/venv.html)

## Basic Build Instructions
1. Clone this repo and change to directory.
2. To install a virtual environment, run this command: `sudo apt install python3-venv`
3. install venv: `sudo python3 -m venv venv`
4. Activate our virtual environment  `. venv/bin/activate`
5. Install requirements: `pip install -r requirements.txt`

## Running the application
1.  Assign our app.py script to a variable called FLASK_APP `export FLASK_APP=app.py`
2.  `flask run --host=0.0.0.0` This will allow you to access the app fom within your network.You can access the app using the IP address of your device(Raspberry pi in this case).IP address in this case was http://192.168.1.49:5000/

## Docker
`$ docker build -t moviesiteapp .`

`$ docker run -d -p 5000:5000  moviesiteapp`

test




