import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

from simon.accounts.pages import LoginPage

import time

from datetime import datetime

def getOTPCode():
    # Creating the driver (browser)
    #PATH = r"C:\Users\chiay\Downloads\Compressed\chromedriver_win32_2/chromedriver.exe"
    # driver = webdriver.Chrome(executable_path="C:/Users/Wei Cong/Downloads/chromedriver_win32/chromedriver.exe")
    # driver.maximize_window()

    # # Login
    # #       and uncheck the remember check box
    # #       (Get your phone ready to read the QR code)
    # login_page = LoginPage(driver)
    # login_page.load()
    # time.sleep(7)
    options = Options()
    options.add_argument("--user-data-dir=chrome-data")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    driver = webdriver.Chrome(executable_path="C:/Users/Wei Cong/Downloads/chromedriver_win32/chromedriver.exe",options=options)
    driver.maximize_window()
    driver.get('https://web.whatsapp.com')  # Already authenticated

    time.sleep(20)

    ##################### Provide Recepient Name Here ###############################
    driver.find_element_by_xpath("//span[@title='"+"Take attendance lo😂😂"+"']").click()

    last_message = driver.find_element_by_xpath("(//div[@tabindex='-1'])").text

    str = last_message
    arr=str.splitlines()
    driver.quit()
    #print(arr[len(arr)-3])

    return arr[len(arr)-3]

def driver(username,password,otpCode):

    driver = webdriver.Chrome(executable_path="C:/Users/Wei Cong/Downloads/chromedriver_win32/chromedriver.exe")
    
    driver.get("https://apspace.apu.edu.my/tabs/dashboard")
           
    driver.implicitly_wait(5)
    login_show = driver.find_element_by_xpath("/html/body/app-root/ion-app/ion-router-outlet/app-login/ion-content/div/section[2]/div/ion-grid/ion-row[1]/ion-col[2]/ion-button")

    login_show.click()
    
    driver.implicitly_wait(5)
    
    AP_KEY = driver.find_element_by_xpath("/html/body/app-root/ion-app/ion-router-outlet/app-login/ion-content/div/section[2]/div/ion-grid/ion-row[2]/ion-col[1]/form/div/div[1]/ion-input/input")
    PASSWORD = driver.find_element_by_xpath("/html/body/app-root/ion-app/ion-router-outlet/app-login/ion-content/div/section[2]/div/ion-grid/ion-row[2]/ion-col[1]/form/div/div[2]/ion-input/input")
    
    AP_KEY.send_keys(username)
    PASSWORD.send_keys(password)
    
    login_button = driver.find_element_by_xpath("/html/body/app-root/ion-app/ion-router-outlet/app-login/ion-content/div/section[2]/div/ion-grid/ion-row[2]/ion-col[1]/form/div/div[3]/ion-button")
    
    login_button.click()

    #driver.implicitly_wait(5)
    driver.implicitly_wait(10)
        
    ##### read username , tp , course
    
    name = driver.find_element_by_xpath("/html/body/app-root/ion-app/ion-router-outlet/app-tabs/ion-content/ion-tabs/div[1]/ion-router-outlet/app-dashboard/ion-content/div/ion-grid/ion-row/ion-col[1]/ion-card[2]/ion-card-header/ion-card-title")
    tp_number = driver.find_element_by_xpath("/html/body/app-root/ion-app/ion-router-outlet/app-tabs/ion-content/ion-tabs/div[1]/ion-router-outlet/app-dashboard/ion-content/div/ion-grid/ion-row/ion-col[1]/ion-card[2]/ion-card-header/ion-card-subtitle")
    
    #driver.get("https://apspace.apu.edu.my/attendix/update")
    #attendance_page = driver.find_element_by_xpath("/html/body/app-root/ion-app/ion-router-outlet/app-tabs/ion-content/ion-tabs/div[1]/ion-router-outlet/app-dashboard/ion-content/div/ion-grid/ion-row/ion-col[1]/ion-card[3]/ion-card-content/ion-grid/ion-row/ion-col[1]/ion-button")
    attendance_page = driver.find_element_by_xpath("(//ion-button[@class='md button button-block button-solid ion-activatable ion-focusable hydrated'][@tabindex='0'])")
    
    attendance_page.click()
    driver.implicitly_wait(5)
    otp = driver.find_element_by_xpath("/html/body/app-root/ion-app/ion-router-outlet/app-student/ion-content/ion-grid/ion-row/ion-col/div/input[1]")
    otp.send_keys(otpCode)
    
    driver.implicitly_wait(10)
    
    ##### alert message
    
    #message = driver.find_element_by_id("alert-1-msg").text
    message = driver.find_element_by_xpath("(//div[@id='alert-1-msg'][@class='alert-message sc-ion-alert-md'])").text
    ### Show Time & Date
    now = datetime.now()
    current_time = now.strftime("%Y-%m-%d %H:%M:%S")
    

    string="Time =>" + current_time +" || " +"Name =>"+ name.text +" || " +"Message =>" + message +"\n"
    driver.quit()
    return string
    # print("Time :", current_time)
    # print("Name :", name.text)
    # print("Username :", username)
    # print("Message :", message)
    
    #driver.quit()


def sendValidationToWhatsApp(returnMsg):
    options = Options()
    options.add_argument("--user-data-dir=chrome-data")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    driver = webdriver.Chrome(executable_path="C:/Users/Wei Cong/Downloads/chromedriver_win32/chromedriver.exe",options=options)
    driver.maximize_window()
    driver.get('https://web.whatsapp.com')  # Already authenticated

    time.sleep(20)

    ##################### Provide Recepient Name Here ###############################
    driver.find_element_by_xpath("//span[@title='"+"Naga-Bot"+"']").click()

#determine input space to write message
    writing_space = driver.find_element_by_xpath("(//div[@class='_2_1wd copyable-text selectable-text'])").find_element_by_xpath("(//div[@data-tab='6'])")
    writing_space.send_keys(returnMsg)

    #click enter to send
    writing_space.send_keys(u'\ue007')
    time.sleep(10)

#Put ur ID and Password here
students= [["TP00000","TP00000"],["TP000000","Nagalsxxxxx?"],["TP011111","rwrwrrwr"]]
returnMsg=''


otpCode= getOTPCode()

if len(otpCode)==3:
    for x in students:
        returnMsg+=driver(x[0],x[1],otpCode)
else:
    print("invalid otp code")

sendValidationToWhatsApp(returnMsg)

