from selenium import webdriver
from selenium.webdriver.common.by import By
import time # эта строка добавлена заранее, чтобы проверяющий мог использовать time.sleep()

def test_add_to_basket_button_exists(browser):
    browser.get('http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/')
    button = browser.find_elements(By.CLASS_NAME, 'btn-add-to-basket')
    assert len(button) > 0, 'Add to basket button does not exist'