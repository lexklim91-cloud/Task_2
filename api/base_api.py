# api/base_api.py
import requests
from api.endpoints import Endpoints


class BaseAPI:
    
    def __init__(self):
        self.base_url = Endpoints.BASE_URL
        self.session = requests.Session()
    
    """Формирование заголовков с авторизацией"""
    def _get_headers(self, token=None):
        
        headers = {"Content-Type": "application/json"}
        if token:
            headers["Authorization"] = token if token.startswith("Bearer ") else f"Bearer {token}"
        return headers
    
    
    """Обработка ответа с проверкой статуса"""
    def _handle_response(self, response):
        
        try:
            return response.json()
        except:
            return {"error": "Invalid JSON response"}