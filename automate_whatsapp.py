import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--user-data-dir=chrome-data")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
webDriver = webdriver.Chrome('C:\webdrivers\chromedriver.exe', options=options)
webDriver.maximize_window()
webDriver.get('https://web.whatsapp.com')  # Already authenticated

time.sleep(35)
 
webDriver.find_element_by_xpath("//*[@title='Reshanna Jagroo']").click()

now = datetime.now(); 
current_time = now.strftime("%H:%M")
x = 4; 
while(x > 0):
    now = datetime.now(); 
    current_time = now.strftime("%H:%M")
    print(current_time)
    if(current_time == "09:11"):
        webDriver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys("9:11")
        webDriver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button/span').click()
        x = x - 1
        time.sleep(60)

    if(current_time == "11:11"):
        webDriver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(current_time)
        webDriver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button/span').click()
        x = x - 1
        time.sleep(60)

    if(current_time == "16:20"):
        webDriver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys("4:20")
        webDriver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button/span').click()
        x = x - 1
        time.sleep(60)

    if(current_time == "21:11"):
        webDriver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys("9:11")
        webDriver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button/span').click()
        x = x - 1
        time.sleep(60)
    
    if(current_time == "23:11"):
        webDriver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys("11:11")
        webDriver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button/span').click()
        x = x - 1
        time.sleep(60)

time.sleep(5)

webDriver.close()