#! /extdisks/sda4/opkg/usr/bin python
#date: 2015/11/09
#For Autologin ChinaUnicom 201
#Code by Funnyang

import sys  
import re  
import urllib2  
import urllib  
import requests  
import cookielib  
import socket  
import fcntl  
import struct

reload(sys)  
sys.setdefaultencoding("utf-8")

#get local ip
def get_ip_address(ifname):  
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  
    return socket.inet_ntoa(fcntl.ioctl(      
         s.fileno(),         
         0x8915,  # SIOCGIFADDR                 
         struct.pack('256s', ifname[:15])                         
    )[20:24])                                  

#login
loginurl = 'http://114.247.41.52:808/protalAction!portalAuth.action?'

class Login(object):

    def __init__(self):
        self.wlanuserip = ''
        self.localIp = ''
        self.basip = ''
        self.lpsUserName = ''
        self.lpsPwd = ''

        self.cj = cookielib.LWPCookieJar()
        self.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cj))
        urllib2.install_opener(self.opener)

    def setLoginInfo(self,wlanusrip,localIp,basip,lpsUserName,lpsPwd):
        self.wlanuserip = wlanuserip                                       
        self.localIp = localIp                                            
        self.basip =  basip                                              
        self.lpsUserName =  lpsUserName                                       
        self.lpsPwd = lpsPwd 

    def login(self):
        loginparams = {'wlanuserip':self.wlanuserip,'localIp':self.localIp,'basip':self.basip,'lpsUserName':self.lpsUserName,'lpsPwd':self.lpsPwd}
        headers = {'User-Agent':'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_2_1 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8C148 Safari/6533.18.5'}    
        req = urllib2.Request(loginurl, urllib.urlencode(loginparams),headers=headers)  
        response = urllib2.urlopen(req)
        self.operate = self.opener.open(req)
        thePage = response.read()    
        print thePage

if __name__ == '__main__':  
    userlogin = Login()
    wlanuserip = get_ip_address('eth0.2') 
    localIp = ''
    basip = '61.148.2.82'
    lpsUserName = '手机号/账户'
    lpsPwd = '密码'
    userlogin.setLoginInfo(wlanuserip,localIp,basip,lpsUserName,lpsPwd)
    userlogin.login()
