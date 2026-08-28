# helpers.py
import random
import time


"""Генерирует уникальные данные для регистрации пользователя"""
def unique_user_data():
    
    timestamp = int(time.time() * 1000)
    return {
        "email": f"test_{timestamp}@example.com",
        "password": f"Pass{timestamp}",
        "name": f"User_{timestamp}"
    }
    
    
"""Генерирует случайный email (для вспомогательных тестов)"""
def generate_email():
    first_names = ["alex", "maria", "alex", "anna"]
    last_names = ["smith", "ivanov", "doe", "petrov"]
    domains = ["gmail.com", "mail.ru", "yandex.ru"]
    email = f"{random.choice(first_names)}.{random.choice(last_names)}@{random.choice(domains)}"
    return email