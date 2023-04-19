from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

try:
    browser = webdriver.Chrome()
    browser.get('https://suninjuly.github.io/selects1.html')
    summ = int(browser.find_element(By.ID, 'num1').text) + int(browser.find_element(By.ID, 'num2').text)

    select = Select(browser.find_element(By.ID, 'dropdown'))
    select.select_by_value(str(summ))
    browser.find_element(By.TAG_NAME, 'button').click()

finally:
    time.sleep(10)
    browser.quit()
