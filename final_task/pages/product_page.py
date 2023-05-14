import unittest

from .base_page import BasePage
from selenium.common.exceptions import NoAlertPresentException
from .locators import PageObjectLocators
import math
import time

# добавление товара в корзину
class PageObject(BasePage):
        def add_product_to_basket(self):
            link = self.browser.find_element(*PageObjectLocators.BASKET_BUTTON)
            link.click()

# рассчет результата математического выражения и ввод ответа
        def solve_quiz_and_get_code(self):
            time.sleep(2)
            alert = self.browser.switch_to.alert
            x = alert.text.split(" ")[2]
            answer = str(math.log(abs((12 * math.sin(float(x))))))
            alert.send_keys(answer)
            alert.accept()
            try:
                alert = self.browser.switch_to.alert
                alert_text = alert.text
                print(f"Your code: {alert_text}")
                alert.accept()
            except NoAlertPresentException:
                print("No second alert presented")

            time.sleep(2)

# проверка, что есть сообщение о том, что товар добавлен в корзину
        def should_be_message(self):
            assert self.is_element_present(*PageObjectLocators.MESSAGE), "Message is not presented"

# проверка, что название товара в сообщении совпадает с тем товаром, который добавлен
        def should_be_equal_title(self):
            TITLE_TEXT_el = self.browser.find_element(*PageObjectLocators.TITLE)
            TITLE_TEXT = TITLE_TEXT_el.text
            TITLE_MESSAGE_TEXT_el = self.browser.find_element(*PageObjectLocators.TITLE_MESSAGE)
            TITLE_MESSAGE_TEXT = TITLE_MESSAGE_TEXT_el.text
            MESSAGE_TEXT = "Title is not equal"
            print("текст1:", TITLE_TEXT), print("текст2:", TITLE_MESSAGE_TEXT) # чтобы видеть, что сравнивается
            assert TITLE_TEXT == TITLE_MESSAGE_TEXT, MESSAGE_TEXT

# проверка, что стоимость корзины совпадает с ценой товара
        def should_be_equal_price(self):
            PRICE_TEXT_el = self.browser.find_element(*PageObjectLocators.PRICE)
            PRICE_TEXT = PRICE_TEXT_el.text
            PRICE_MESSAGE_TEXT_el = self.browser.find_element(*PageObjectLocators.PRICE_MESSAGE)
            PRICE_MESSAGE_TEXT = PRICE_MESSAGE_TEXT_el.text
            MESSAGE_TEXT = "Price is not equal"
            print("текст3:", PRICE_TEXT), print("текст4:", PRICE_MESSAGE_TEXT)  # чтобы видеть, что сравнивается
            assert PRICE_TEXT == PRICE_MESSAGE_TEXT, MESSAGE_TEXT

# проверка, что элемент не появляется на странице в течение заданного времени
        def should_not_be_success_message(self):
            assert self.is_not_element_present(*PageObjectLocators.SUCCESS_MESSAGE), \
                "Success message is presented, but should not be"

# проверка, что элемент исчезает на странице в течение заданного времени
        def should_dissapear_of_success_message(self):
            assert self.is_disappeared(*PageObjectLocators.SUCCESS_MESSAGE), \
                "Success message is presented, but should not be"

if __name__ == "__main__":
    unittest.main()