# api/orders_api.py
import requests
from api.base_api import BaseAPI
from api.endpoints import Endpoints
from api.ingredients_api import IngredientsAPI


class OrdersAPI(BaseAPI):
    
    """Создание нового заказа"""
    def create_order(self, token, ingredients):
        data = {"ingredients": ingredients}
        headers = self._get_headers(token)
        return requests.post(Endpoints.POST_ORDERS, json=data, headers=headers)
    
    
    """Получение всех заказов (публичная лента)"""
    def get_all_orders(self):
        return requests.get(Endpoints.GET_ORDERS_ALL)         
    
    
    """Получение заказов текущего пользователя"""
    def get_user_orders(self, token):        
        headers = self._get_headers(token)
        return requests.get(Endpoints.GET_ORDERS, headers=headers)
    
    
    """Создание заказа с автоматическим получением ингредиентов"""
    def create_order_with_valid_ingredients(self, token):
        
        ingredients_api = IngredientsAPI()
        ingredients = ingredients_api.get_valid_ingredient_ids()
        response = self.create_order(token, ingredients)
        return response, ingredients
    
    
    """Создание заказа и получение его номера"""
    def get_created_order_number(self, token, ingredients=None):
        
        if ingredients is None:
            ingredients_api = IngredientsAPI()
            ingredients = ingredients_api.get_valid_ingredient_ids()
        
        response = self.create_order(token, ingredients)
        if response.get("success"):
            return response["order"]["number"]
        return None