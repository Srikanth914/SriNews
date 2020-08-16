#from bs4 import BeautifulSoup
#from newsapi import NewsApiClient
from flask import Flask,request,render_template,url_for,redirect
import requests

#newsapi = NewsApiClient(api_key='803162dab26f487591f53a00a05cef96')

#top_headlines = newsapi.get_top_headlines(q='bitcoin',
  #                                        sources='bbc-news,the-verge',
  ##                                        category='business',
   #                                       language='en',
   #                                       country='in')

app = Flask(__name__)

url = ('https://newsapi.org/v2/top-headlines?'
       'country=in&'
       'apiKey=803162dab26f487591f53a00a05cef96')
def get_data(url):
    response = requests.get(url)
    data = response.json()
    articles = data['articles']
    return articles

articles = get_data(url)

@app.route('/')
def home():
    return render_template('index.html',articles=articles)

@app.route('/invalid')
def invalid():
    return "<center><h2 style='color:green;'>something went wrong..!</h2></center>"

@app.route('/search', methods=['POST','GET'])
def search():
    if request.method =='POST':
            data =request.form['search']
            if not data:
                return redirect(url_for('invalid'))
            else:
                url= ('https://newsapi.org/v2/everything?q='+data+'&apiKey=803162dab26f487591f53a00a05cef96')
                articles = get_data(url)
                return render_template('search.html',articles=articles,data=data)
      
if __name__ == '__main__':
    app.run()


if __name__ == '__main__':
    app.run(debug=True)