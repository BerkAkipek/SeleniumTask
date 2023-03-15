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

# Find Refresh password
driver.find_element(By.ID, 'forgotPassword').click()

sleep(1)

driver.find_element(By.XPATH, "//input[@id='forgottenUserEmail']").send_keys("sdfasdfadfG")
driver.find_element(By.ID, "sendLinkForPasswordBtn").click()

sleep(1)

message = driver.find_element(By.XPATH, "//div[contains(text(),'Lütfen geçerli bir e-posta adresi girin.')]").text

assert "Lütfen geçerli bir e-posta adresi girin." in message

sleep(1)