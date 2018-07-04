from flask import Flask

from database.db_helper import init

app = Flask(__name__)
init()

@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
