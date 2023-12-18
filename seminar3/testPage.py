#Расширение BasePage дополлнительными операциями функции по управлению элементами страниц ( более детальные операции, которые могут меняться
# локаторы хранятся

import logging
from baseApp import BasePage
from selenium.webdriver.common.by import By


class TestSearchLocators:
    LOCATOR_LOGIN_FIELD = (By.XPATH, """//*[@id='login']/div[1]/label/input"""  )       # локатор поля логина
    LOCATOR_PASS_FIELD = (By.XPATH, """//*[@id='login']/div[2]/label/input""")          # локатор поля пароля
    LOCATOR_LOGIN_BTN = (By.CSS_SELECTOR, 'button')                                     # локатор кнопки зарегестрироваться
    LOCATOR_ERROR_FIELD = (By.XPATH,"""//*[@id='app']/main/div/div/div[2]/h2""" )       # локатор кода ошибки при неправильном пароле
    LOCATOR_SUCCESS_FIELD = (By.XPATH,"""//*[@id='app']/main/nav/ul/li[3]/a""" )        # локатор отображения приветствия при правильном вводе логина - пароля
    LOCATOR_ADD_POST_BTN = (By.XPATH,"""//*[@id="create-btn"]""" )                      # локатор кнопки добавления поста
    LOCATOR_TITLE_POST = (By.XPATH,"""//*[@id="create-item"]/div/div/div[1]/div/label/input""" )    # локатор поля ввода заголока поста
    LOCATOR_DESCRIPTION_POST = (By.XPATH, """//*[@id="create-item"]/div/div/div[2]/div/label/span/textarea""")  # локатор поля ввода описания поста
    LOCATOR_CONTENT_POST = (
    By.XPATH, """//*[@id="create-item"]/div/div/div[3]/div/label/span/textarea""")  # локатор поля ввода контента поста
    LOCATOR_SAVE_POST_BTN = (By.XPATH,'''//*[@id="create-item"]/div/div/div[7]/div/button''')  # локатор кнопки сохранить пост
    LOCATOR_OUTPUT_TITLE_POST = (By.XPATH,'''//*[@id="app"]/main/div/div[1]/h1''' )  # локатор вывода заголовка поста

    LOCATOR_CONTACT_BTN = (By.XPATH, '''//*[@id="app"]/main/nav/ul/li[2]/a''')       # локатор кнопки Contuct us
    LOCATOR_NAME_CONTACTPAGE = (By.XPATH,'''//*[@id="contact"]/div[1]/label/input''')   # локатор поля ввода имени на странице Contuct us
    LOCATOR_EMAIL_CONTACTPAGE = (By.XPATH, '''//*[@id="contact"]/div[2]/label/input''')  # локатор поля ввода почты на странице Contuct us
    LOCATOR_CONTENT_CONTACTPAGE = (By.XPATH, '''//*[@id="contact"]/div[3]/label/span/textarea''')  # локатор поля ввода контента на странице Contuct us
    LOCATOR_CONTUCT_US_BTN = (By.XPATH, '''//*[@id="contact"]/div[4]/button''')   # Локатор кнопки contuct us


