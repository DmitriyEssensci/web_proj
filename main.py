import os
from flask import Flask
from flask import request
from flask import make_response
from flask import abort
from flask import render_template
from flask_bootstrap import Bootstrap5
from flask_script import Manager

def os_list_dir():
    dir = "C:\\Users\\sdgro\\OneDrive\\Рабочий стол\\Python\\web_proj\\data\\"
    ls_input = os.listdir(dir+"input\\")
    ls_output = os.listdir(dir+"output\\")
    ls_move = os.listdir(dir+"move\\")
    print(len(ls_input))

app = Flask(__name__)

#@app.route('/')
# def index():
#     return '<h1>Hello World!</h1>'

# @app.route('/')
# def index():
#     user_agent = request.headers.get('User-Agent')
    #return '<p>Your browser is %s</p>' % user_agent

@app.route('/')
def index():
    response = make_response('<h1> This document carries a cookie! </h1>')
    response.set_cookie('answer', '42')
    #return response 
    return render_template('index.html')
 
@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)

@app.route('/user/<id>')
def  get_user(id):
    user = load_user(id)
    if not user:
        abort(404)
        
    return '<h1> Hello %s</h1> % user.name'
    #return render_template('if-else_operation.html', id=user)

if __name__ == '__main__':
    app.run(debug= True)
    Manager.run()