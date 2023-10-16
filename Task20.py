from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from time import sleep


class Acess_cowin:

    def __init__(self,url):
        self.url = url
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        self.original_handle = []
        self.handles =[]

# Access the Cowin or given url 

    def breach_url(self):
        try:
            self.driver.maximize_window()
            self.driver.get(self.url)
            sleep(5)
        except Exception as error:
            print("Error on: ",error)

# Access the required the elements window id for the opened tabs

    def get_req_data(self):
        try:
            self.breach_url()
            self.driver.find_element(by=By.LINK_TEXT, value="FAQ").click()
            sleep(10)
            self.original_handle = self.driver.current_window_handle
            self.handles = self.driver.window_handles
            faq_handle = self.handles[1]  
            print("Window ID For FAQ:", faq_handle)
            self.driver.find_element(by=By.XPATH, value='//*[@id="navbar"]/div[4]/div/div[1]/div/nav/div[3]/div/ul/li[5]/a').click()
            sleep(10)
            self.handles = self.driver.window_handles
            partner_handle = self.handles[1] 
            print("Window ID For partners:", partner_handle)
        except Exception as error:
            print("error on: ",error)



#  Close the opened tabs as per the requirements 

    def close_tabs(self):
        try:
            for handle in self.handles:
                if handle != self.original_handle:
                    self.driver.switch_to.window(handle)
                    self.driver.close()
                    sleep(5)
        except Exception as close_error:
            print("close_error:",close_error)

        finally:
            self.driver.quit()


url = "https://www.cowin.gov.in/"
as_wp = Acess_cowin(url)
as_wp.get_req_data()
as_wp.close_tabs()
        

