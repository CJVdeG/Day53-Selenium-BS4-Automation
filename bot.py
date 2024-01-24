from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class FormFiller:

    def __init__(self):
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option('detach', True)
        self.driver = webdriver.Chrome(options=self.chrome_options)
        self.driver.maximize_window()

    def open_form(self, link):
        self.driver.get(link)

    def enter_form(self, link, price, address):
        # Enter address
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(
            (By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
        )).send_keys(address)

        # Enter price
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(
            (By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
        )).send_keys(price)

        # Enter link
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(
            (By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
        )).send_keys(link)

        # Submit form
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(
            (By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
        )).click()

    def open_new_form(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(
            (By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
        )).click()