class OperationsHelper(BasePage):       # наследуется от класса BasePage

    # метод вводо логина в поле логина
    def enter_login(self, word):
        logging.info(f"send {word} of element {TestSearchLocators.LOCATOR_LOGIN_FIELD[1]}")
        login_field = self.find_element(TestSearchLocators.LOCATOR_LOGIN_FIELD)                  # поиск поля Login на странице сайта с помощью локатора
        login_field.clear()  # стирается поле ввода логина
        login_field.send_keys(word)                 # посылается word в поле логина

    # метод ввода пароля в поле пароля
    def enter_pass(self, word):
        logging.info(f"send {word} of element {TestSearchLocators.LOCATOR_PASS_FIELD[1]}")
        pass_field = self.find_element(TestSearchLocators.LOCATOR_PASS_FIELD)
        pass_field.clear()  # стирается поле ввода логина
        pass_field.send_keys(word)  # посылается word в поле логина

    # метод нажатия кнопки
    def click_login_button(self):
        logging.info(f"click login button")
        self.find_element(TestSearchLocators.LOCATOR_LOGIN_BTN).click()

    # метод возврата текста кода ошибки при вводе непраильного логина-пароля
    def get_error_text(self):
        error_field = self.find_element(TestSearchLocators.LOCATOR_ERROR_FIELD, time=5)
        text = error_field.text
        logging.info(f"we find text {text} in error field {TestSearchLocators.LOCATOR_ERROR_FIELD[1]}")
        return text

    # метод получения приветствия пользоывтеля при успешном входе в пост
    def get_hello_user(self):
        hello_user = self.find_element(TestSearchLocators.LOCATOR_SUCCESS_FIELD, time=5)
        text = hello_user.text
        logging.info(f"we find text {text} in error field {TestSearchLocators.LOCATOR_SUCCESS_FIELD[1]}")
        return text

    # метод нажатия на кнопку добавления поста
    def click_add_post_button(self):
        logging.info(f"click add postbutton")
        self.find_element(TestSearchLocators.LOCATOR_ADD_POST_BTN).click()

    # метод ввода заголовка поста
    def enter_title_post(self, word):
        logging.info(f"send {word} of element {TestSearchLocators.LOCATOR_TITLE_POST[1]}")
        title_post_field = self.find_element(TestSearchLocators.LOCATOR_TITLE_POST)
        title_post_field.clear()  # стирается поле ввода
        title_post_field.send_keys(word)  # посылается word в поле

    # метод ввода описания поста
    def enter_description_post(self, word):
        logging.info(f"send {word} of element {TestSearchLocators.LOCATOR_DESCRIPTION_POST[1]}")
        des_post_field = self.find_element(TestSearchLocators.LOCATOR_DESCRIPTION_POST)
        des_post_field.clear()  # стирается поле ввода
        des_post_field.send_keys(word)  # посылается word в поле

    # метод ввода контента поста
    def enter_content_post(self, word):
        logging.info(f"send {word} of element {TestSearchLocators.LOCATOR_CONTENT_POST[1]}")
        cont_post_field = self.find_element(TestSearchLocators.LOCATOR_CONTENT_POST)
        cont_post_field.clear()  # стирается поле ввода
        cont_post_field.send_keys(word)  # посылается word в поле

    # метод нажатия на кнопку сохранения поств
    def click_save_post(self):
        logging.info(f"click add savebutton")
        self.find_element(TestSearchLocators.LOCATOR_SAVE_POST_BTN).click()

        # метод получения наименования заголовка поста при успешном добавлении поста
    def get_title_post(self):
        title_post = self.find_element(TestSearchLocators.LOCATOR_OUTPUT_TITLE_POST, time=5)
        text = title_post.text
        logging.info(f"we find text {text} in error field {TestSearchLocators.LOCATOR_OUTPUT_TITLE_POST}")
        return text

    def click_contuct_buttton(self):
        logging.info(f"click contuct button")
        self.find_element(TestSearchLocators.LOCATOR_CONTACT_BTN).click()

    def click_contuct_us_buttton(self):
        logging.info(f"click contuct us button")
        self.find_element(TestSearchLocators.LOCATOR_CONTUCT_US_BTN).click()

    def enter_name_contuct_page(self, word):
        logging.info(f"send {word} of element {TestSearchLocators.LOCATOR_NAME_CONTACTPAGE[1]}")
        name_contact_field = self.find_element(TestSearchLocators.LOCATOR_NAME_CONTACTPAGE)
        name_contact_field.clear()  # стирается поле ввода
        name_contact_field.send_keys(word)  # посылается word в поле

    def enter_email_contuct_page(self, word):
        logging.info(f"send {word} of element {TestSearchLocators.LOCATOR_EMAIL_CONTACTPAGE[1]}")
        email_contact_field = self.find_element(TestSearchLocators.LOCATOR_EMAIL_CONTACTPAGE)
        email_contact_field.clear()  # стирается поле ввода
        email_contact_field.send_keys(word)  # посылается word в поле

    def enter_content_contuct_page(self, word):
        logging.info(f"send {word} of element {TestSearchLocators.LOCATOR_CONTENT_CONTACTPAGE[1]}")
        content_contact_field = self.find_element(TestSearchLocators.LOCATOR_CONTENT_CONTACTPAGE)
        content_contact_field.clear()  # стирается поле ввода
        content_contact_field.send_keys(word)  # посылается word в поле