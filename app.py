from flask import Flask, render_template, request
import time
import datetime
from controllers.data_queries import save_data, get_data
from controllers.post_processing import get_tweets
from controllers.miner import miner
from dao.feeling_dao import create_feelings
from dao.font_dao import create_fonts
from dao.user_dao import create_users
from database.db_helper import init

app = Flask(__name__)

init(False)
create_feelings()
create_users()
create_fonts()

start = time.mktime(datetime.datetime.strptime("01/03/2018", "%d/%m/%Y").timetuple())
end = time.mktime(datetime.datetime.strptime("31/07/2018", "%d/%m/%Y").timetuple())


arq = open('hashtags.txt', 'r')
lines = arq.readlines()
for hashtag in lines:
    hashtag = hashtag.replace("\n", "")
    miner(start, end, hashtag)
    get_tweets(hashtag)

arq.close()
save_data(get_data())

@app.route('/')
def Index():
    return render_template('hash-busca.html')

@app.route('/pesquisaHash', methods={'POST','GET'})
def PesquisaHash():
    select = request.form.get('busca') 
    return render_template('hash-busca.html', TAG = str(select))

@app.route('/fonte-busca', methods={'POST','GET'})
def PesquisaFonte():
    return render_template('fonte-busca.html')

@app.route('/quantidade-tweets', methods={'POST','GET'})
def QuantidadeTweets():
    return render_template('quantidade-tweets.html')
    
if __name__ == '__main__':
    app.run()
    #debug=True
