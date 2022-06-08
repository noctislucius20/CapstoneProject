import json
import os
import urllib.request

class ChatService:
    def get_predicted_chat(self, data):
        data_to_bytes = json.dumps(data).encode('utf-8')
        ml_url = os.getenv('ML_SERVER_URL')
        url = f'https://{ml_url}/smart_chatbot/predict'
        req = urllib.request.Request(url, method='GET')
        req.add_header('Content-Type', 'application/json')
        returned_data = urllib.request.urlopen(req, data_to_bytes)
        result = returned_data.read()

        return result