from flask import Flask

app = Flask(__name__)


@app.route('/api/v1/primeira-rota')
def hello_world():
    return 'Flask na SIC!'


if __name__ == '__main__':
    app.run()
