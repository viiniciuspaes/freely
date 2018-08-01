from flask import Flask

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
# hashtag = "LulaLivre"
# miner(1527811200, 1530791440, hashtag)
# get_tweets(hashtag)

@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run(DEBUG=True)
