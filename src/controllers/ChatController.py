from flask import Blueprint, request, make_response
from src.exceptions.ClientError import ClientError
from src.services.ChatService import ChatService
from src.controllers.AuthController import token_required
import json
import urllib

chat = Blueprint('chat', __name__)

@chat.route('/chat/predict', methods=['POST'])
@token_required
def get_chat():
    data = request.get_json()

    try:
        result = ChatService().get_predicted_chat(data)

        response = make_response({"status": "success", "data": json.loads(result)})
        response.headers['Content-Type'] = 'application/json'
        return response

    except ClientError as e:
        response = make_response({"status": "error", "message": e.message})
        response.status_code = e.statusCode
        response.headers['Content-Type'] = 'application/json'
        return response

    except urllib.error.HTTPError as e:
        response = make_response({"status": "error", "message": "Server fail"})
        response.status_code = e.code
        response.headers['Content-Type'] = 'application/json'
        return response
