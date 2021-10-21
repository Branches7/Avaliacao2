from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def login():  # put application's code here
    return render_template('login.html')
@app.route('/home')
def home():
    return render_template('home.html')


if __name__ == '__main__':
    app.run()