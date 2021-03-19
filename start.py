import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from simon.accounts.pages import LoginPage

import time

from datetime import datetime

#PATH = r"C:\Users\chiay\Downloads\Compressed\chromedriver_win32_2/chromedriver.exe"

username_1 = "TP050735"
password_1 = "TP050735"
username_2 = "TP051139"
password_2 = "Nagalsw030300?"


	

# Creating the driver (browser)
#PATH = r"C:\Users\chiay\Downloads\Compressed\chromedriver_win32_2/chromedriver.exe"
driver = webdriver.Chrome(executable_path="/usr/lib/chromium-browser/chromedriver")
driver.maximize_window()

# Login
#       and uncheck the remember check box
#       (Get your phone ready to read the QR code)
login_page = LoginPage(driver)
login_page.load()
time.sleep(7)


selected_group = driver.find_element_by_xpath("//span[@title='"+"Take attendance lo😂😂"+"']")
selected_group.click()

last_message = driver.find_element_by_xpath("(//div[@tabindex='-1'])").text

str = last_message
arr=str.splitlines()
#print(arr[len(arr)-3])

validate_otp = len(arr[len(arr)-3]) == 3

#get the latest 3 int
#code = print(arr[len(arr)-3] )



def driver1():

    driver = webdriver.Chrome(executable_path="/usr/lib/chromium-browser/chromedriver")
    
    driver.get("https://apspace.apu.edu.my/tabs/dashboard")
           
    driver.implicitly_wait(5)
    login_show = driver.find_element_by_xpath("/html/body/app-root/ion-app/ion-router-outlet/app-login/ion-content/div/section[2]/div/ion-grid/ion-row[1]/ion-col[2]/ion-button")

    login_show.click()
    
    driver.implicitly_wait(5)
    
    AP_KEY = driver.find_element_by_xpath("/html/body/app-root/ion-app/ion-router-outlet/app-login/ion-content/div/section[2]/div/ion-grid/ion-row[2]/ion-col[1]/form/div/div[1]/ion-input/input")
    PASSWORD = driver.find_element_by_xpath("/html/body/app-root/ion-app/ion-router-outlet/app-login/ion-content/div/section[2]/div/ion-grid/ion-row[2]/ion-col[1]/form/div/div[2]/ion-input/input")
    
    AP_KEY.send_keys(username_1)
    PASSWORD.send_keys(password_1)
    
    login_button = driver.find_element_by_xpath("/html/body/app-root/ion-app/ion-router-outlet/app-login/ion-content/div/section[2]/div/ion-grid/ion-row[2]/ion-col[1]/form/div/div[3]/ion-button")
    
    login_button.click()
    
    
    #driver.implicitly_wait(5)
    driver.implicitly_wait(10)
    
    
    ##### read username , tp , course
    
    name = driver.find_element_by_xpath("/html/body/app-root/ion-app/ion-router-outlet/app-tabs/ion-content/ion-tabs/div[1]/ion-router-outlet/app-dashboard/ion-content/div/ion-grid/ion-row/ion-col[1]/ion-card[2]/ion-card-header/ion-card-title")
    # tp_number = driver.find_element_by_xpath("/html/body/app-root/ion-app/ion-router-outlet/app-tabs/ion-content/ion-tabs/div[1]/ion-router-outlet/app-dashboard/ion-content/div/ion-grid/ion-row/ion-col[1]/ion-card[2]/ion-card-header/ion-card-subtitle")
    
    
    
    attendance_page = driver.find_element_by_xpath("/html/body/app-root/ion-app/ion-router-outlet/app-tabs/ion-content/ion-tabs/div[1]/ion-router-outlet/app-dashboard/ion-content/div/ion-grid/ion-row/ion-col[1]/ion-card[3]/ion-card-content/ion-grid/ion-row/ion-col[1]/ion-button")
    
    attendance_page.click()
    driver.implicitly_wait(5)
    otp = driver.find_element_by_xpath("/html/body/app-root/ion-app/ion-router-outlet/app-student/ion-content/ion-grid/ion-row/ion-col/div/input[1]")
    otp.send_keys(code)
    
    driver.implicitly_wait(10)
    
    ##### alert message
    
    message = driver.find_element_by_id("alert-1-msg").text
    
    ### Show Time & Date
    now = datetime.now()
    current_time = now.strftime("%Y-%m-%d %H:%M:%S")
    
    print("Time :", current_time)
    print("Name :", name.text)
    print("Username :", username_1)
    print("Message :", message)
    
    #driver.quit()

