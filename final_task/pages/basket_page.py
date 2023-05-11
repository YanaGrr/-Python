from .base_page import BasePage
from .locators import BasePageLocators

class BasketPage(BasePage):
# гость переходит в корзину по кнопке в шапке сайта
    def view_basket(self):
        link = self.browser.find_element(*BasePageLocators.VIEW_BASKET_BUTTON)
        link.click()

# ожидаем, что в корзине нет товаров
    def should_no_items(self):
        assert self.is_not_element_present(*BasePageLocators.ITEMS_ARE_PRESENTED), "Basket is not empty"

# ожидаем, что есть текст о том, что корзина пуста
    def should_be_empty_basket_message(self):
        assert self.is_element_present(*BasePageLocators.EMPTY_BASKET_MESSAGE), "Message is not presented"