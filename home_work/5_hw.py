from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")

def find_web_elem(css_loc):
    web_Elem = driver.find_element(By.CSS_SELECTOR, css_loc)
    return web_Elem

if find_web_elem('#user-name') and find_web_elem('#password') and find_web_elem('#login-button'):
    print('Элементы найдены')
else:
    print('Элементы не найдены')

