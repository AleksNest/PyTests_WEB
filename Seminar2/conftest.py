import pytest
import yaml
from module import Site

with open("./testdata.yaml") as f:
    testdata = yaml.safe_load(f)

@pytest.fixture()
def select_input_login():
    return """//*[@id='login']/div[1]/label/input"""        # локатор поля ввода логина

@pytest.fixture()
def select_input_password():
    return """//*[@id='login']/div[2]/label/input"""    # локатор поля ввода пароля

@pytest.fixture()
def select_input_button():
    return """button"""                                 # локатор кнопки

@pytest.fixture()
def select_error():
    return """//*[@id='app']/main/div/div/div[2]/h2"""  # локатор появления кода ошибки

@pytest.fixture()
def select_hello_user():
    return """//*[@id='app']/main/nav/ul/li[3]/a"""  # локатор появления надписи при успешном логине и пароле

@pytest.fixture()
def select_posts():
    return """//*[@id="create-btn"]"""        # локатор входа на страницу постов

@pytest.fixture()
def select_input_title_post():
    return """//*[@id="create-item"]/div/div/div[1]/div/label/input"""        # локатор поля ввода заголовка поста

@pytest.fixture()
def select_input_description_post():
    return """//*[@id="create-item"]/div/div/div[2]/div/label/span/textarea"""        # локатор поля ввода описания поста

@pytest.fixture()
def select_input_content_post():
    return """//*[@id="create-item"]/div/div/div[3]/div/label/span/textarea"""        # локатор поля ввода контента поста





@pytest.fixture()
def select_btn_save_post():
    return '''//*[@id="create-item"]/div/div/div[7]/div/button'''
    #return """//*[@id="create-item"]/div/div/div[7]/div/button"""        # локатор кнопки save post
#create-item > div > div > div:nth-child(7) > div > button







@pytest.fixture()
def select_title_post():
    return """//*[@id="app"]/main/div/div[1]/h1"""        # локатор поля ввода заголовка поста


# вызывает экземпляр класса Site(старт ), завершает работу с страницей
@pytest.fixture()
def site():
    site_class = Site(testdata['address'])
    yield site_class        # старт работы тестов до выполнеия тестов
    site_class.close()      # после всех тестов возвращаемся к функции и закрываем ссессиюи (страницы)


