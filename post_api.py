import yaml
import requests
from opens import ReadArchive
import pandas as pd

class ApiRequest:
    def __init__(self):
        try:
            with open("datas.yml", 'r') as file:
                self.datas = yaml.safe_load(file)
            
            self.access_token = self.datas['access_token']
            self.file_path = self.datas['path']
        except FileNotFoundError:
            print("O arquivo datas.yml não foi encontrado.")
            raise
        except KeyError as e:
            print(f"Chave ausente no arquivo YAML: {e}")
            raise

    def body(self, number, name):
        to_phone_number = str(number).replace('.0', '').strip() if number else ''

        url = self.datas['URL']

        headers = {
            'Authorization': f'Bearer {self.access_token}',
            'Content-Type': 'application/json'
        }

        payload = {
            "messaging_product": "whatsapp",
            "to": to_phone_number,
            "type": "template",
            "template": {
                "name": "teste", 
                "language": {
                "code": "pt_BR" 
                },
                "components": [
                {
                    "type": "header",
                    "parameters": [
                    {
                        "type": "text",
                        "text": name
                    }
                    ]
                },
                {
                    "type": "body",
                    "parameters": [] 
                }
                ]
            }
        }

        return url, headers, payload
    
    def request(self, url, headers, payload):
        try:
            response = requests.post(url, headers=headers, json=payload)
            
            if response.status_code == 200:
                print('Mensagem enviada com sucesso!')
                print(response.json())
            else:
                print('Falha ao enviar a mensagem.')
                print(f'Status Code: {response.status_code}')
                print(f'Resposta: {response.json()}')
        except requests.exceptions.RequestException as e:
            print(f"Erro ao fazer a requisição: {e}")

    def send_messages(self):
        info = ReadArchive(self.file_path)
        names = info.get_name()
        numbers = info.get_number()
        values = info.get_value()
        
        for name, number, value in zip(names, numbers, values):
            if pd.isna(number):
                number = ''
            if pd.isna(name):
                name = ''
            
            url, headers, payload = self.body(number, name)
            self.request(url, headers, payload)

api_request = ApiRequest()
api_request.send_messages()
