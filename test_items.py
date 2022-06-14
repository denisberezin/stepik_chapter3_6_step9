import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

class TestMainPage():

    def test_add_to_basket_button_exists(self, browser):
        browser.get(link)
        time.sleep(30)
        items = browser.find_elements(By.CSS_SELECTOR, ".btn-add-to-basket")
        assert items, "Add to basket button not found"

