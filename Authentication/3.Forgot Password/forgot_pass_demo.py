from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time


class Quantibly():
    def test_signin_valid(self):
        base_url = 'https://app.quantibly.com/login'
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.maximize_window()
        driver.get(base_url)

        # Click Forgot Password
        forgot_password = driver.find_element(By.XPATH, '//*[@id="app"]/div/div/div/div/div/div[2]/div/div/form/section/div[3]/a')
        forgot_password.click()
        time.sleep(2)

        # Forgot Password
        email_address = driver.find_element(By.XPATH, '//*[@id="app"]/div/div/div/div/div/div[2]/div/div/div[2]/div/input')
        email_address.clear()
        email_address.send_keys('mshuvo530@gmail.com')
        time.sleep(2)

        reset_password = driver.find_element(By.XPATH, '//*[@id="app"]/div/div/div/div/div/div[2]/div/div/button/span[1]')
        reset_password.click()
        time.sleep(5)

        driver.close()


test_obj = Quantibly()
test_obj.test_signin_valid()
