from flask import Flask

from controllers.infos import get_tweets
from controllers.miner import miner
from database.db_helper import init

app = Flask(__name__)

init(True)
# hashtag = "LulaLivre"
# miner(1527811200, 1530791440, hashtag)
# get_tweets(hashtag)

@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run(DEBUG=True)
