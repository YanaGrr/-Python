from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
# проверка страницы логина
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

# проверка на корректный url адрес
    def should_be_login_url(self):
        current_url = self.browser.current_url
        assert "login" in current_url, "Url is incorrect"

# проверка, что есть форма логина
    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

# проверка, что есть форма регистрации на странице
    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"

# регистрация пользователя
    def register_new_user(self, email, password):
        self.browser.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(email) # ввести значение в поле EMAIL
        self.browser.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(password) # ввести значение в поле PASSWORD
        self.browser.find_element(*LoginPageLocators.REPEAT_PASSWORD_INPUT).send_keys(password) # повторить пароль
        self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON).click() # нажать на кнопку "Зарегистрироваться"