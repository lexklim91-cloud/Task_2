# test_api/test_user_update.py
import pytest
import allure
from api.user_api import UserAPI
from helpers import unique_user_data

user_api = UserAPI()


class TestUpdateUser:
    
    @allure.step("""Изменение данных пользователя с авторизацией - успешно""")
    @pytest.mark.parametrize("field_to_update, new_value", [
        ("email", "newewmail@example.com"),
        ("name", "NewUserName")
    ])
    def test_update_user_with_auth_success(self, created_user, field_to_update, new_value):
        update_data = {field_to_update: new_value}
        response = user_api.update_user(created_user["accessToken"], update_data)
        data = response.json()
        assert response.status_code == 200   
        assert data["success"] is True
        assert data["user"][field_to_update] == new_value
        
        # Проверяем, что изменения сохранились
        get_response = user_api.get_user(created_user["accessToken"])
        assert get_response.json()["user"][field_to_update] == new_value
    
    
    @allure.step("""Изменение данных пользователя без авторизации - ошибка 401""")
    @pytest.mark.parametrize("field_to_update, new_value", [
        ("email", "unauth@example.com"),
        ("name", "UnauthUser")
    ])
    def test_update_user_without_auth_fails(self, field_to_update, new_value):
        
        user_data = unique_user_data()
        # Создаем пользователя
        created = user_api.create_user_and_get_tokens(user_data)
        update_data = {field_to_update: new_value}
        # Пытаемся обновить без токена
        response = user_api.update_user(None, update_data)
        data = response.json()
        assert response.status_code == 401          
        assert data["success"] is False
        assert data["message"] == "You should be authorised"
        
        # Очистка
        if created.get("accessToken"):
            user_api.delete_user(created["accessToken"])
    
    
    @allure.step("""Обновление email на уже существующий - ошибка 403""")
    def test_update_email_to_existing_fails(self, created_user):
        
        # Создаем второго пользователя
        second_user_data = {
            "email": "seconduser@example.com",
            "password": "SecondPass123",
            "name": "SecondUser"
        }
        second_user_list = user_api.create_user_and_get_tokens(second_user_data)
        second_user = second_user_list.json()
        # Пытаемся обновить email первого пользователя на email второго
        update_data = {"email": second_user_data["email"]}
        response = user_api.update_user(created_user["accessToken"], update_data)
        data = response.json()
        assert response.status_code == 403                
        assert data["success"] is False
        assert data["message"] == "User with such email already exists"
        
        # Очистка
        if second_user.get("accessToken"):
            user_api.delete_user(second_user["accessToken"])