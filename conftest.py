# conftest.py
import pytest
import sys
import os

# Добавляем корневую директорию в путь
root_dir = os.path.dirname(os.path.abspath(__file__))
if root_dir not in sys.path:
    sys.path.insert(0, root_dir)

from api.user_api import UserAPI
from api.orders_api import OrdersAPI
from api.ingredients_api import IngredientsAPI
from helpers import unique_user_data

# Инициализация API-классов
user_api = UserAPI()
orders_api = OrdersAPI()
ingredients_api = IngredientsAPI()


"""Создание пользователя и возврат данных с токенами"""
@pytest.fixture
def created_user():
    user_data = unique_user_data()                     
    created = user_api.create_user_and_get_tokens(user_data)
    yield created
    # Удаление пользователя после теста
    if created.get("accessToken"):
        user_api.delete_user(created["accessToken"])


"""Заголовки с авторизацией"""
@pytest.fixture
def auth_headers(created_user):
    return {"Authorization": created_user["accessToken"]}


"""Получение валидных ID ингредиентов"""
@pytest.fixture
def valid_ingredients():
    return ingredients_api.get_valid_ingredient_ids()
    

"""Создание заказа и возврат его номера"""
@pytest.fixture
def created_order(created_user, valid_ingredients):
    order_number = orders_api.get_created_order_number(
        created_user["accessToken"], 
        valid_ingredients
    )
    return order_number