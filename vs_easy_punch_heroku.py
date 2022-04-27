import os
from selenium import webdriver
from vs_easy_punch_lib import VSEasyPunchLib


if __name__ == '__main__':   
    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    chrome_options.add_argument("--headless") 
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)
    driver.implicitly_wait(30) 
    driver.get("https://scsrwd.azurewebsites.net/Login.aspx?ParentUniqueGUID=718a7779-0c98-4a22-a619-1618319fb87c&CompanyID=W10C89A7A9D57A845C978EVI&Logout=true")
    website_controller = VSEasyPunchLib(driver)
    if website_controller.login("U0803","123456789")==False:
        quit()
    website_controller.read_punch_time_morning()


    
  