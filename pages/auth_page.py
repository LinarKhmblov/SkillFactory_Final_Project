from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import *


class AuthPage:
    """
    Класс страница авторизации
    """

    def __init__(self, driver):
        """
        Конструктор класса AuthPage.

        :param driver: объект Selenium WebDriver
        """
        self.driver = driver
        self.base_url = SITE

    def open_web_page(self):
        """
        Переходит на веб-сайта тестирования.
        """
        return self.driver.get(self.base_url)

    def find_element(self, locator, time=10):
        """
        Поиск элемента заданного локатора.

        :param locator: кортеж с стратегией и значением локатора
        :param time: максимальное время ожидания появления элемента (по умолчанию 10 секунд)
        :return: объект WebElement
        """
        return WebDriverWait(self.driver, time).until(
            EC.presence_of_element_located(locator), message=f"Не удалось найти элемент по локатору {locator}"
        )

    def click_element(self, locator):
        """
        Клик по найденному элементу.

        :param locator: кортеж с стратегией и значением локатора
        :return: None
        """
        self.find_element(locator).click()

    def input_data(self, locator, text):
        """
        Ввод текста в поле ввода.

        :param locator: кортеж с стратегией и значением локатора
        :param text: текст для ввода в поле ввода
        :return: None
        """
        self.find_element(locator).send_keys(text)

    def check_out(self, driver):
        return self.driver.switch_to.window(driver.window_handles[1])