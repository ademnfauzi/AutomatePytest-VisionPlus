import os
import random
import requests
import json
import jsonpath
import time

from vplus.test.general.user import users

class Generate:
    
    def endpointUrl(self):
        env = os.environ.get("ENV", "prod").lower()
        if(env == "prod"):
            url = 'https://vplus-bss.visionplus.id'
        elif(env == "stag"):
            url = 'https://temp-bss-stg.visionplus.id'
        
        print(url)
        return url
    
    def numberRandom(self):
        angka_random = ''.join(random.choices('0123456789', k=5))
        angkahp = "8991111"+angka_random
        print(angkahp)
        return angkahp
    
    def numberRandomForEmail(self):
        angka_random = ''.join(random.choices('0123456789', k=3))
        angkahp = "899"+angka_random
        print(angkahp)
        return angkahp
    
    def endpointLoginCMS(self,url):
        url = url + '/cms-service/v1/login'
        data ={
            "email": "tech@visionplus.id",
            "password": "4321Lupa"
        }
        response = requests.post(url, json=data)
        datajson = response.json()
        dataaccess = jsonpath.jsonpath(datajson, "data.token.access_token")[0]
        return dataaccess
    
    def endpointOTP(self, teksrandom):
        url = self.endpointUrl()
        # endpoint getotp
        dataaccess = self.endpointLoginCMS(url)
        url = url + '/otp/v1/admin?limit=100&recipient='+teksrandom 
        # params = {"recipient": teksrandom,
        #           "limit":"100"}  # Mengubah params menjadi dictionary
        headersAuth = {'Authorization': 'Bearer ' + dataaccess}  # Menggunakan dictionary untuk headers
        # response = requests.get(url, headers=headersAuth, params=params)
        response = requests.get(url, headers=headersAuth)
        print(response)
        dataJSONOTP = json.loads(response.text)
        dataOTP = jsonpath.jsonpath(dataJSONOTP, 'data.data[0].OTP')
        print(dataOTP)
        return dataOTP
    
    def endpointOTPforgotPW(self, teksrandom):
        url = self.endpointUrl()
        dataaccess = self.endpointLoginCMS(url)
        # endpoint getotp
        url = url + '/otp/v1/admin?&limit=100&recipient='+teksrandom 
        # params = {"recipient": teksrandom,
        #           "limit":"100"}  # Mengubah params menjadi dictionary
        headersAuth = {'Authorization': 'Bearer ' + dataaccess}  # Menggunakan dictionary untuk headers
        # response = requests.get(url, headers=headersAuth, params=params)
        response = requests.get(url, headers=headersAuth)
        print(response)
        dataJSONOTP = json.loads(response.text)
        dataOTP = jsonpath.jsonpath(dataJSONOTP, 'data.data[1].OTP')
        return dataOTP
    
    def endpointOTPafterDeleted(self, teksrandom,url):
        dataaccess = self.endpointLoginCMS()
        # endpoint getotp
        url = url + '/otp/v1/admin?recipient='+teksrandom+'&limit=100' 
        # params = {"recipient": teksrandom,
        #           "limit":"100"}  # Mengubah params menjadi dictionary
        headersAuth = {'Authorization': 'Bearer ' + dataaccess}  # Menggunakan dictionary untuk headers
        # response = requests.get(url, headers=headersAuth, params=params)
        response = requests.get(url, headers=headersAuth)
        dataJSONOTP = json.loads(response.text)
        dataOTP = jsonpath.jsonpath(dataJSONOTP, 'data.data[2].OTP')
        print(dataOTP)
        return dataOTP