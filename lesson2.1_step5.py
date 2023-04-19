from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get('https://suninjuly.github.io/math.html')
    x = browser.find_element(By.ID, 'input_value').text
    
    browser.find_element(By.ID, 'answer').send_keys(calc(x))
    browser.find_element(By.CSS_SELECTOR, '[for="robotCheckbox"]').click()
    browser.find_element(By.CSS_SELECTOR, '[for="robotsRule"]').click()
    browser.find_element(By.TAG_NAME, 'button').click()

finally:
   time.sleep(10)
   browser.quit()