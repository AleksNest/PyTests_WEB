import time
import yaml
from selenium import webdriver  # установка силенеиума
from selenium.webdriver.common.by import By                 # селениум для Python
from selenium.webdriver.chrome.service import Service       # вариант ручного подключения драйвера для Chrome, при этом сам драйвер скачивается в проект
from webdriver_manager.firefox import GeckoDriverManager  # для автоматической установки драйвера для Firefox
from webdriver_manager.chrome import ChromeDriverManager  # для автоматической установки драйвера Chrome

with open("./testdata.yaml") as f:
    testdata = yaml.safe_load(f)
    browser = testdata["browser"]


class Site:
    def __init__(self, address):
        if browser == "firefox":
            service = Service(executable_path=GeckoDriverManager().install())       # установка драйвера при автоматической установки
            options = webdriver.FirefoxOptions()
            self.driver = webdriver.Firefox(service=service, options=options)       #свойство класса
        elif browser == "chrome":
            service = Service(executable_path=ChromeDriverManager().install())
            options = webdriver.ChromeOptions()
            self.driver = webdriver.Chrome(service=service, options=options)
        self.driver.implicitly_wait(5)          # ожидания открытия страницы
        self.driver.maximize_window()           # открывает полностью окно браузера
        self.driver.get(address)                # драйвер загружает страничку по адресу в браузере, в драйвере - код страницы
        time.sleep(testdata['sleep_time'])      # время ожидания, так как страница загружается не сразу

    def find_element(self, mode, path):         # метод поиска элемента на веб странице
        if mode == 'css':
            element = self.driver.find_element(By.CSS_SELECTOR, path)           #ищем по селектору CSS, path - берем с devtools элемента странички сайта
        elif mode == "xpath":
            element = self.driver.find_element(By.XPATH, path)
        else:
            element = None
        return element

    def get_element_property(self, mode, path, property):       # получение свойства элемента (например получение цвета кнопки)
        element = self.find_element(mode, path)
        return element.value_of_css_property(property)          # получение свойства у элемента, если свойство есть

    def close(self):
        self.driver.close()
