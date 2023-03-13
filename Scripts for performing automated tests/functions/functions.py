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
        
    def cadastralSearch(self, cadastralReference):
        WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.ID, "busquedaPorCodigo"))).click()
        WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.ID, "referencia"))).click()
        WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.ID, "referencia"))).send_keys(cadastralReference)
        WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.ID, "iniciarBusquedaReferencia"))).click()        
        self.driver.find_elements(By.XPATH, "//*[@class='close']")[1].click()
        time.sleep(60)

    def coordinateSearch(self, coord1, coord2):
        WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.ID, "busquedaPorCoordenadas"))).click()
        WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.ID, "coordLon"))).click() 
        WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.ID, "coordLon"))).send_keys(coord1)
        WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.ID, "coordLat"))).click() 
        WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.ID, "coordLat"))).send_keys(coord2)
        WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.ID, "comboLon"))).click() 
        dropdown = WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.ID, "comboLon")))
        dropdown.find_element(By.XPATH, "//option[. = 'OES']").click()
        WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.ID, "comboLat"))).click() 
        dropdown = WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.ID, "comboLat")))
        WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.ID, "comboLat"))).click() 
        dropdown.find_element(By.XPATH, "//option[. = 'NOR']").click()
        WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.ID, "iniciarBusquedaCoordenadas"))).click() 
        self.driver.find_elements(By.XPATH, "//*[@class='close']")[2].click()
        time.sleep(60)

    def fileSearch(self, file): 
        self.driver.find_element(By.ID, "busquedaPorFichero").click()
        file_upload = WebDriverWait(self.driver, 60).until(
            EC.presence_of_element_located((By.ID, "geoFileUpload"))
        )
        #BTT0101_vivar_del_cid-burgos.gpx
        file_upload.send_keys('C:\\Users\\djherrera.externo\\Downloads\\'+str(file))
        self.driver.find_element(By.ID, "iniciarBusquedaFichero").click()
        self.driver.find_elements(By.XPATH, "//*[@class='close']")[0].click()
        time.sleep(60)
        
    def pointSearch(self): 
        self.driver.find_element(By.ID, "busquedaPorPunto").click()
        wait = WebDriverWait(self.driver, 60)
        main_canvas = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[name()='canvas']")))
        size = main_canvas.size
        w, h = size['width'], size['height']
        new_w = w*0.64
        new_h = h*0.53
        ActionChains(self.driver).move_by_offset(new_h, new_h).pause(1).perform().click()
        time.sleep(60)
        
    def geometrySearch(self): 
        self.driver.find_element(By.ID, "busquedaPorGeometria").click()
        wait = WebDriverWait(self.driver, 60)
        main_canvas = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[name()='canvas']")))
        size = main_canvas.size
        w, h = size['width'], size['height']
        new_w = w*0.64
        new_h = h*0.53
        ActionChains(self.driver).move_by_offset(new_h, new_h).pause(1).perform()
        wait.until(EC.element_to_be_clickable((By.XPATH, "//*[name()='canvas']"))).click()
        ActionChains(self.driver).move_by_offset(10,0).pause(1).perform()
        wait.until(EC.element_to_be_clickable((By.XPATH, "//*[name()='canvas']"))).click()
        ActionChains(self.driver).move_by_offset(0,10).pause(1).perform()
        wait.until(EC.element_to_be_clickable((By.XPATH, "//*[name()='canvas']"))).click()
        ActionChains(self.driver).move_by_offset(-10,0).pause(1).perform()
        wait.until(EC.element_to_be_clickable((By.XPATH, "//*[name()='canvas']"))).click()
        ActionChains(self.driver).move_by_offset(0,-10).pause(1).perform()
        wait.until(EC.element_to_be_clickable((By.XPATH, "//*[name()='canvas']"))).click()
        time.sleep(60)
        
    def results(self): 
        element=WebDriverWait(self.driver,60).until(EC.element_to_be_clickable((By.CLASS_NAME, "numResultados")))
        assert int(''.join(filter(str.isdigit, element.text))) > 0, element.text+" Not results found"

    def view(self): 
        WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, "//*[@class='header-card']"))).click()
        time.sleep(10)  
        
    def checkmetadatarecord(self):
        assert EC.number_of_windows_to_be(2), "Metadata record was not open"

    def display(self): 
        WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.CLASS_NAME, "numResultados"))).click()
        time.sleep(60)
        
    def faceted_filter(self): 
        WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, "//*[@class='faceta']"))).click()
        time.sleep(60)
        
    def buy_catalogue(self): 
        WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, "//*[@class='link-ico-count  to-buy']"))).click()
        time.sleep(60)   

    def locate_catalogue(self): 
        WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, "//*[@class='icono link-ico marker']"))).click()
        time.sleep(60)

    def view(self): 
        WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, "//*[@class='header-card']"))).click()
        time.sleep(60)
        
    def filter_products(self): 
        WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.CLASS_NAME, "productos"))).click()
        time.sleep(60)
 
    def buy_product(self): 
        WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, "//*[@class='comprabtn']"))).click()
        time.sleep(60)

    def view_product(self): 
        WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, "//*[@class='nombre']"))).click()
        time.sleep(60)

    def filter_downloads(self): 
        WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.CLASS_NAME, "descargables"))).click()
        time.sleep(60)
        
    def locate_download(self): 
        WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, "//*[@class='link-ico marker']"))).click()
        time.sleep(60)

    def download_catalogue(self): 
        WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, "//*[@class='link-ico-count  download']"))).click()
        time.sleep(60)
    
    def download_resource(self):
        WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, "//*[@class='link-ico download']"))).click()
        time.sleep(60)  
        
    def buy_resource(self): 
        WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, "//*[@class='comprabtn']"))).click()
        time.sleep(60)
        
    def free_class(self,free_class): 
        WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, "//*[@class='"+free_class+"+']"))).click()
    
    def locate(self): 
        WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, "//*[@class='icono link-ico marker']"))).click()
        time.sleep(60)
        
    def check_download(self): 
        element=WebDriverWait(self.driver,60).until(EC.element_to_be_clickable((By.CLASS_NAME, "numDescargas")))
        assert int(filter(str.isdigit, element.text)) > 0, element.text+" Not downloads found"
        
    def check_cart(self): 
        element=WebDriverWait(self.driver,60).until(EC.element_to_be_clickable((By.CLASS_NAME, "numCarrito")))
        assert int(filter(str.isdigit, element.text)) > 0, element.text+" Not products found"
        
    def check_geometry_displayed(self): 
        element=WebDriverWait(self.driver,60).until(EC.element_to_be_clickable((By.CLASS_NAME, "numGeometrias")))
        assert int(filter(str.isdigit, element.text)) > 0, element.text+" Not geometries found"
