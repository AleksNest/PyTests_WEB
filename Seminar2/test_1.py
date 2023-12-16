import yaml
from module import Site
import time

with open("./testdata.yaml") as f:
    testdata = yaml.safe_load(f)

#site = Site(testdata['address'])            # создаем экземпляр класса

# проверка вывода ошибки 401 при невалидном вводе логина и пароля
def test_step1(site, select_input_login, select_input_password, select_input_button, select_error):
    #x_selector1 = """//*[@id='login']/div[1]/label/input"""     # берем с сdevtools селектор (локатор-путь) элемента на страничке сайта поля ввода логина
    #input1 = site.find_element("xpath", x_selector1)            # находим элемент поля логина
    input1 = site.find_element("xpath", select_input_login)     # используем фикстуры - заменяет 2 верхних строки
    input1.send_keys("test")                                    # отправляем в поле логина слово test

    #x_selector2 = """//*[@id='login']/div[2]/label/input"""     # берем с сdevtools элемента на страничке сайта поля ввода пароля
    #input2 = site.find_element("xpath", x_selector2)
    input2 = site.find_element("xpath", select_input_password)
    input2.send_keys("test")

    #btn_selector = 'button'                                      # берем с сdevtools селектор (путь) элемент на страничке сайта кнопки
    #btn = site.find_element('css', btn_selector)                # нашли элемент  button (кнопка)
    btn = site.find_element('css', select_input_button)
    btn.click()                                                 # кликаем на эту кнопку
    #x_selector3 = """//*[@id='app']/main/div/div/div[2]/h2"""   # берем с сdevtools селектор (путь) элемента текста кода ошибки "401"
    #err_label = site.find_element("xpath", x_selector3)         # нашли элемент  кода ошибки
    err_label = site.find_element("xpath", select_error)

    assert err_label.text == '401'                              # текст ошибки элемента вывода кода ошибки должен быть равен 401


# проверка входа при валидном логине и пароле
def test_step2(site, select_input_login, select_input_password, select_input_button, select_hello_user):

    input1 = site.find_element("xpath", select_input_login)
    input1.send_keys(testdata['login'])
    input2 = site.find_element("xpath", select_input_password)
    input2.send_keys(testdata['password'])
    btn = site.find_element('css', select_input_button)
    btn.click()

    hello_user = site.find_element("xpath", select_hello_user)
    assert hello_user.text == f'Hello, {testdata["login"]}'




def test_step3(site, select_input_login, select_input_password, select_input_button, select_posts,  select_input_title_post, select_input_description_post, select_input_content_post, select_btn_save_post, select_title_post):
    # вход на сайт
    input1 = site.find_element("xpath", select_input_login)
    input1.send_keys(testdata['login'])
    input2 = site.find_element("xpath", select_input_password)
    input2.send_keys(testdata['password'])
    btn = site.find_element('css', select_input_button)
    btn.click()

    # вход на страницу создания поста
    btn1 = site.find_element("xpath", select_posts)
    btn1.click()

   # добавление поста
    input3 = site.find_element("xpath", select_input_title_post)
    input3.send_keys("Заголовок1")
    input4 = site.find_element("xpath", select_input_description_post)
    input4.send_keys("Описание1")
    input5 = site.find_element("xpath", select_input_content_post)
    input5.send_keys("Контент1")

    time.sleep(3)
    btn_save = site.find_element("xpath", select_btn_save_post)
    btn_save.click()
    time.sleep(3)
    title_post = site.find_element("xpath", select_title_post)
    assert title_post.text == 'Заголовок1'


