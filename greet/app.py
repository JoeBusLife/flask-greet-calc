from flask import Flask

app = Flask(__name__)

@app.route('/welcome')
def Display_Welcome():
    return 'welcome'

@app.route('/welcome/home')
def Display_Welcome_Home():
    return 'welcome home'

@app.route('/welcome/back')
def Display_Welcome_Back():
    return 'welcome back'