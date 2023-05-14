from selenium.webdriver.common.by import By

class MainPageLocators(): pass # заглушка

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form") # форма "Войти"
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form") # форма "Зарегистрироваться"
    EMAIL_INPUT = (By.NAME, "registration-email") # поле для ввода EMAIL в форме "Зарегистрироваться"
    PASSWORD_INPUT = (By.NAME, "registration-password1") # поле для ввода PASSWORD в форме "Зарегистрироваться"
    REPEAT_PASSWORD_INPUT = (By.NAME, "registration-password2") # поле для повторного ввода PASSWORD в форме "Зарегистрироваться"
    REGISTER_BUTTON = (By.NAME, "registration_submit") # кнопка "Зарегистрироваться"

class PageObjectLocators:
    TITLE = (By.CSS_SELECTOR,"h1") # название книги на сайте
    TITLE_MESSAGE = (By.CSS_SELECTOR, "div.alertinner strong") # название книги в сообщении
    PRICE = (By.CSS_SELECTOR,"p.price_color") # цена на сайте
    PRICE_MESSAGE = (By.CSS_SELECTOR, "div.alertinner p strong") # цена в сообщении
    MESSAGE = (By.CSS_SELECTOR, "#messages") # блок с сообщениями об успешном добавлении книги
    BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket") # кнопка "Добавить в корзину"
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success") # сообщение [название книги] был добавлен в вашу корзину

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link") # кнопка "Войти или зарегистрироваться"
    VIEW_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-group .btn-default") # кнопка "Посмотреть корзину"
    EMPTY_BASKET_MESSAGE = (By.CSS_SELECTOR, "#content_inner p") # сообщение о пустой корзине
    ITEMS_ARE_PRESENTED = (By.CSS_SELECTOR, ".basket-title") # товары в корзине
    USER_ICON = (By.CSS_SELECTOR, ".icon-user") # пользователь зарегистрирован