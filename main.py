from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import unittest

class Desafio1(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.implicitly_wait(3)
        self.driver.get("https://shopcart-challenge.4all.com/")
        self.driver.maximize_window()

    def teste(self):
        time.sleep(1)
        self.driver.find_element_by_css_selector('img.sc-iAyFgw.mBXxg').click()
        time.sleep(1)        
        self.driver.find_element_by_id('category-1').click()
        time.sleep(1)
        self.driver.find_element_by_id('add-product-4-btn').click()
        time.sleep(1)        
        self.driver.find_element_by_id('add-product-5-btn').click()
        time.sleep(1)
        self.driver.find_element_by_class_name('sc-kGXeez.brMovy').click()
        time.sleep(1)
        for i in range(4):
            self.driver.find_element_by_id('add-product-4-qtd').click()
            time.sleep(1)
        self.driver.find_element_by_id('finish-checkout-button').click()
        time.sleep(1)
        self.driver.find_element_by_class_name('close-modal.sc-jqCOkK.ippulb').click()
        time.sleep(1)



    def tearDown(self):
        self.driver.close


if __name__ == '__main__':
    unittest.main()