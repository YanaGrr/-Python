from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .locators import BasePageLocators

class BasePage():
    def __init__(self, browser, url): #конструктор — метод, который вызывается, когда мы создаем объект; в качестве параметров мы передаем экземпляр драйвера и url адрес, - внутри конструктора сохраняем эти данные, как аттрибуты нашего класса
        self.browser = browser
        self.url = url
    def open(self): #метод, который открывает нужную страницу в браузере, используя метод get()
        self.browser.get(self.url)
    def __init__(self, browser, url, timeout=10): #команда для неявного ожидания со значением по умолчанию в 10
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)
    def is_element_present(self, how, what): #метод, в котором будем перехватывать исключение. В него будем передавать два аргумента: как искать (css, id, xpath и тд) и собственно что искать (строку-селектор)
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True
    def is_not_element_present(self, how, what, timeout=4): #абстрактный метод, который проверяет, что элемент не появляется на странице в течение заданного времени:
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True

        return False

    def is_disappeared(self, how, what, timeout=4): #если же мы хотим проверить, что какой-то элемент исчезает, то следует воспользоваться явным ожиданием вместе с функцией until_not, в зависимости от того, какой результат мы ожидаем
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False

        return True

    def go_to_login_page(self):  # открыть главную страницу
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        link.click()
    def should_be_login_link(self):  # проверка, что есть ссылка, которая ведет на логин
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"

    def should_be_authorized_user(self): # проверка, что пользователь залогинен
        assert self.is_element_present(*BasePageLocators.USER_ICON), "User icon is not presented," \
                                                                     " probably unauthorised user"