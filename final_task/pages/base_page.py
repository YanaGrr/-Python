from selenium import webdriver

class BasePage():
    def __init__(self, browser, url): #конструктор — метод, который вызывается, когда мы создаем объект; в качестве параметров мы передаем экземпляр драйвера и url адрес, - внутри конструктора сохраняем эти данные, как аттрибуты нашего класса
        self.browser = browser
        self.url = url
    def open(self): #метод, который открывает нужную страницу в браузере, используя метод get()
        self.browser.get(self.url)