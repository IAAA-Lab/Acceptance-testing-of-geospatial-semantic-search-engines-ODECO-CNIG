import time
import json
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
chrome_options = Options()

link = "http://devige.ign.es/comunidad/ign-semantico/buscador"

class myFunctions():
    
    @classmethod
    def setup_class(self):
        print("\nstart browser for test suite..")
        self.driver = webdriver.Chrome(options=chrome_options)

    @classmethod
    def teardown_class(self):
        print("quit browser for test suite..")
        self.driver.quit()
    
    def enterSemanticWeb(self):
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.get(link)
        self.driver.set_window_size(1616, 1176)
        time.sleep(5) 

    def textualSearch(self, text):
        WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.ID,"autocomplete"))).click()
        WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.ID,"autocomplete"))).send_keys(text)
        WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.ID,"autocomplete"))).send_keys(Keys.ENTER)
        time.sleep(20) 

    def results(self): 
        element=WebDriverWait(self.driver,60).until(EC.element_to_be_clickable((By.CLASS_NAME, "numResultados")))
        assert int(''.join(filter(str.isdigit, element.text))) > 0, element.text+" Not results found"

    def view(self): 
        WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, "//*[@class='header-card']"))).click()
        time.sleep(10)  
        
    def checkmetadatarecord(self):
        assert EC.number_of_windows_to_be(2), "Metadata record was not open"
