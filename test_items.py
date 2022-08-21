import time
import math
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestSelenium1py:

    def test_add_item_button(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
        browser.get(link)

        time.sleep(30) #добавил сам, т.к. по заданию непонятно кому это нужно делать, мне или ревьюеру
                       #думаю ты не обидишься)

        browser.implicitly_wait(10)

        try:
            browser.find_element(By.CSS_SELECTOR, "button.btn-add-to-basket")
            is_add_item_button_on_page = True
        except:
            is_add_item_button_on_page = False

        assert is_add_item_button_on_page, "'add item' button not found"
        