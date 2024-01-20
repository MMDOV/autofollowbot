from selenium import webdriver
from selenium.webdriver.firefox import service
from selenium.webdriver.firefox import options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException, TimeoutException
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
import time

webdriver_path = r"geckodriver.exe"


class InstaFollower:

    def __init__(self):
        self.modal = None
        self.ser = service.Service(executable_path=webdriver_path)
        self.options = options.Options()
        self.options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
        self.driver = webdriver.Firefox(service=self.ser, options=self.options)
        self.wait = WebDriverWait(self.driver, 20)

    def login(self, user, pas):
        """gets username and password and logs in to the account"""
        self.driver.get(r"https://www.instagram.com/accounts/login/")
        while True:
            try:
                self.wait.until(
                    ec.element_to_be_clickable((By.XPATH, r'/html/body/div[2]/div/div/div[2]/div/div/div/div['
                                                          r'1]/section/main/div/div/div[1]/div[2]/form/div/div['
                                                          r'1]/div/label/input')))
                break
            except TimeoutException:
                continue

        username = self.driver.find_element(By.XPATH, r'/html/body/div[2]/div/div/div[2]/div/div/div/div['
                                                      r'1]/section/main/div/div/div[1]/div[2]/form/div/div['
                                                      r'1]/div/label/input')
        password = self.driver.find_element(By.XPATH, r'/html/body/div[2]/div/div/div[2]/div/div/div/div['
                                                      r'1]/section/main/div/div/div[1]/div[2]/form/div/div['
                                                      r'2]/div/label/input')
        username.send_keys(user)
        password.send_keys(pas)
        password.send_keys(Keys.ENTER)

    def find_followers(self, similar_acc):
        """gets the similar insta page and opens it up then loads the list of its followers"""
        self.driver.get(f'https://www.instagram.com/{similar_acc}/followers')
        while True:
            try:
                self.wait.until(
                    ec.presence_of_element_located(
                        (By.XPATH, r'/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div['
                                   r'2]/div/div/div/div/div[2]/div/div/div[2]')))
                break
            except TimeoutException:
                continue
        self.modal = self.driver.find_element(By.XPATH, r'/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div['
                                                        r'2]/div/div/div/div/div[2]/div/div/div[2]')
        for i in range(10):
            self.modal.send_keys(Keys.END)
            time.sleep(2)
        for i in range(10):
            self.modal.send_keys(Keys.HOME)

    def follow(self):
        """starts following until insta says no!!"""
        follow_buttons = self.modal.find_elements(By.CSS_SELECTOR, r'button')
        for button in follow_buttons:
            try:
                button.click()
            except ElementClickInterceptedException:
                self.driver.find_element(By.XPATH, r'//button[text()="Cancel"]').click()
                button.click()
            finally:
                time.sleep(1)
