from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


class People():
    def test_personal_details(self):
        base_url = 'https://app.quantibly.com/login'
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.maximize_window()
        driver.get(base_url)

        # Find Elements
        email = driver.find_element(By.XPATH,
                                    '//*[@id="app"]/div/div/div/div/div/div[2]/div/div/form/section/div[1]/div/input')
        password = driver.find_element(By.XPATH,
                                       '//*[@id="app"]/div/div/div/div/div/div[2]/div/div/form/section/div[2]/input')
        signin_btn = driver.find_element(By.XPATH,
                                         '//*[@id="app"]/div/div/div/div/div/div[2]/div/div/form/section/button')

        # SignIn Action
        email.clear()
        email.send_keys('mshuvo530@gmail.com')
        time.sleep(1)

        password.clear()
        password.send_keys('Test@123')
        time.sleep(1)

        signin_btn.click()
        time.sleep(2)

        # People Link Click
        '''
        driver.find_element(By.LINK_TEXT, 'People').click()
        time.sleep(2)
        
        people = driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div[1]/div/div/div/div[1]/div[1]/div/div[2]/div[2]')
        people.click()
        time.sleep(2)
        
        lets_go = driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div[1]/div/div/div/div[2]/button/span')
        lets_go.click()
        time.sleep(2)
        '''

        base_url = 'https://app.quantibly.com/people/personnel-details'
        driver.get(base_url)
        time.sleep(2)

        # Click Add New Personnel
        add_new_personnel = driver.find_element(By.XPATH,
                                                '//*[@id="app"]/div/div[3]/div[1]/div[3]/div/div/div[1]/div[2]/a')
        add_new_personnel.click()
        time.sleep(2)

        cancel = driver.find_element(By.XPATH, '//*[@id="smartwizard"]/div[2]/a')
        cancel.click()
        time.sleep(2)

        add_new_personnel = driver.find_element(By.XPATH,
                                                '//*[@id="app"]/div/div[3]/div[1]/div[3]/div/div/div[1]/div[2]/a/span/i')
        add_new_personnel.click()
        time.sleep(3)

        '''
        prefix = driver.find_element(By.XPATH, '//*[@id="step-1"]/div[2]/div/div/div[1]/div/div')
        sel = Select(prefix)
        sel.select_by_visible_text('Mr')
        time.sleep(2)
        '''

        first_name = driver.find_element(By.XPATH, '//*[@id="step-1"]/div[2]/div/div/div[2]/div/div/input')
        first_name.clear()
        first_name.send_keys('Md:')
        time.sleep(1)

        middle_name = driver.find_element(By.XPATH, '//*[@id="step-1"]/div[2]/div/div/div[3]/div/div/input')
        middle_name.clear()
        middle_name.send_keys('Morshedul')
        time.sleep(1)

        last_name = driver.find_element(By.XPATH, '//*[@id="step-1"]/div[2]/div/div/div[4]/div/div/input')
        last_name.clear()
        last_name.send_keys('Islam')
        time.sleep(1)

        '''
        gender = driver.find_element(By.XPATH, '//*[@id="step-1"]/div[2]/div/div/div[5]/div/div')
        sel = Select(gender)
        sel.select_by_visible_text('Male')
        #sel.select_by_index(1)
        # sel.select_by_value('1')
        time.sleep(2)
        '''

        date_of_birth = driver.find_element(By.XPATH, '//*[@id="step-1"]/div[2]/div/div/div[6]/div/div/input')
        date_of_birth.clear()
        date_of_birth.send_keys('1996-01-01')
        time.sleep(1)

        language = driver.find_element(By.XPATH, '//*[@id="step-1"]/div[2]/div/div/div[7]/div/div/input')
        language.clear()
        language.send_keys('English')
        time.sleep(1)

        designation = driver.find_element(By.XPATH, '//*[@id="step-1"]/div[2]/div/div/div[8]/div/div/input')
        designation.clear()
        designation.send_keys('SQA Engineer')
        time.sleep(1)

        '''
        educational_background = driver.find_element(By.XPATH, '//*[@id="step-1"]/div[2]/div/div/div[9]/div/div/div[1]/div')
        sel = Select(educational_background)
        sel.select_by_visible_text('Bachelors Degree')
        time.sleep(1)
        '''

        date_of_employement = driver.find_element(By.XPATH, '//*[@id="step-1"]/div[2]/div/div/div[10]/div/div/input')
        date_of_employement.clear()
        date_of_employement.send_keys('2021-06-16')
        time.sleep(1)

        next = driver.find_element(By.XPATH, '//*[@id="smartwizard"]/div[2]/button')
        next.click()
        time.sleep(2)

        next = driver.find_element(By.XPATH, '//*[@id="smartwizard"]/div[2]/button[2]')
        next.click()
        time.sleep(2)

        next = driver.find_element(By.XPATH, '//*[@id="smartwizard"]/div[2]/button[2]/span')
        next.click()
        time.sleep(2)

        confirm = driver.find_element(By.XPATH, '//*[@id="smartwizard"]/div[2]/button[2]')
        confirm.click()
        time.sleep(3)

        delete = driver.find_element(By.XPATH, '//*[@id="myTable"]/tbody/tr/td[1]/a[3]/i')
        delete.click()
        time.sleep(3)


test_obj = People()
test_obj.test_personal_details()
