from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

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
