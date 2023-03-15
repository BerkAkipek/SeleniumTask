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

# Connect with facebook
driver.find_element(By.XPATH, "//div[contains(@class,'btnLogin')]").click()

sleep(2)

driver.find_element(By.XPATH, "//input[@id='pass']").send_keys("berk.akipek.99@gmail.com")

sleep(5)


