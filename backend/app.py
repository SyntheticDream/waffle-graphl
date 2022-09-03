from flask import Flask, current_app

DEBUG = True

app = Flask(__name__)
app.config.from_object(__name__)

@app.route('/', methods=['GET'])
def index():
    return current_app.send_static_file('index.html')

# hack
@app.route('/assets/<asset>', methods=['GET'])
def assets(asset):
    return current_app.send_static_file(f'assets/{asset}')


if __name__ == '__main__':
    app.run()
