from flask import Flask

app = Flask(__name__)
@app.route('/username/<name>')
def home(name):
    return f'{name} is learning Flask!'

if __name__ == '__main__':
    app.run(debug=True)