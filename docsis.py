#!/usr/bin/python

import requests
import json


class Docsis:
    '''
    class to control a "Technicolor DPC3848V DOCSIS 3.0 Gateway"
    '''

    AUTH="check.php"
    SSID_CONFIG="actionHandler/ajaxSet_WSecurity.php"
    CHECK_LOGIN="actionHandler/checkLogin.php"
    RESTART= "actionHandler/ajaxSet_DeviceRestart.php"

    def __init__(self,username,password,base_url="192.168.0.1"):
        self.username=username
        self.password=password
        self.base_url=base_url
        self.s = requests.session()
        self.s.headers.update(
            {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
            'Host':base_url})


    def build_url(self,endpoint):
        return "http://{}/{}".format(self.base_url,endpoint)

    def login(self):
        ep = self.build_url(self.AUTH)
        data = {
            'login':'LogIn',
            'password_login':self.password,
            'username_login':self.username,
        }   
        return self.s.post(ep,data)

    def check_login(self):
        ep = self.build_url(self.CHECK_LOGIN)
        return self.s.get(ep, headers={"Upgrade-Insecure-Requests":"1"})

    def configure_wifi(self,enable_2,enable_5,ssid="docsis",password="password1234"):
        '''
        this was extracted by sniffing HTTP traffic in firefox
        '''
        radio_enable="{}".format(enable_2).lower()
        radio_enable_5g="{}".format(enable_5).lower()

        data = {"ssid_number":"1,2","encrypt_mode":"WPA-WPA2-Personal","encrypt_method":"AESTKIP","network_password":password,"encrypt_rekey":"3600","network_pass_def":"1","network_pass_64":",,,,","network_pass_128":",,,,","radius_ip":"0.0.0.0","radius_port":"0","radius_sec":"","radius_rekey":"0","encrypt_mode_5g":"WPA-WPA2-Personal","encrypt_method_5g":"AESTKIP","network_password_5g":password,"encrypt_rekey_5g":"3600","network_pass_def_5g":"1","network_pass_64_5g":",,,,","network_pass_128_5g":",,,,","radius_ip_5g":"0.0.0.0","radius_port_5g":"0","radius_sec_5g":"","radius_rekey_5g":"0","thisUser":"cusadmin","new_passwd":"","radio_enable":radio_enable,"network_name":ssid,"radio_enable_5g":radio_enable_5g,"network_name_5g":ssid+"-5G","thisMenu":"vsetup"}

        config = json.dumps(data)
       
        #config = config_template#format()
        data={'configInfo':config}
        ep = self.build_url(self.SSID_CONFIG)
        #self.check_auth() #refresh cookie
        self.check_login()
        return json.loads(self.s.post(ep,data).content)

    def restart(self):
        ep = self.build_url(self.RESTART)
        settings = json.dumps({ "DeviceRestart":"Router,WiFi,VoIP,Dect,MoCA", 
		"LoginName":self.username, 
		"password":self.password,
		"isrestart":"TRUE"})
        self.check_login()
        result=False
        try:
            self.s.post(ep,{'deviceRestartInfo':settings})
        except requests.exceptions.ConnectionError:
            #this is expected
            result=True
        return result

        



