import pytest
import time
from .pages.product_page import PageObject
from .pages.base_page import BasePage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage

link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"


# 1. проверка, что есть ссылка, которая ведет на логин
def test_guest_should_see_login_link_on_product_page(browser):
    page = BasePage(browser, link)  # инициализируем BasePage, передаем в конструктор экземпляр драйвера и url адрес
    page.open()  # открываем страницу
    page.should_be_login_link()  # проверка, что есть ссылка, которая ведет на логин


# 2. проверка, что пользователь может войти или залогиниться
@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    page = BasePage(browser, link)  # инициализируем BasePage, передаем в конструктор экземпляр драйвера и url адрес
    page.open()  # открываем страницу
    page.should_be_login_link()  # выполняем метод страницы — переходим на страницу логина
    login_page = BasePage(browser,
                          browser.current_url)  # аналогично: return LoginPage(browser=self.browser, url=self.browser.current_url)
    login_page.go_to_login_page()  # проверка, что есть ссылка, которая ведет на логин


# 3. проверка перехода в корзину
@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = BasketPage(browser, link)  # инициализируем BasketPage, передаем в конструктор экземпляр драйвера и url адрес
    page.open()  # гость открывает главную страницу
    page.view_basket()  # переходит в корзину по кнопке в шапке сайта
    page.should_no_items()  # ожидаем, что в корзине нет товаров
    page.should_be_empty_basket_message()  # ожидаем, что есть текст о том, что корзина пуста


@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  pytest.param(
                                      "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
                                      marks=pytest.mark.xfail)
                                  ])
# 4. проверка добавления в корзину товаров по акции (оставлено 2е ссылки: корректная и с ошибкой)
@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser, link):
    page = PageObject(browser,
                      link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()  # открываем страницу
    page.add_product_to_basket()  # нажимаем на кнопку "Добавить в корзину"
    page.solve_quiz_and_get_code()  # считаем результат математического выражения и вводим ответ
    page.should_be_message()  # проверка, что есть сообщение о том, что товар добавлен в корзину
    page.should_be_equal_title()  # проверка, что название товара в сообщении совпадает с тем товаром, который добавлен
    page.should_be_equal_price()  # проверить, что стоимость корзины совпадает с ценой товара


# 5. проверка наличия сообщения об успехе при добавлении товара в корзину (обратная проверка - проверка, что тест падает при наличии сообщения)
@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = PageObject(browser,
                      link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()  # открываем страницу
    page.add_product_to_basket()  # нажимаем на кнопку "Добавить в корзину"
    page.should_not_be_success_message()  # проверяем, что нет сообщения об успехе с помощью is_not_element_present


# 6. проверка отсутствия сообщения об успехе, если не добавлять товар в корзину
def test_guest_cant_see_success_message(browser):
    page = PageObject(browser,
                      link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()  # открываем страницу
    page.should_not_be_success_message()  # проверяем, что нет сообщения об успехе с помощью is_not_element_present


# 7. проверка наличия сообщения об успехе при добавлении товара в корзину (обратная проверка - проверка, что тест падает при наличии сообщения)
@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = PageObject(browser,
                      link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()  # открываем страницу
    page.add_product_to_basket()  # нажимаем на кнопку "Добавить в корзину"
    page.should_dissapear_of_success_message()  # проверяем, что нет сообщения об успехе с помощью is_disappeared


class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    # 8. регистрация
    def setup(self, browser):
        page = PageObject(browser,
                          link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.open()  # открываем страницу
        page.go_to_login_page()  # открываем страницу
        page = LoginPage(browser, browser.current_url)  # переходим на страницу логина
        email = str(time.time()) + "@fakemail.org"  # значение для email
        password = "h?AwPZ}%g"  # значения для пароля
        page.register_new_user(email, password)  # выполняем регистрацию
        page.should_be_authorized_user()  # проверка, что пользователь зарегистрирован

    # 9. проверка отсутствия сообщения об успехе, если не добавлять товар в корзину
    def test_user_cant_see_success_message(self, browser):
        page = PageObject(browser,
                          link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.open()  # открываем страницу
        page.should_not_be_success_message()  # проверяем, что нет сообщения об успехе с помощью is_not_element_present

    # 10. проверка добавления в корзину товаров зарегистрированным пользователем
    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        page = PageObject(browser,
                          link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.open()  # открываем страницу
        page.add_product_to_basket()  # нажимаем на кнопку "Добавить в корзину"
        page.should_be_message()  # проверка, что есть сообщение о том, что товар добавлен в корзину
        page.should_be_equal_title()  # проверка, что название товара в сообщении совпадает с тем товаром, который добавлен
        page.should_be_equal_price()  # проверить, что стоимость корзины совпадает с ценой товара
