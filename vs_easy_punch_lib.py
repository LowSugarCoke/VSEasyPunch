from selenium import webdriver
import re
import time

class VSEasyPunchLib:
    def __init__(self,driver):
        self.driver = driver;
        return
    
    def login(self,user, password):
        try:
            print("Start to login")
            user_entry = self.driver.find_element_by_xpath('//*[@id="FormLayout_edtUserID_I"]')
            user_entry.send_keys(user)

            password_entry = self.driver.find_element_by_xpath('//*[@id="FormLayout_edtPassword_I"]')
            password_entry.send_keys(password)

            login_button = self.driver.find_element_by_xpath('//*[@id="FormLayout_btnLogin_CD"]')
            login_button.click()
            print("Login successfully")
            return True
        except Exception as e:
            print("Login Failed")
            print(e)
            return False

    def read_punch_time_morning(self):
        try:
            print("Start to search punch time")
            navbar = self.driver.find_element_by_xpath('//*[@id="HeaderPanel_LeftAreaMenu_DXI0_Img"]')
            navbar.click()
   
            staff_area_navbar = self.driver.find_element_by_xpath('//*[@id="LeftPanel_LeftPanelContent_NavBar_GHC1"]')
            staff_area_navbar.click()
        
            staff_punch_search_link = self.driver.find_element_by_xpath('//*[@id="LeftPanel_LeftPanelContent_NavBar_I1i0_T"]')
            staff_punch_search_link.click()

            self.driver.switch_to.frame('PageContent_FrameContent')

            search_button = self.driver.find_element_by_xpath('//*[@id="TB_Load"]')
            search_button.click()

            page_number = re.findall(r'/\d+',self.driver.find_element_by_xpath('//*[@id="TPGrid_WATT0021502_DXPagerBottom"]/b[1]').text)
            page_number = int(page_number[0].strip('/'))

            for i in range(0,page_number):
                content = self.driver.find_element_by_xpath('//*[@id="TPGrid_WATT0021502_DXMainTable"]/tbody')
                ans = re.findall(r'.*刷卡檔轉入 上班',content.text)
                if len(ans)>0:
                    print(ans)
 
                self.driver.find_element_by_xpath('//*[@id="TPGrid_WATT0021502_DXPagerBottom_PBN"]').click() 
                time.sleep(1)

            print("Search punch time successfully")

        except Exception as e:
            print("Read punch time morining failed")
            print(e)
