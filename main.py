import os
from flask import Flask

def os_list_dir():
    dir = "C:\\Users\\sdgro\\OneDrive\\Рабочий стол\\Python\\web_proj\\data\\"
    ls_input = os.listdir(dir+"input\\")
    ls_output = os.listdir(dir+"output\\")
    ls_move = os.listdir(dir+"move\\")
    print(len(ls_input))

app = Flask(__name__)
@app.route('/')
def index():
    return '<h1>Hello World!</h1>'

if __name__ == '__main__':
    app.run(debug= True)





os_list_dir()
