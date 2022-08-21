import time
import pytest
from selenium.webdriver.common.by import By


class TestSelenium1py:

    def test_add_item_button(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
        browser.get(link)

        time.sleep(10) #добавил сам, т.к. по заданию непонятно кому это нужно делать, мне или ревьюеру
                       #думаю ты не обидишься и тебе хватит и 10 секунд на проверку текста)

        browser.implicitly_wait(10) #если вдруг строка выше будет удалена

        try:
            browser.find_element(By.CSS_SELECTOR, "button.btn-add-to-basket")
            is_add_item_button_on_page = True
        except:
            is_add_item_button_on_page = False

        assert is_add_item_button_on_page, "'add item' button not found"
        