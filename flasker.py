# -*- coding: utf-8 -*-
from flask import Flask
from flask import render_template
from flask import request
from Network import BIT_Network
from User import User_Info
 

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        output = ''
        us_info = User_Info().getUserInfo()
        return render_template('index.html', us_info=us_info, info=output)
    else:
        true_flag = True
        usr = request.form.get("usr", type = str, default = '')
        pwd = request.form.get("pwd", type = str, default = '')
        us_info = (usr, pwd)
        if not (usr and pwd):
            output = 'Your user information is not complete!'
            return render_template('index.html', us_info=us_info, info=output)
        btn_method = request.form.get("method", type = str, default = 'Login')
        if btn_method == 'Login':
            output = BIT_Network((usr, pwd)).login()
        else:
            type_logout = request.form.get("type_logout", type = str, default = 'y')
            print(type_logout)
            output = BIT_Network((usr, pwd)).logout(type_logout)
        if 'Password is Error' in output:
            true_flag = False
        else:
            User_Info().saveUserInfo(us_info, true_flag)
        us_info = User_Info().getUserInfo()
        
        
        return render_template('index.html', us_info=us_info, info=output)
    
@app.route('/upload', methods=['GET', 'POST'])
def upload():
    files = request.files.get('file')
    if not files:
        return 'Please upload file!'
    with open(r'C:\Users\ZQCheng\Desktop\Network\static\{}'.format(files.filename), 'wb') as fd:
        fd.write(files.read())
    return render_template('download.html', url='/static/{}'.format(files.filename))


   
    
if __name__ == '__main__':
    app.run(host='127.0.0.1', port='8000')
