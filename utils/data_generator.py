"""
Генератор тестовых данных для автотестов Stellar Burgers
"""
import random
import string


def generate_name():
    """Генерирует случайное имя для пользователя"""
    names = ['Иван', 'Мария', 'Петр', 'Анна', 'Сергей', 'Елена', 'Дмитрий', 'Ольга']
    surnames = ['Иванов', 'Петров', 'Сидоров', 'Смирнов', 'Козлов', 'Новиков', 'Морозов', 'Петрова']
    return f"{random.choice(names)}{random.choice(surnames)}"


def generate_email(cohort_number=36):
    """
    Генерирует email в формате: имя_фамилия_номер_когорты_любые_3_цифры@домен
    Пример: даниэльхуснутдинов36123@yandex.ru
    
    Args:
        cohort_number: номер когорты (по умолчанию 36)
    
    Returns:
        str: email в требуемом формате
    """
    # Получаем имя и фамилию, объединяем их слитно (без пробелов)
    name = generate_name().lower()  # Переводим в нижний регистр для email
    random_digits = ''.join([str(random.randint(0, 9)) for _ in range(3)])
    domains = ['yandex.ru', 'mail.ru', 'gmail.com']
    domain = random.choice(domains)
    
    # Формат: имяфамилия + номер_когорты + 3_цифры + @домен
    # Пример: даниэльхуснутдинов36123@yandex.ru
    email = f"{name}{cohort_number}{random_digits}@{domain}"
    return email


def generate_login(cohort_number=36):
    """
    Генерирует логин (email) в формате: имя_фамилия_номер_когорты_любые_3_цифры@домен
    Логин - это email для входа в систему
    Пример: даниэльхуснутдинов36123@yandex.ru
    
    Args:
        cohort_number: номер когорты (по умолчанию 36)
    
    Returns:
        str: логин (email) в требуемом формате
    """
    return generate_email(cohort_number)


def generate_password(min_length=6, max_length=12):
    """
    Генерирует валидный пароль (≥6 символов)
    
    Args:
        min_length: минимальная длина пароля (по умолчанию 6)
        max_length: максимальная длина пароля (по умолчанию 12)
    
    Returns:
        str: случайный пароль
    """
    length = random.randint(min_length, max_length)
    # Используем буквы (верхний и нижний регистр), цифры и спецсимволы
    characters = string.ascii_letters + string.digits + "!@#$%^&*"
    password = ''.join(random.choice(characters) for _ in range(length))
    return password


def generate_invalid_password(max_length=5):
    """
    Генерирует невалидный пароль (<6 символов)
    
    Args:
        max_length: максимальная длина пароля (по умолчанию 5)
    
    Returns:
        str: случайный пароль длиной менее 6 символов
    """
    length = random.randint(1, max_length)
    characters = string.ascii_letters + string.digits
    password = ''.join(random.choice(characters) for _ in range(length))
    return password


def generate_test_data(cohort_number=36):
    """
    Генерирует полный набор тестовых данных
    
    Args:
        cohort_number: номер когорты (по умолчанию 36)
    
    Returns:
        dict: словарь с тестовыми данными (name, email, password)
    """
    return {
        'name': generate_name(),
        'email': generate_email(cohort_number),
        'password': generate_password()
    }
