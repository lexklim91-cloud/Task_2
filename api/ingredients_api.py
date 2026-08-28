# api/ingredients_api.py
import requests
from api.base_api import BaseAPI
from api.endpoints import Endpoints


class IngredientsAPI(BaseAPI):
    
    """Получение списка всех ингредиентов"""
    def get_ingredients(self):
        response = requests.get(Endpoints.GET_INGREDIENTS)
        return self._handle_response(response)
    
    
    """Получение валидных ID ингредиентов для заказа"""
    def get_valid_ingredient_ids(self, limit=2):
        data = self.get_ingredients()
        if data.get("success") and "data" in data:
            ingredients = data["data"]
            return [ing["_id"] for ing in ingredients[:limit]]
        return []