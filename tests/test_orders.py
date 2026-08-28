
import allure
from api.orders_api import OrdersAPI
from api.ingredients_api import IngredientsAPI

orders_api = OrdersAPI()
ingredients_api = IngredientsAPI()


class TestCreateOrder:
    @allure.step("""Создание заказа с авторизацией и ингредиентами - успешно""")
    def test_create_order_with_auth_success(self, created_user, valid_ingredients):
        response = orders_api.create_order(created_user["accessToken"], valid_ingredients)
        data = response.json()
        assert response.status_code == 200
        assert data["success"] is True
        assert "name" in data
        assert "order" in data
        assert "number" in data["order"]
        assert isinstance(data["order"]["number"], int)
    
    
    @allure.step("""Создание заказа с неверным хешем ингредиента - ошибка 500""")
    def test_create_order_with_invalid_ingredient_hash_fails(self, created_user):
        response = orders_api.create_order(created_user["accessToken"], ["invalid_hash_12345"])
        assert response.status_code == 500
    
    
    @allure.step("""Создание заказа с несколькими ингредиентами - успешно""")
    def test_create_order_with_multiple_valid_ingredients_success(self, created_user, valid_ingredients):
        response = orders_api.create_order(created_user["accessToken"], valid_ingredients)
        data = response.json()
        assert response.status_code == 200
        assert data["success"] is True
        assert data["order"]["number"] > 0