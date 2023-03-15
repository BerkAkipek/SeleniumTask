from selenium.webdriver.common.by import By


class LoginPage():


    def __init__(self, driver) -> None:
        self.driver = driver
        self.mail_input_xpath = "//input[@id='email']"
        self.password_input_xpath = "//input[@id='password']"
        self.login_button_xpath = "//div[@id='loginButton']"
        self.more_then_15_characters_error_xpath = "//div[contains(text(),'Girilen değer en fazla 15 karakter olmalıdır.')]"
        self.please_enter_valid_mail_xpath = "//div[contains(text(),'Lütfen geçerli bir e-posta adresi girin.')]"
        self.empty_mail_error_xpath = "//div[contains(text(),'Lütfen e-posta adresinizi girin.')]"
        self.empty_password_error_xpath = "//div[contains(text(),'Bu alanın doldurulması zorunludur.')]"
        self.refresh_password_id = 'forgotPassword'
        self.forgot_password_mail_xpath = "//input[@id='forgottenUserEmail']"
        self.send_link_for_password = "//a[@id='sendLinkForPasswordBtn']"
        self.refresh_password_error_xpath

    
    def enter_email(self, email):
        self.driver.find_element(By.XPATH, self.mail_input_xpath).clear()
        self.driver.find_element(By.XPATH, self.mail_input_xpath).send_keys(email)
    

    def enter_password(self, password):
        self.driver.find_element(By.XPATH, self.password_input_xpath).clear()
        self.driver.find_element(By.XPATH, self.password_input_xpath).send_keys(password)
    

    def enter_mail_forgotten_password(self, email):
        self.driver.find_element(By.XPATH, self.forgot_password_mail_xpath).send_keys(email)


    def click_login(self):
        self.driver.find_element(By.XPATH, self.login_button_xpath).click()

    
    def click_refresh_password(self):
        self.driver.find_element(By.ID, self.refresh_password_id).click()
    

    def click_send_link_forgotten_password(self):
        self.driver.find_element(By.XPATH, self.send_link_for_password).click()
    

    def return_invalid_password_text(self):
        message = self.driver.find_element(By.XPATH, self.more_then_15_characters_error_xpath).text
        return message
    

    def return_invalid_mail_text(self):
        message = self.driver.find_element(By.XPATH, self.please_enter_valid_mail_xpath).text
        return message
    

    def return_empty_mail_error_text(self):
        message = self.driver.find_element(By.XPATH, self.empty_mail_error_xpath).text
        return message
    

    def return_empty_password_error_text(self):
        message = self.driver.find_element(By.XPATH, self.empty_password_error_xpath).text
        return message
    
    
