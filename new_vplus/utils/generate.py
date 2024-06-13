import random
import requests
import json
import jsonpath
import time

class Generate:
    def angkaRandom(self):
        angka_random = ''.join(random.choices('0123456789', k=5))
        angkahp = "8997777"+angka_random
        print(angkahp)
        return angkahp
    
    def endpointLoginCMS(self):
        url = 'https://temp-bss-stg.visionplus.id/cms-service/v1/login'
        data ={
            "email": "baskara@gmail.com",
            "password": "4321lupa"
        }
        response = requests.post(url, json=data)
        datajson = response.json()
        dataaccess = jsonpath.jsonpath(datajson, "data.token.access_token")[0]
        return dataaccess
    
    def endpointOTP(self, teksrandom):
        # endpoint getotp
        dataaccess = self.endpointLoginCMS()
        url = 'https://temp-bss-stg.visionplus.id/otp/v1/admin?' 
        params = {"recipient": teksrandom}  # Mengubah params menjadi dictionary
        headersAuth = {'Authorization': 'Bearer ' + dataaccess}  # Menggunakan dictionary untuk headers
        response = requests.get(url, headers=headersAuth, params=params)
        print(response)
        dataJSONOTP = json.loads(response.text)
        dataOTP = jsonpath.jsonpath(dataJSONOTP, 'data.data[0].OTP')
        print(dataOTP)
        return dataOTP
    
    def endpointOTPforgotPW(self, teksrandom):
        # url = 'https://vplus-bss.visionplus.id/cms-service/v1/login'
        # data ={
        #     "email": "baskara@gmail.com",
        #     "password": "4321lupa"
        # }
        # response = requests.post(url, json=data)
        # datajson = response.json()
        # dataaccess = jsonpath.jsonpath(datajson, "data.token.access_token")[0]
        dataaccess = self.endpointLoginCMS()
        # endpoint getotp
        url = 'https://temp-bss-stg.visionplus.id/otp/v1/admin?' 
        params = {"recipient": teksrandom}  # Mengubah params menjadi dictionary
        headersAuth = {'Authorization': 'Bearer ' + dataaccess}  # Menggunakan dictionary untuk headers
        response = requests.get(url, headers=headersAuth, params=params)
        dataJSONOTP = json.loads(response.text)
        dataOTP = jsonpath.jsonpath(dataJSONOTP, 'data.data[1].OTP')
        return dataOTP
    
   
    def endpointOTPafterDeleted(self, teksrandom):
        # url = 'https://vplus-bss.visionplus.id/cms-service/v1/login'
        # data ={
        #     "email": "baskara@gmail.com",
        #     "password": "4321lupa"
        # }
        # response = requests.post(url, json=data)
        # datajson = response.json()
        # dataaccess = jsonpath.jsonpath(datajson, "data.token.access_token")[0]
        dataaccess = self.endpointLoginCMS()
        # endpoint getotp
        url = 'https://vplus-bss.visionplus.id/otp/v1/admin?' 
        params = {"recipient": teksrandom}  # Mengubah params menjadi dictionary
        headersAuth = {'Authorization': 'Bearer ' + dataaccess}  # Menggunakan dictionary untuk headers
        response = requests.get(url, headers=headersAuth, params=params)
        dataJSONOTP = json.loads(response.text)
        dataOTP = jsonpath.jsonpath(dataJSONOTP, 'data.data[2].OTP')
        print(dataOTP)
        return dataOTP
     
