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

# Try to login without a password
driver.find_element(By.CSS_SELECTOR, "#email").send_keys("example@example.com")
driver.find_element(By.CSS_SELECTOR, "#loginButton").click()
message02 = driver.find_element(By.XPATH, "//div[contains(text(),'Bu alanın doldurulması zorunludur.')]").text

assert "Bu alanın doldurulması zorunludur." in message02

# End Test
