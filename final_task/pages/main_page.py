from .base_page import BasePage
from selenium.webdriver.common.by import By

class MainPage(BasePage): #класс-предок в Python указывается в скобках
        def go_to_login_page(self): #открыть главную страницу
            login_link = self.browser.find_element(By.CSS_SELECTOR, "#login_link")
            login_link.click()
        def should_be_login_link(self): #проверить, что есть ссылка, которая ведет на логин
            assert self.is_element_present(By.CSS_SELECTOR, "#login_link"), "Login link is not presented"
