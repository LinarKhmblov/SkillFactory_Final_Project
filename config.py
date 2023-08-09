from faker import Faker

# Основной URL тестируемого сайта
SITE = 'https://b2c.passport.rt.ru'

# Валидные данные для авторизации
USER_EMAIL = 'VALID_EMAIL'
USER_PHONE = 'VALID_PHONE (+79876543210)'
PASSWORD = 'VALID_PASSWORD'

# Невалидные данные для авторизации
fake = Faker()
invalid_psswrd = fake.password()