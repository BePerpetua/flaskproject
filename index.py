from flask import Flask

app = Flask(__name__)

@app.route('/')
def homepage(name):
    return '<h1>Hello</h1>'

@app.route('/about')
def aboutpage():
    return '<h1>This is the about page</h1>'

@app.route('/<name>')
def secondmessage(name):
    return f'Hello {name}'

@app.route('/contact')
def thirdmessage():
    return '<h1>Contact us on this page</h1>'