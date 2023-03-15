from selenium.webdriver.common.by import By


class HomePage():

    def __init__(self, driver) -> None:
        self.driver = driver
        self.login_link_link_text = "Giriş Yap"


    def click_login(self):
        self.driver.find_element(By.LINK_TEXT, self.login_link_link_text).click()
    

    
