# Создайте файл 5_hw.py в нем выполняйте все задания
# 1. Создайте функцию которая
# a. переходит на страницу https://www.saucedemo.com/
# b. находит элементы:
# i. текстовое поле username
# ii. текстовое поле password
# iii. кнопку submit
# c. Создайте условие, если элементы найдены - вывести в консоль текст “Элементы найдены”

from selenium import webdriver
from selenium.webdriver.common.by import By

def find_web_elem():
    locators = ['#user-name', '#password', '#login-button'] # список локаторов

    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/") #переход на страницу https://www.saucedemo.com/

    text_field_1 = driver.find_element(By.CSS_SELECTOR, locators[0]) # поиск текстового поля username
    text_field_2 = driver.find_element(By.CSS_SELECTOR, locators[1]) # поиск текстового поля password
    button = driver.find_element(By.CSS_SELECTOR, locators[2]) # поиск кнопки submit
    # Условие, если элементы найдены - вывести в консоль текст “Элементы найдены”
    if (text_field_1 is None) and (text_field_2 is None) and (button is None):
        print('Элементы не найдены')
    else:
        print('Элементы найдены')

find_web_elem()