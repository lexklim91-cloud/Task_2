# conftest.py
import pytest
import random
import sys
import os
import time

# Добавляем корневую директорию в путь
root_dir = os.path.dirname(os.path.abspath(__file__))
if root_dir not in sys.path:
    sys.path.insert(0, root_dir)

from api.user_api import UserAPI
from api.orders_api import OrdersAPI
from api.ingredients_api import IngredientsAPI

# Инициализация API-классов
user_api = UserAPI()
orders_api = OrdersAPI()
ingredients_api = IngredientsAPI()



"""Генерация уникальных данных для пользователя на основе времени"""
@pytest.fixture
def unique_user_data():
    
    timestamp = int(time.time() * 1000)
    return {
        "email": f"test_{timestamp}@example.com",
        "password": f"Pass{timestamp}",
        "name": f"User_{timestamp}"
    }



"""Создание пользователя и возврат данных с токенами"""
@pytest.fixture
def created_user(unique_user_data):
    
    user_data = user_api.create_user_and_get_tokens(unique_user_data)
    yield user_data
    
    # Удаление пользователя после теста
    if user_data.get("accessToken"):
        user_api.delete_user(user_data["accessToken"])



"""Заголовки с авторизацией"""
@pytest.fixture
def auth_headers(created_user):
   
    return {"Authorization": created_user["accessToken"]}


"""Получение валидных ID ингредиентов"""
@pytest.fixture
def valid_ingredients():
    
    return ingredients_api.get_valid_ingredient_ids()
    

"""Невалидный хеш ингредиента"""
@pytest.fixture
def invalid_ingredient_hash():
    return "invalid_hash_12345"

"""Создание заказа и возврат его номера"""
@pytest.fixture
def created_order(created_user, valid_ingredients):
    order_number = orders_api.get_created_order_number(
        created_user["accessToken"], 
        valid_ingredients
    )
    return order_number


@pytest.fixture()
def generate_email():
    first_names = ["alex", "maria", "alex", "anna"]
    last_names = ["smith", "ivanov", "doe", "petrov"]
    domains = ["gmail.com", "mail.ru", "yandex.ru"]

    email = f"{random.choice(first_names)}.{random.choice(last_names)}@{random.choice(domains)}"
    return email