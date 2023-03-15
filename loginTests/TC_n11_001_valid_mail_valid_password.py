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

# Test with valid mail invalid password
driver.find_element(By.XPATH, "//input[@id='email']").send_keys("berk.akipek.99@gmail.com")
driver.find_element(By.XPATH, "//input[@id='password']").send_keys("ABS2254292asd")
driver.find_element(By.XPATH, "//div[@id='loginButton']").click()

sleep(2)

if driver.current_url != "https://www.n11.com/":
    print("Login Failed\n")

sleep(1)