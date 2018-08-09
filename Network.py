# -*- coding: utf-8 -*-

import re
import requests


class BIT_Network():
    def __init__(self, userInfo):
        self.web_port = 801        
        self.url_init = 'http://10.0.0.55:{}'.format(self.web_port)
        
        self.u_name = userInfo[0]
        self.u_pwd = userInfo[1]
        
        self.headers = {
            'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate',
            'Cache-Control': 'no-cache',
            'Connection': 'keep-alive',
            'DNT': '1',
            'Host': '10.0.0.55:{}'.format(self.web_port),
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.78 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest',
        }
        
        self.url_BIT = self.url_init + '/include/auth_action.php'
        self.url_info = self.url_init + '/srun_portal_pc_succeed.php'
        self.url_logout = self.url_init[:-4] + '/cgi-bin/srun_portal'
        
        self.bit = requests.session()
        
    def login(self):
        self.data_login = {
            'username': self.u_name,
            'password': self.u_pwd,
            'ac_id': '1',
            'save_me': '0',
            'ajax': '1',
            'action': 'login',
        }
        
        self.bit_login = self.bit.post(self.url_BIT, data=self.data_login, headers=self.headers)
        self.bit_login.encoding = 'utf-8'
        self.bit_html = self.bit_login.text.lower()

        if 'login_ok' in self.bit_html:
            output_init = 'Welcome to connect BIT network!'
            self.response_test = self.bit.get(self.url_info, headers=self.headers)
            re_P = r'<span.*?>(.*?)</span>'
            self.user_info = re.findall(re_P, self.response_test.text)
            self.us_name = self.user_info[0].strip()
            self.us_ip = self.user_info[1].strip()
            self.us_bytes = self.user_info[2].strip()
            self.us_balance = self.user_info[4].strip()
            output = '{0}\n\nUsername: {1}\nLogin IP: {2}\nUsed Bytes: {3}\nBalance: {4}'.format(output_init, self.us_name, self.us_ip, self.us_bytes, self.us_balance)
            return output
        elif 'ip has been online' in self.bit_html:
            output_init = 'IP has been Online!'
            self.response_test = self.bit.get(self.url_info, headers=self.headers)
            re_P = r'<span.*?>(.*?)</span>'
            self.user_info = re.findall(re_P, self.response_test.text)
            self.us_name = self.user_info[0].strip()
            self.us_ip = self.user_info[1].strip()
            self.us_bytes = self.user_info[2].strip()
            self.us_balance = self.user_info[4].strip()
            output = '{0}\n\nUsername: {1}\nLogin IP: {2}\nUsed Bytes: {3}\nBalance: {4}'.format(output_init, self.us_name, self.us_ip, self.us_bytes, self.us_balance)
            return output
        elif 'password is error' in self.bit_html:
            output = 'Password is Error!'
            return output
        elif 'arrearage' in self.bit_html:
            output = 'Arrearage User!'
            return output
        else:
            output = 'Error occurs during connecting network ...'
            return output
    
    def logout(self, type='y'):
        self.data_logout = {
            'username': self.u_name,
            'password': None,
            'ac_id': '1',
            'type': '2',
            'action': 'logout',
        }
        if type == 'n':
            self.data_logout['password'] = self.u_pwd
        
        self.bit_logout = self.bit.post(self.url_logout, data=self.data_logout, headers=self.headers)
        self.bit_logout.encoding = 'utf-8'

        self.bit_html = self.bit_logout.text.lower().strip()
        if 'logout_ok' in self.bit_html:
                output = 'IP has been logouted!'
        else:
            output = 'Note:\n\nIP has been logouted, or Some Error occur during logouting IP'
        return output