"""
Автотесты проверки страницы авторизации сайта Ростелеком.
Ссылка на тест-кейсы 'https://docs.google.com/spreadsheets/d/1-bBIuIFrSoDuJZaEMxpDhLj635Hd5Off4txA1LvEw2Y/edit?usp=sharing'
"""

from config import *
import pytest


class TestAuthorizationPage:
    """Класс тестов проверяющие страницу авторизации"""

    # AT0001 Открывается страница с формой "Авторизация"
    def test001_authorization_page_is_open(self, auth):
        """"Проверяет что страница авторизации открыта"""

        base_url = 'https://b2c.passport.rt.ru/'
        current_url = auth.driver.current_url

        assert base_url == current_url, 'URL открытого сайта не сответствует ожидаемому base_url'
        assert auth.find_element(auth.page_logo).text == auth.auth_title, 'Логотип открытой страницы не соответствует эталону, либо перешли по другой ссылке'

    # AT0002 Пункт меню "Почта" кликабелен и открывает форму авторизации по почте и паролю
    def test002_mail_logo(self, auth):
        """Проверка открытия формы авторизации по почтовому адресу и паролю"""

        auth.click_element(auth.mail_btn)
        assert auth.find_element(auth.mail_input_field), "Отсутствует поле ввода адреса эл. почты"

    # AT0003, AT0004
    # Базовая позитивная проверка авторизации по валидным телефону/почте и паролю.
    # По умолчанию при открытии страницы открыта форма авторизации по телефону -- таб "Телефон"
    # При вводе почты таб "Телефон" переключается на таб "Почта"
    @pytest.mark.fail_if_captcha
    @pytest.mark.parametrize('username', [USER_PHONE, USER_EMAIL], ids=['valid phone', 'valid email'])
    def test003_valid_authorization(self, auth, username):
        """"Проверка авторизации валидными данными"""

        auth.input_data(auth.username_input_field, username)
        auth.input_data(auth.password_input_field, PASSWORD)
        auth.click_element(auth.enter_btn)
        assert auth.find_element(auth.logout_btn), "Отсутствует кнопка выхода"

    # AT0005, AT0006
    # Негативный тест авторизации по валидным телефону/почте и невалидному паролю. Появляется сообщение об ошибке.
    @pytest.mark.fail_if_captcha
    @pytest.mark.parametrize('username', [USER_PHONE, USER_EMAIL], ids=['valid phone', 'valid email'])
    def test005_authorization_with_invalid_psswrd(self, auth, username):
        """Проверка авторизации с невалидным паролем"""

        auth.input_data(auth.username_input_field, username)
        auth.input_data(auth.password_input_field, invalid_psswrd)
        auth.click_element(auth.enter_btn)
        assert auth.find_element(auth.error_mssg).text == auth.invalid_data_mssg

    # AT0007 Негативный тест авторизации по пустому полю ввода телефона и валидному паролю. Появляется сообщение об ошибке.
    # AT0008 Негативный тест авторизации по пустому полю ввода телефона и пустому полю пароля. Появляется сообщение об ошибке.
    @pytest.mark.parametrize('password', [PASSWORD, ''], ids=['valid password', 'invalid password (empty input)'])
    def test007_authorization_with_empty_phone_field(self, auth, password):
        """Проверка авторизации с пустым полем для ввода номера телефона"""

        auth.click_element(auth.phone_btn)
        auth.input_data(auth.username_input_field, '')
        auth.input_data(auth.password_input_field, password)
        auth.click_element(auth.enter_btn)
        assert auth.find_element(auth.empty_username).text == auth.empy_phone_field_mssg

    # AT0009 Негативный тест авторизации по пустому полю ввода почты и валидному паролю. Появляется сообщение об ошибке.
    def test009_authorization_with_empty_mail_field(self, auth):
        """Авторизация с пустым полем ввода почты"""

        auth.click_element(auth.mail_btn)
        auth.input_data(auth.username_input_field, '')
        auth.input_data(auth.password_input_field, PASSWORD)
        auth.click_element(auth.enter_btn)
        assert auth.find_element(auth.empty_username).text == auth.empy_email_field_mssg

    # AT00010 Негативный тест авторизации по пустому полю ввода логина и валидному паролю. Появляется сообщение об ошибке
    def test010_authorization_with_empty_login_field(self, auth):
        """Авторизация с пустым полем ввода логина"""

        auth.click_element(auth.login_btn)
        auth.input_data(auth.username_input_field, '')
        auth.input_data(auth.password_input_field, PASSWORD)
        auth.click_element(auth.enter_btn)
        assert auth.find_element(auth.empty_username).text == auth.empy_login_field_mssg

    # AT0011 Негативный тест авторизации по пустому полю ввода лицевого счета и валидному паролю.
    # Появляется сообщение об ошибке.
    def test011_authorization_with_empty_ls_field(self, auth):
        """Авторизация с пустым полем ввода лицевого счета"""

        auth.click_element(auth.ls_btn)
        auth.input_data(auth.username_input_field, '')
        auth.input_data(auth.password_input_field, PASSWORD)
        auth.click_element(auth.enter_btn)
        assert auth.find_element(auth.empty_username).text == auth.empy_ls_field_mssg

    # AT0012 Ссылка "Забыл пароль" кликабельна и открывает форму "Восстановление пароля"
    def test012_open_password_recovery_form(self, auth):
        """
        Проверка открытия формы 'Восстановление пароля'
        Проверка возвращения на страницу 'Авторизации'
        """

        auth.click_element(auth.forgot_psswrd)
        assert auth.find_element(auth.page_logo).text == auth.psswrd_recovery_title

        auth.click_element(auth.get_back_btn)
        assert auth.find_element(auth.page_logo).text == auth.auth_title, 'Логотип открытой страницы не соответствует эталону, либо перешли по другой ссылке'

    # AT0013 Ссылка "Зарегистрироваться" кликабельна и открывает форму "Регистрация"
    def test013_open_registration_form(self, auth):
        """Проверка открытия формы 'Регистрация'"""

        auth.click_element(auth.register_btn)
        assert auth.find_element(auth.page_logo).text == auth.registration_title, "Форма 'Регистрация' не открылась. Либо изменился эталонный текст "

    # AT0014 Позитивная проверка авторизации по валидному телефону и паролю при вводе телефона в таб "Почта"
    @pytest.mark.fail_if_captcha
    def test014_authorization_valid_phone_tab_mail(self, auth):
        """Проверка авторизации по вводу номера телефона в таб 'Почта'"""

        auth.click_element(auth.mail_btn)
        auth.input_data(auth.username_input_field, USER_PHONE)
        auth.input_data(auth.password_input_field, PASSWORD)
        active_tab_name = auth.find_element(auth.work_tab).text
        auth.click_element(auth.enter_btn)
        assert auth.find_element(auth.logout_btn)
        assert active_tab_name == 'Телефон'

    # AT0015 Позитивная проверка авторизации по валидному телефону и паролю при вводе телефона в таб "Логин"
    @pytest.mark.fail_if_captcha
    def test015_authorization_valid_phone_tab_login(self, auth):
        """Проверка авторизации по вводу номера телефона в таб 'Логин'"""

        auth.click_element(auth.login_btn)
        auth.input_data(auth.username_input_field, USER_PHONE)
        auth.input_data(auth.password_input_field, PASSWORD)
        active_tab_name = auth.find_element(auth.work_tab).text
        auth.click_element(auth.enter_btn)
        assert auth.find_element(auth.logout_btn)
        assert active_tab_name == 'Телефон'

    # AT0016 Позитивная проверка авторизации по валидному телефону и паролю при вводе телефона в таб "Лицевой счет"
    @pytest.mark.fail_if_captcha
    def test016_authorization_valid_phone_tab_ls(self, auth):
        """Проверка авторизации по вводу номера телефона в таб 'Лицевой счет'"""

        auth.click_element(auth.ls_btn)
        auth.input_data(auth.username_input_field, USER_PHONE)
        auth.input_data(auth.password_input_field, PASSWORD)
        active_tab_name = auth.find_element(auth.work_tab).text
        auth.click_element(auth.enter_btn)
        assert auth.find_element(auth.logout_btn)
        assert active_tab_name == 'Телефон'

    # AT0017 Позитивная проверка перехода на страницу авторизации через соц. сеть Вконтакте
    def test017_authorization_with_vk_profile(self, auth):
        """Проверка авторизации через профиль во Вконтакте"""

        auth.click_element(auth.vk_profile_btn)
        assert auth.find_element(auth.vk_enter)

    # AT0018 Позитивная проверка перехода на страницу авторизации через соц. сеть Однокласники
    def test018_authorization_social_network_ok(self, auth):
        """Проверка авторизации через профиль в Одноклассниках"""

        auth.open_web_page()
        auth.click_element(auth.ok_profile_btn)
        assert auth.find_element(auth.ok_enter)

    # AT0019 Позитивная проверка перехода на страницу авторизации через почтовый клиент Mail.ru
    def test019_authorization_social_mail(self, auth):
        """Проверка авторизации через почтовый клиент Mail.ru"""

        auth.click_element(auth.mail_ru_btn)
        assert auth.find_element(auth.mail_ru_enter)

    # AT0020 Позитивная проверка перехода на страницу авторизации через сервис клиент Yandex ID
    def test020_authorization_social_yandex(self, auth):
        """Проверка авторизации через сервис клиент Yandex ID"""

        auth.click_element(auth.yandex_btn)
        if auth.find_element(auth.yandex_btn):
            auth.click_element(auth.yandex_btn)
            assert auth.find_element(auth.yandex_enter)
        else:
            assert auth.find_element(auth.yandex_enter)

    # AT0021 Позитивная проверка перехода на страницу пользовательского соглашения
    def test021_agreement_is_clickable(self, auth):
        """Проверка открытия и перехода на страницу пользовательского соглашения"""

        auth.click_element(auth.terms_of_use_tab)
        windows = auth.driver.window_handles
        auth.driver.switch_to.window(windows[-1])

        assert auth.find_element(auth.terms_of_use_root)


