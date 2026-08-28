# api/password_api.py
import requests
from api.base_api import BaseAPI
from api.endpoints import Endpoints


class PasswordAPI(BaseAPI):

    """Запрос на сброс пароля"""
    def request_password_reset(self, email):
        
        data = {"email": email}
        response = requests.post(Endpoints.POST_PASSWORD_RESET, json=data)
        return self._handle_response(response)
    
    
    """Установка нового пароля с кодом из письма"""
    def reset_password(self, password, token):
       
        data = {"password": password, "token": token}
        response = requests.post(Endpoints.POST_PASSWORD_RESET_RESET, json=data)
        return self._handle_response(response)