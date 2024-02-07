import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.firefox.options import Options
from twocaptcha import TwoCaptcha

username = "username"
password = "password"
captcha_api ="captcha-api"
t = 1

def login():
    options = Options() 
    options.add_argument("-headless")
    driver = webdriver.Firefox(options=options)
    driver.get("https://golestan.ub.ac.ir/forms/authenticateuser/main.htm")
    driver.switch_to.frame(0)
    time.sleep(1*t)
    driver.switch_to.frame(3)
    time.sleep(1*t)
    driver.switch_to.frame(1)
    time.sleep(6*t)
    driver.find_element(By.ID, "F80351").send_keys(username)
    driver.find_element(By.ID, "F80401").send_keys(password)
    driver.find_element(By.TAG_NAME,"img").click()
    captcha_src = driver.find_element(By.TAG_NAME,"img").get_attribute("src")
    acp = captcha(captcha_src)#this part of code can be better
    captcha_box = driver.find_element(By.ID,"F51701")
    captcha_box.send_keys(acp)
    captcha_box.send_keys(Keys.ENTER)
    #after log in to page we wane
    time.sleep(5*t)
    driver.switch_to.parent_frame()
    time.sleep(1*t)
    driver.switch_to.parent_frame()
    time.sleep(1*t)
    driver.switch_to.parent_frame()
    time.sleep(1*t)
    driver.switch_to.frame(1)
    time.sleep(1*t)
    driver.switch_to.frame(3)
    time.sleep(1*t)
    driver.switch_to.frame(2)
    time.sleep(5*t)
    driver.find_element(By.XPATH,"/html/body/table[1]/tbody/tr[6]/td[2]/div/table/tbody/tr[7]").click()
    driver.find_element(By.XPATH,"/html/body/table[1]/tbody/tr[6]/td[2]/div/table/tbody/tr[7]").click()
    time.sleep(1*t)
    driver.switch_to.parent_frame()
    time.sleep(1*t)
    driver.switch_to.parent_frame()
    time.sleep(1*t)
    driver.switch_to.parent_frame()
    time.sleep(1*t)
    driver.switch_to.frame(2)
    time.sleep(1*t)
    driver.switch_to.frame(3)
    time.sleep(5*t)
    driver.switch_to.frame(2)
    driver.find_element(By.XPATH, "/html/body/div[3]/table/tbody/tr[5]/td[3]").click()
    time.sleep(1*t)
    driver.switch_to.parent_frame()
    time.sleep(1*t)
    driver.switch_to.parent_frame()
    time.sleep(1*t)
    driver.switch_to.parent_frame()
    time.sleep(1*t)
    driver.switch_to.frame(2)
    time.sleep(1*t)
    driver.switch_to.frame(3)
    time.sleep(1*t)
    driver.switch_to.frame(2)
    time.sleep(1*t)
    driver.switch_to.frame(2)
    time.sleep(5*t)
    data = driver.page_source
    print("------------------------------------------------------------")
    driver.quit()
    hToT(data)

    #print("------------------------------------------------------------")
    #print (driver.page_source)
    
def captcha(cp):
    solver = TwoCaptcha(captcha_api)
    result = solver.normal(cp,minLen = "5",maxLen = "5",phrase = "1")
    return result["code"]

def hToT(HTMLDoc):

    with open("tmp.html", "w", encoding="utf-8") as f:
        f.write(HTMLDoc)
    html_tables = pd.read_html("tmp.html", encoding="utf8")
    data2 = html_tables[2]
    data3 = (data2.loc[1:8,[5,8]])
    with open("out.txt", "w") as f:
        f.write(str(data3))
    print (data3)

#def show():

#def setup_telegram():

#def telegram_bat():

login()