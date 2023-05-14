from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .locators import BasePageLocators

class BasePage():
# конструктор — метод, который вызывается, когда мы создаем объект;
# в качестве параметров мы передаем экземпляр драйвера и url адрес, - внутри конструктора сохраняем эти данные, как аттрибуты нашего класса
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

# метод, который открывает нужную страницу в браузере, используя метод get()
    def open(self):
        self.browser.get(self.url)

# метод для открытия главной страницы
    def go_to_login_page(self):
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        link.click()

# команда для неявного ожидания со значением по умолчанию в 10
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

# метод, перехватывающий исключения
# передаётся два аргумента: как искать (css, id, xpath и тд) и что искать (строка-селектор)
    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True
# проверка, что элемент не появляется на странице в течение заданного времени
    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False
# проверка, что какой-то элемент исчезает
# используется явное ожидание вместе с функцией until_not, в зависимости от того, какой результат ожидается
    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True

# проверка, что есть ссылка, которая ведет на логин
    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"

# проверка, что пользователь залогинен
    def should_be_authorized_user(self):
        assert self.is_element_present(*BasePageLocators.USER_ICON), "User icon is not presented," \
                                                                     " probably unauthorised user"