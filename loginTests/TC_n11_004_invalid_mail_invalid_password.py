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

# Test vith invalid mail and password
driver.find_element(By.CSS_SELECTOR, "#email").send_keys("asdfashsfgdfgh")
driver.find_element(By.CSS_SELECTOR, "#password").send_keys("134679Hello")
message = driver.find_element(By.XPATH, "//div[contains(text(),'Lütfen geçerli bir e-posta adresi girin.')]").text

assert "Lütfen geçerli bir e-posta adresi girin" in message
