
BASE_URL = "https://stellarburgers.education-services.ru" # Базовый URL сервера

# --- Ингредиенты ---

GET_INGREDIENTS = "/api/ingredients" # Получение списка всех доступных ингредиентов для бургеров

# --- Пользователи (регистрация и авторизация) ---

POST_REGISTER = "/api/auth/register" # Создание нового пользователя (требует email, password, name)
POST_LOGIN = "/api/auth/login" # Авторизация пользователя (требует email, password)
POST_LOGOUT = "/api/auth/logout" # Выход из системы (требует refreshToken в теле запроса)
POST_TOKEN = "/api/auth/token" # Обновление accessToken по refreshToken (продлевает сессию)
GET_USER = "/api/auth/user" # Получение данных текущего пользователя (требует accessToken в заголовке)
PATCH_USER = "/api/auth/user" # Обновление данных пользователя (требует accessToken и изменяемые поля)
DELETE_USER = "/api/auth/user" # Удаление пользователя (требует accessToken)

# --- Заказы ---

POST_ORDERS = "/api/orders" # Создание нового заказа (требует авторизацию и список id ингредиентов)
GET_ORDERS_ALL = "/api/orders/all" # Получение всех заказов (публичная лента, до 50 последних)
GET_ORDERS = "/api/orders" # Получение заказов текущего пользователя (требует авторизацию)

# --- Восстановление пароля ---

POST_PASSWORD_RESET = "/api/password-reset"# Запрос на сброс пароля (отправляет email с кодом для восстановления)
POST_PASSWORD_RESET_RESET = "/api/password-reset/reset"# Установка нового пароля (требует новый пароль и токен из письма)

# Тестовые данные
class CourierData:
    VALID_LOGIN = "test_courier_2026"
    VALID_PASSWORD = "password123"
    VALID_FIRST_NAME = "Ivan"

    @staticmethod
    def generate_random_login():
        import time
        return f"courier_{int(time.time())}"

class OrderData:
    DEFAULT_FIRST_NAME = "Алексей"
    DEFAULT_LAST_NAME = "Климкин"
    DEFAULT_ADDRESS = "Москва"
    DEFAULT_METRO_STATION = 4
    DEFAULT_PHONE = "+7 800 355 35 35"
    DEFAULT_RENT_TIME = 5
    DEFAULT_DELIVERY_DATE = "2026-08-03"
    DEFAULT_COMMENT = "Saske, come back!"