def driver2():

    driver = webdriver.Chrome(executable_path="/usr/lib/chromium-browser/chromedriver")
    
    driver.get("https://apspace.apu.edu.my/tabs/dashboard")
           
    driver.implicitly_wait(5)
    login_show = driver.find_element_by_xpath("/html/body/app-root/ion-app/ion-router-outlet/app-login/ion-content/div/section[2]/div/ion-grid/ion-row[1]/ion-col[2]/ion-button")
    
    login_show.click()
    
    driver.implicitly_wait(5)
    
    AP_KEY = driver.find_element_by_xpath("/html/body/app-root/ion-app/ion-router-outlet/app-login/ion-content/div/section[2]/div/ion-grid/ion-row[2]/ion-col[1]/form/div/div[1]/ion-input/input")
    PASSWORD = driver.find_element_by_xpath("/html/body/app-root/ion-app/ion-router-outlet/app-login/ion-content/div/section[2]/div/ion-grid/ion-row[2]/ion-col[1]/form/div/div[2]/ion-input/input")
    
    AP_KEY.send_keys(username_2)
    PASSWORD.send_keys(password_2)
    
    login_button = driver.find_element_by_xpath("/html/body/app-root/ion-app/ion-router-outlet/app-login/ion-content/div/section[2]/div/ion-grid/ion-row[2]/ion-col[1]/form/div/div[3]/ion-button")
    
    login_button.click()
    
    
    #driver.implicitly_wait(5)
    driver.implicitly_wait(10)
    
    
    ##### read username , tp , course
    
    name = driver.find_element_by_xpath("/html/body/app-root/ion-app/ion-router-outlet/app-tabs/ion-content/ion-tabs/div[1]/ion-router-outlet/app-dashboard/ion-content/div/ion-grid/ion-row/ion-col[1]/ion-card[2]/ion-card-header/ion-card-title")
    # tp_number = driver.find_element_by_xpath("/html/body/app-root/ion-app/ion-router-outlet/app-tabs/ion-content/ion-tabs/div[1]/ion-router-outlet/app-dashboard/ion-content/div/ion-grid/ion-row/ion-col[1]/ion-card[2]/ion-card-header/ion-card-subtitle")
    
    
    
    attendance_page = driver.find_element_by_xpath("/html/body/app-root/ion-app/ion-router-outlet/app-tabs/ion-content/ion-tabs/div[1]/ion-router-outlet/app-dashboard/ion-content/div/ion-grid/ion-row/ion-col[1]/ion-card[3]/ion-card-content/ion-grid/ion-row/ion-col[1]/ion-button")
    
    attendance_page.click()
    driver.implicitly_wait(5)
    otp = driver.find_element_by_xpath("/html/body/app-root/ion-app/ion-router-outlet/app-student/ion-content/ion-grid/ion-row/ion-col/div/input[1]")
    otp.send_keys(code)
    
    driver.implicitly_wait(10)
    
    ##### alert message
    
    message = driver.find_element_by_id("alert-1-msg").text
    
    ### Show Time & Date
    now = datetime.now()
    current_time = now.strftime("%Y-%m-%d %H:%M:%S")
    
    print("Time :", current_time)
    print("Name :", name.text)
    print("Username :", username_1)
    print("Message :", message)
    
    driver.quit()

if validate_otp:
    #attendance.py code   
    code = arr[len(arr)-3]  
    driver1()

####driver2()









