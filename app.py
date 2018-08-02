from flask import Flask
import time
import datetime

from analise.data_queries import save_data, get_data
from controllers.post_processing import get_tweets
from controllers.miner import miner
from dao.feeling_dao import create_feelings
from dao.font_dao import create_fonts
from dao.user_dao import create_users
from database.db_helper import init

app = Flask(__name__)

init(True)
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
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run(DEBUG=True)
