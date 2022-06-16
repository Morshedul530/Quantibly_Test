from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time


# Signup
class Quantibly():
    def test_signup_valid(self):
        base_url = 'https://app.quantibly.com/register/'
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.maximize_window()
        driver.get(base_url)

        # Find Elements
        organization_name = driver.find_element(By.XPATH, '//*[@id="app"]/div/div/div/div/div/div[2]/div/div/form/section/div[1]/div/input')
        email_address = driver.find_element(By.XPATH, '//*[@id="app"]/div/div/div/div/div/div[2]/div/div/form/section/div[2]/div/input')
        get_started = driver.find_element(By.XPATH, '//*[@id="app"]/div/div/div/div/div/div[2]/div/div/form/button/span[1]')

        # Signup Action
        organization_name.clear()
        organization_name.send_keys('iQuantile')
        time.sleep(1)

        email_address.clear()
        email_address.send_keys('shuvo.bandahajir@gmail.com')
        time.sleep(1)

        get_started.click()
        time.sleep(3)

        # Email Verification Code
        verification_code = driver.find_element(By.ID, '1')
        verification_code.clear()
        verification_code.send_keys('5')

        verification_code = driver.find_element(By.ID, '2')
        verification_code.clear()
        verification_code.send_keys('6')

        verification_code = driver.find_element(By.ID, '3')
        verification_code.clear()
        verification_code.send_keys('2')

        verification_code = driver.find_element(By.ID, '4')
        verification_code.clear()
        verification_code.send_keys('5')

        verification_code = driver.find_element(By.ID, '5')
        verification_code.clear()
        verification_code.send_keys('8')

        verification_code = driver.find_element(By.ID, '6')
        verification_code.clear()
        verification_code.send_keys('0')

        # Verify Token
        verify_token = driver.find_element(By.XPATH, '//*[@id="app"]/div/div/div/div/div/div[2]/div/div/form/button')
        verify_token.click()
        time.sleep(2)


test_obj = Quantibly()
test_obj.test_signup_valid()
