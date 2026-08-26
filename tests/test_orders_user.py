
import allure
from api.orders_api import OrdersAPI
from api.ingredients_api import IngredientsAPI

orders_api = OrdersAPI()
ingredients_api = IngredientsAPI()


class TestGetUserOrders:
    
    
    @allure.step("""Получение заказов авторизованного пользователя - успешно""")
    def test_get_orders_with_auth_success(self, created_user):
        
        # Сначала создаем заказ
        ingredients = ingredients_api.get_valid_ingredient_ids()
        create_response = orders_api.create_order(created_user["accessToken"],ingredients)
        create_order_list = create_response.json()
        created_order_number = create_order_list["order"]["number"]
        
        # Получаем заказы пользователя
        response = orders_api.get_user_orders(created_user["accessToken"])
        data = response.json()
        assert response.status_code == 200
        
        assert data["success"] is True
        assert "orders" in data
        assert isinstance(data["orders"], list)
        assert len(data["orders"]) > 0
        assert "total" in data
        assert "totalToday" in data
        
        # Проверяем, что созданный заказ есть в списке
        order_numbers = [order["number"] for order in data["orders"]]
        assert created_order_number in order_numbers
    
    
    @allure.step("""Получение заказов без авторизации - ошибка 401""")
    def test_get_orders_without_auth_fails(self):
        
        response = orders_api.get_user_orders(None)
        data = response.json()
        assert response.status_code == 401        
        assert data["success"] is False
        assert data["message"] == "You should be authorised"
    
    
    @allure.step("""Получение всех заказов (публичная лента) - успешно""")
    def test_get_orders_all_public_success(self):
        
        response = orders_api.get_all_orders()
        data = response.json()
        assert response.status_code == 200
        assert data["success"] is True
        assert "orders" in data
        assert isinstance(data["orders"], list)
        assert "total" in data
        assert "totalToday" in data
        
