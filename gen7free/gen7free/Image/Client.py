import requests
import asyncio
import json

class Client:
    def __init__(self, TOKEN: str, SECRET_KEY: str) -> None:
        self.URL = "https://api-key.fusionbrain.ai/"
        self.AUTH_HEADERS = {
            'X-Key': f'Key {TOKEN}',
            'X-Secret': f'Secret {SECRET_KEY}',
        }

    def generate(self, params, model):
        data = {
            'model_id': (None, model),
            'params': (None, json.dumps(params), 'application/json')
        }
        response = requests.post(self.URL + 'key/api/v1/text2image/run', headers=self.AUTH_HEADERS, files=data)
        data = response.json()
        return data['uuid']

    def get_model(self):
        response = requests.get(self.URL + 'key/api/v1/models', headers=self.AUTH_HEADERS)
        data = response.json()
        return data[0]['id']
    
    async def check_generation(self, request_id, attempts=10, delay=10):
        while attempts > 0:
            response = requests.get(self.URL + 'key/api/v1/text2image/status/' + request_id, headers=self.AUTH_HEADERS)
            data = response.json()
            if data['status'] == 'DONE':
                return data['images']

            attempts -= 1
            await asyncio.sleep(delay)