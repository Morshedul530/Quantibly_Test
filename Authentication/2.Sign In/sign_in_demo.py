from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time


# Sign In
class Quantibly():
    def test_signin_valid(self):
        base_url = 'https://app.quantibly.com/login'
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.maximize_window()
        driver.get(base_url)

        # Find Elements
        email = driver.find_element(By.XPATH, '//*[@id="app"]/div/div/div/div/div/div[2]/div/div/form/section/div[1]/div/input')
        password = driver.find_element(By.XPATH, '//*[@id="app"]/div/div/div/div/div/div[2]/div/div/form/section/div[2]/input')
        signin_btn = driver.find_element(By.XPATH, '//*[@id="app"]/div/div/div/div/div/div[2]/div/div/form/section/button')

        # SignIn Action
        email.clear()
        email.send_keys('mshuvo530@gmail.com')
        time.sleep(1)

        password.clear()
        password.send_keys('Test@123')
        time.sleep(1)

        signin_btn.click()
        time.sleep(5)

        driver.close()


test_obj = Quantibly()
test_obj.test_signin_valid()
