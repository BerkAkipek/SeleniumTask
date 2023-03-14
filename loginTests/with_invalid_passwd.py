#!/usr/bin/python3

# Selenium Task

from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


service_obj = Service("/home/berk/chromedriver/stable/chromedriver")
driver = webdriver.Chrome(service=service_obj)

# Go to the www.n11.com
driver.maximize_window()
driver.get("https://www.n11.com/")

# Go to hyperlink GirişYap
driver.find_element(By.LINK_TEXT, "Giriş Yap").click()

sleep(1)

# Try to login with an invalid password
driver.find_element(By.CSS_SELECTOR, "#email").send_keys("berk.akipek.96@gmail.com")
driver.find_element(By.CSS_SELECTOR, "#password").send_keys("ABS11431811asdfghjkl")
driver.find_element(By.CSS_SELECTOR, "#loginButton").click()
message03 = driver.find_element(By.XPATH, "//div[contains(text(),'Girilen değer en fazla 15 karakter olmalıdır.')]").text

assert "Girilen değer en fazla 15 karakter olmalıdır." in message03

# End Test
