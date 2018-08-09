# -*- coding: utf-8 -*-

import os, base64, json

class User_Info():
    def __init__(self):
        self.userPath = os.getcwd()
        self.userFile = os.path.join(self.userPath, 'user', 'user.json')
        os.makedirs(os.path.dirname(self.userFile), exist_ok=True)

    def getUserInfo(self):
        try:
            with open(self.userFile, 'rt') as fd:
                us_info = json.load(fd)
            u_name = us_info['usr']
            u_pwd = base64.decodebytes(bytes(us_info['pwd'], 'utf-8')).decode()
        except:
            u_name = ''
            u_pwd = ''
        return u_name, u_pwd
    
    def saveUserInfo(self, userInfo, true_flag):
        if not (os.path.exists(self.userFile) and true_flag):
            u_name = userInfo[0]
            u_pwd = base64.encodebytes(bytes(userInfo[1], 'utf-8')).decode()
            us_info = {'usr': u_name, 'pwd': u_pwd}
            with open(self.userFile, 'wt') as fd:
                json.dump(us_info, fd, indent=4)
        else:
            pass