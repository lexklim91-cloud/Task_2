# api/user_api.py
import requests
from api.base_api import BaseAPI
from api.endpoints import Endpoints


class UserAPI(BaseAPI):
   
    """Регистрация нового пользователя"""
    def register_user(self, user_data):
        return requests.post(Endpoints.POST_REGISTER, json=user_data)
    
    
    """Авторизация пользователя"""
    def login_user(self, login_data):                
        return requests.post(Endpoints.POST_LOGIN, json=login_data)
    
    
    """Получение данных пользователя"""
    def get_user(self, token):
        headers = self._get_headers(token)
        return requests.get(Endpoints.GET_USER, headers=headers)
        
    
    
    """Обновление данных пользователя"""
    def update_user(self, token, update_data):
        headers = self._get_headers(token)
        return requests.patch(Endpoints.PATCH_USER, json=update_data, headers=headers)

    
    
    
    """Удаление пользователя"""
    def delete_user(self, token):       
        headers = self._get_headers(token)
        return requests.delete(Endpoints.DELETE_USER, headers=headers)
    
    
     
    """Выход из системы"""
    def logout_user(self, refresh_token):       
        data = {"token": refresh_token}
        return requests.post(Endpoints.POST_LOGOUT, json=data)
    
    
    """Обновление accessToken"""
    def refresh_token(self, refresh_token):        
        data = {"token": refresh_token}
        return requests.post(Endpoints.POST_TOKEN, json=data)

    
    
    """Регистрация пользователя и получение токенов"""
    def create_user_and_get_tokens(self, user_data):
        
        response = self.register_user(user_data)
        data = response.json()
        if data.get("success"):
            return {
                **user_data,
                "accessToken": data.get("accessToken"),
                "refreshToken": data.get("refreshToken"),
                "user": data.get("user")
            }
        return response