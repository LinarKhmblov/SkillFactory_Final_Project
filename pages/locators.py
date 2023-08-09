from selenium.webdriver.common.by import By
from pages.auth_page import AuthPage
from selenium import webdriver

class Locators(AuthPage):
    """Локаторы страницы авторизации"""

    # Локаторы
    page_logo = (By.XPATH, '//*[@id="page-right"]/div/div/h1')  # Заголовок страницы
    phone_btn = (By.ID, "t-btn-tab-phone")  # Кнопка телефон
    mail_btn = (By.ID, "t-btn-tab-mail")  # Кнопка почта
    login_btn = (By.ID, "t-btn-tab-login")  # Кнопка 'Войти'
    ls_btn = (By.ID, "t-btn-tab-ls")  # Кнопка 'ЛС'
    mail_input_field = (By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[1]/div[2]/div/span[2]')  # Поле ввода для почты
    username_input_field = (By.ID, 'username')  # Поле ввода для имени пользователя
    password_input_field = (By.ID, 'password')  # Поле ввода для пароля
    enter_btn = (By.ID, 'kc-login')  # Кнопка 'Войти'
    logout_btn = (By.ID, 'logout-btn')  # Кнопка 'Выйти'
    error_mssg = (By.CSS_SELECTOR, '.rt-input-container__meta--error')  # Сообщение об ошибке
    empty_username = (By.CSS_SELECTOR, '.rt-input-container__meta--error')  # Сообщение об отсутствующем имени пользователя
    forgot_psswrd = (By.ID, 'forgot_password')  # Кнопка 'Забыли пароль?'
    register_btn = (By.XPATH, "//a[@id='kc-register']")  # Кнопка 'Зарегистрироваться'
    work_tab = (By.CSS_SELECTOR, '.rt-tab.rt-tab--small.rt-tab--active')  # Активная вкладка
    vk_profile_btn = (By.ID, "oidc_vk")  # Кнопка 'Вконтакте'
    vk_enter = (By.XPATH, "// div[contains(text(), 'Вход в VK ID')]")  # 'Вход в VK ID'
    ok_profile_btn = (By.ID, "oidc_ok")  # Кнопка 'Одноклассники'
    ok_enter = (By.XPATH, "//div[contains(text(),'Одноклассники')]")  # Идентификатор 'Одноклассники'
    mail_ru_btn = (By.ID, "oidc_mail")  # Кнопка 'Мой Мир@Mail.Ru'
    mail_ru_enter = (By.XPATH, "// span[contains(text(), 'Мой Мир@Mail.Ru')]")  # Идентификатор 'Мой Мир@Mail.Ru'
    yandex_btn = (By.ID, "oidc_ya")  # Кнопка 'Яндекс'
    yandex_enter = (By.XPATH, "//*[@id='UserEntryFlow']/form/div/div[1]/h1")  # Идентификатор 'Яндекс'
    terms_of_use_tab = (By.XPATH, "//a[@class='rt-link rt-link--orange' and @href='https://b2c.passport.rt.ru/sso-static/agreement/agreement.html']")  # Активная вкладка 'Пользовательское соглашение'
    terms_of_use_root = (By.ID, "root")  # Идентификатор текста соглашения
    get_back_btn = (By.ID, 'reset-back')

    # Тексты сообщений
    invalid_data_mssg = 'Неверный логин или пароль'
    invalid_captcha_mssg = 'Неверно введен текст с картинки'
    empy_phone_field_mssg = 'Введите номер телефона'
    empy_email_field_mssg = 'Введите адрес, указанный при регистрации'
    empy_login_field_mssg = 'Введите логин, указанный при регистрации'
    empy_ls_field_mssg = 'Введите номер вашего лицевого счета'
    auth_title = 'Авторизация'
    psswrd_recovery_title = 'Восстановление пароля'
    registration_title = 'Регистрация'