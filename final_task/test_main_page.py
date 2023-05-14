import pytest
from .pages.base_page import BasePage
from .pages.basket_page import BasketPage

link = "http://selenium1py.pythonanywhere.com"


@pytest.mark.login_guest  # логическая сгруппировка тестов в один класс просто ради более стройного кода
class TestLoginFromMainPage():
    # 1. проверка, что есть ссылка, которая ведет на логин
    def test_guest_should_see_login_link(self, browser):
        page = BasePage(browser, link)  # инициализируем BasePage, передаем в конструктор экземпляр драйвера и url адрес
        page.open()  # открываем страницу
        page.should_be_login_link()  # проверка, что есть ссылка, которая ведет на логин

    # 2. проверка, что пользователь может войти или залогиниться
    def test_guest_can_go_to_login_page(self, browser):
        page = BasePage(browser, link)  # инициализируем BasePage, передаем в конструктор экземпляр драйвера и url адрес
        page.open()  # открываем страницу
        page.go_to_login_page()  # выполняем метод страницы — переходим на страницу логина
        login_page = BasePage(browser,
                              browser.current_url)  # аналогично: return LoginPage(browser=self.browser, url=self.browser.current_url)
        login_page.should_be_login_link()  # проверка, что есть ссылка, которая ведет на логин


# 3. проверка перехода в корзину
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    page = BasketPage(browser, link)  # инициализируем BasketPage, передаем в конструктор экземпляр драйвера и url адрес
    page.open()  # открываем главную страницу
    page.view_basket()  # переходим в корзину по кнопке в шапке сайта
    page.should_no_items()  # ожидаем, что в корзине нет товаров
    page.should_be_empty_basket_message()  # ожидаем, что есть текст о том, что корзина пуста