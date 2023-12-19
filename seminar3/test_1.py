from testPage import  OperationsHelper
import logging
import yaml
import pytest
import time

with open("./testdata.yaml") as f:
    testdata = yaml.safe_load(f)


# тест на проверку ввода неправильных логина и пароля
def test_step_1(browser):   # драйвер браузера берет из фикстуры
    logging.info("Test1 start")
    testpage = OperationsHelper(browser)   # создание экземаляра для работы с операциями со страницей, который подтягивает также класс BasePage
    testpage.go_to_site()   # открытие страницы
    testpage.enter_login("test")  # ввод слова в поле логина
    testpage.enter_pass("test")
    testpage.click_login_button()
    assert testpage.get_error_text() == '401'

#тест на проверку ввода валидных логина и пароля
def test_step_2(browser):
    logging.info("Test2 start")
    testpage = OperationsHelper(browser)
    testpage.go_to_site()
    testpage.enter_login(testdata['login'])
    testpage.enter_pass(testdata['password'])
    testpage.click_login_button()
    assert testpage.get_hello_user() == f'Hello, {testdata["login"]}'


# тест на проверку добавления поста
def test_step_3(browser):
    logging.info("Test3 start")
    testpage = OperationsHelper(browser)
    testpage.go_to_site()
    testpage.enter_login(testdata['login'])
    testpage.enter_pass(testdata['password'])
    testpage.click_login_button()
    testpage.click_add_post_button()
    testpage.enter_title_post('Заголовок новый')
    testpage.enter_description_post('Описание новое')
    testpage.enter_content_post('контент новый')
    testpage.click_save_post()
    time.sleep(5)
    assert testpage.get_title_post() == 'Заголовок новый'

# тест на проверку появления alert при валидном заполнение формы Contact us
def test_step4(browser):
    logging.info("Test4 start")
    testpage = OperationsHelper(browser)
    testpage.go_to_site()
    testpage.enter_login(testdata['login'])
    testpage.enter_pass(testdata['password'])
    testpage.click_login_button()
    time.sleep(2)
    testpage.click_contuct_buttton()
    time.sleep(2)
    testpage.enter_name_contuct_page('Алексей')
    testpage.enter_email_contuct_page('al_nest@inbox.ru')
    testpage.enter_content_contuct_page('контент')
    testpage.click_contuct_us_buttton()
    time.sleep(3)
    assert  testpage.get_alert() == 'Form successfully submitted'






