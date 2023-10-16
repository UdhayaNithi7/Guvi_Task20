from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.firefox.options import Options
from time import sleep
import os

class Labour:
    def __init__(self, url):
        self.url = url
        self.download_folder = "E:\\Automation Testing\\pdf-img-folder"
        self.set_firefox_options()
        self.driver = webdriver.Firefox(options=self.options, service=Service(GeckoDriverManager().install()))

    def set_firefox_options(self):
        self.options = Options()
        self.options.set_preference("browser.download.folderList", 2)
        self.options.set_preference("browser.download.manager.showWhenStarting", False)
        self.options.set_preference("browser.download.dir", self.download_folder)
        self.options.set_preference("browser.download.useDownloadDir", True)
        self.options.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/pdf")
        self.options.set_preference("pdfjs.disabled",True)

# Access the given webpage 

    def get_webpage(self):
        try:
            self.driver.maximize_window()
            self.driver.get(self.url)
            sleep(5)
        except Exception as error:
            print("Error on: ", error)

    def create_folder(self):
        os.makedirs(self.download_folder, exist_ok=True)

# Access and get the monthly Report from the webpage 

    def month_repo(self):
        try:
            docu = self.driver.find_element(By.XPATH, '//*[@id="nav"]/li[7]')
            ActionChains(self.driver).move_to_element(docu).perform()
            sleep(5)
            self.driver.find_element(by=By.XPATH, value='/html/body/nav/div/div/div/ul/li[7]/ul/li[2]/a').click()
            sleep(5)
            self.driver.find_element(by=By.XPATH, value='/html/body/section[3]/div/div/div[3]/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[2]/div[2]/table/tbody/tr[2]/td[2]/a').click()
            alert = self.driver.switch_to.alert
            alert.accept()
            sleep(5)
        except Exception as error:
            print("Report error on: ",error)

# Access & download the images from photo gallery 

    def download_images(self):
        try:
            self.get_to_swachhata_hi()

            # Find image elements with alt attribute "Swachhata Hi Seva"
            image_elements = self.driver.find_elements(By.XPATH, '//img[@alt="Swachhata Hi Seva"]')

            for img_element in image_elements[:10]:  # Download the first 10 images
                img_url = img_element.get_attribute('src')
                if img_url:
                    img_name = f"image_{image_elements.index(img_element)}.jpg"
                    img_path = os.path.join(self.download_folder, img_name)
                    with open(img_path, 'wb') as img_file:
                        img_file.write(img_element.screenshot_as_png)
            print("Images succesfully downloaded as of requirements")
        except Exception as error:
            print("getting img error on: ",error)
        finally:
            self.driver.quit()

# Get into the media & photo gallery 

    def get_to_swachhata_hi(self):
        try:
            media = self.driver.find_element(By.XPATH, '//*[@id="nav"]/li[10]')
            media.click()
            sleep(2)
            self.driver.find_element(By.XPATH, '//*[@id="fontSize"]/div/div/div[3]/div[2]/div[1]/div/div/div[2]/div[2]/table/tbody/tr[1]/td[1]/div[2]/span/a').click()
        except Exception as error:
            print("gallery error on: ",error)    
   

url = "https://labour.gov.in/"
la_wp = Labour(url)
la_wp.create_folder()
la_wp.get_webpage()
la_wp.month_repo()
la_wp.download_images()
