# api/endpoints.py

class Endpoints:
    BASE_URL = "https://stellarburgers.education-services.ru"
    
    # Ингредиенты
    GET_INGREDIENTS = f"{BASE_URL}/api/ingredients"
    
    # Пользователи
    POST_REGISTER = f"{BASE_URL}/api/auth/register"
    POST_LOGIN = f"{BASE_URL}/api/auth/login"
    POST_LOGOUT = f"{BASE_URL}/api/auth/logout"
    POST_TOKEN = f"{BASE_URL}/api/auth/token"
    GET_USER = f"{BASE_URL}/api/auth/user"
    PATCH_USER = f"{BASE_URL}/api/auth/user"
    DELETE_USER = f"{BASE_URL}/api/auth/user"
    
    # Заказы
    POST_ORDERS = f"{BASE_URL}/api/orders"
    GET_ORDERS_ALL = f"{BASE_URL}/api/orders/all"
    GET_ORDERS = f"{BASE_URL}/api/orders"
    
    # Восстановление пароля
    POST_PASSWORD_RESET = f"{BASE_URL}/api/password-reset"
    POST_PASSWORD_RESET_RESET = f"{BASE_URL}/api/password-reset/reset"