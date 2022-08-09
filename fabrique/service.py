
from datetime import datetime
import requests

class MailingProcess:
    def send_message(self, instance, new_message, client):
            token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2OTEyNDM4ODUsImlzcyI6ImZhYnJpcXVlIiwibmFtZSI6InVzaGhha292YSJ9.QXEJpsKRVL5A2rMSOP5_QC1OiF1jHwowWZvOsPGsSlA'
            url_param = 'https://probe.fbrq.cloud/v1/send/'+str(new_message.id)
            api_param = {
                #'id': new_message.id,
                'phone': client.telephon_number,
                'text': instance.text
            }
            header_param = {
                'Authorization': 'Bearer ' + token
            }

            response = requests.post(url=url_param, params=api_param, headers=header_param)
            #response = requests.post(url_param, api_param)
            result = response.json()
            print(result)

    def test_response(self):
            token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2OTEyNDM4ODUsImlzcyI6ImZhYnJpcXVlIiwibmFtZSI6InVzaGhha292YSJ9.QXEJpsKRVL5A2rMSOP5_QC1OiF1jHwowWZvOsPGsSlA'
            url_param = 'https://probe.fbrq.cloud/v1/send/'+'1'
            api_param = {
                'id': 1,
                'phone': 78222233445,
                'text': 'hithere'
            }
            header_param = {
                'Authorization': 'Bearer ' + token
            }

            response = requests.post(url_param, api_param, headers = header_param)
            
            result = response.json()
            print(response,result)


#t = MailingProcess()
#t.test_response()