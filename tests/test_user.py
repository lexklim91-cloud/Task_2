
import pytest
import allure
from api.user_api import UserAPI

user_api = UserAPI()


class TestCreateUser:
    @allure.step("""Создание уникального пользователя - успешный сценарий""")
    def test_create_unique_user_success(self, unique_user_data):
        
        response = user_api.register_user(unique_user_data)
        data = response.json()
        assert response.status_code == 200
        assert data["success"] is True
        assert data["user"]["email"] == unique_user_data["email"]
        assert data["user"]["name"] == unique_user_data["name"]
        assert "accessToken" in data
        assert "refreshToken" in data
        assert data["accessToken"].startswith("Bearer ")
        
        # Очистка - удаляем созданного пользователя
        if data.get("accessToken"):
            user_api.delete_user(data["accessToken"])
    
    
    @allure.step("""Создание пользователя, который уже зарегистрирован - ошибка 403""")
    def test_create_existing_user_fails(self, created_user):
        
        user_data = {
            "email": created_user["email"],
            "password": created_user["password"],
            "name": created_user["name"]
        }
        
        response = user_api.register_user(user_data)
        data = response.json()
        assert response.status_code == 403
        assert data["success"] is False
        assert data["message"] == "User already exists"
    
    
    @allure.step("""Создание пользователя без одного обязательного поля - ошибка 403""")
    @pytest.mark.parametrize("missing_field", ["email", "password", "name"])
    def test_create_user_missing_field_fails(self, unique_user_data, missing_field):
        
        user_data = unique_user_data.copy()
        del user_data[missing_field]
        
        response = user_api.register_user(user_data)
        data = response.json()
        assert response.status_code == 403
        assert data["success"] is False
        assert data["message"] == "Email, password and name are required fields"