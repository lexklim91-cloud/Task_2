
import pytest
import allure
from api.user_api import UserAPI
from api.base_api import BaseAPI

user_api = UserAPI()


class TestLoginUser:
    
    @allure.step("""Логин под существующим пользователем - успешно""")
    def test_login_existing_user_success(self, created_user):
        login_data = {
            "email": created_user["email"],
            "password": created_user["password"]
        }
        response = user_api.login_user(login_data)
        assert response.status_code == 200
        data = response.json()
        assert data["success"] is True
        assert data["user"]["email"] == created_user["email"]
        assert data["user"]["name"] == created_user["name"]
        assert "accessToken" in data
        assert "refreshToken" in data
    
    
    @allure.step("""Логин с неверным логином и паролем - ошибка 401""")
    def test_login_invalid_credentials_fails(self):
        
        login_data = {
           "email": "nonexistent@example.com",
            "password": "WrongPassword123"
        }
        response = user_api.login_user(login_data)
        assert response.status_code == 401
        data = response.json()
        assert data["success"] is False
        assert data["message"] == "email or password are incorrect"
    
    
    @allure.step("""Логин без одного из полей - ошибка 401""")
    @pytest.mark.parametrize("missing_field", ["email", "password"])
    def test_login_missing_field_fails(self, missing_field):
        login_data = {
            "email": "test@example.com",
            "password": "password123"
        }
        del login_data[missing_field]
        response = user_api.login_user(login_data)
        assert response.status_code == 401
        data = response.json()
        assert data["success"] is False
        assert data["message"] == "email or password are incorrect"