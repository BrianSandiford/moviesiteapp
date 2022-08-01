import os
import requests
from flask import Flask, render_template, request
# from elasticapm.contrib.flask import ElasticAPM

app = Flask(__name__)
app.config['DEBUG'] = True

# app.config['ELASTIC_APM'] = {
#          'SERVICE_NAME': 'FlaskApp',
#          'SECRET_TOKEN': '',         
#          'SERVER_URL': 'ec2-3-143-0-67.us-east-2.compute.amazonaws.com:8200'
# }
# apm = ElasticAPM(app)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def page_not_found(e):
    return render_template('500.html'), 500

@app.route('/', methods=['GET','POST'])
def index():
    # api_key =  os.getenv('SECRET_KEY')
    api_key =  '20acf4f9f1a3d619ed2764b51dd7a2f1'
    if request.method == 'POST' :
        movie_name = request.form.get('movie_name')
        if movie_name:
             url = 'https://api.themoviedb.org/3/search/movie?api_key={}'.format(api_key) +'&language=en-US&query={}&page=1&include_adult=false'
             r = requests.get(url.format(movie_name)).json()
        else:
          url = 'https://api.themoviedb.org/3/movie/popular?api_key={}'.format(api_key) +'&language=en-US&page=1'
          r = requests.get(url).json()
    else:
      url = 'https://api.themoviedb.org/3/movie/popular?api_key={}'.format(api_key) +'&language=en-US&page=1'
      r = requests.get(url).json()
    if not r['results']:
      return render_template('404.html'), 404
    else:
     return  render_template('index.html', data=r['results'])


