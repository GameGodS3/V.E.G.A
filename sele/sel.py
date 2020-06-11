from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import csv
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

def createcred():
    temp = input("Type your Instagram username: ")+","+input("Type your Instagram password: ")
    with open('credential.csv', 'w+') as f:
        f.write(temp)
    print("Credentials stored successfully. Resuming login...")

def activity():
    try:
        with open('credential.csv', 'r') as credens:
            key = csv.reader(credens)
            for element in key:
                uname = element[0]
                pword = element[1]
    except IOError:
        print("You do not seem to have the credentials saved.")
        print("Launching prompt for credential creation.....")
        createcred()

    browser = webdriver.Chrome('./chromedriver.exe')
    browser.get('http://www.instagram.com')
    browser.implicitly_wait(30)
    user = browser.find_element_by_name('username')
    pwrd = browser.find_element_by_name('password')
    login = browser.find_element_by_tag_name('button')

    user.send_keys(uname)
    pwrd.send_keys(pword)
    login.click()

    browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button').click()
    browser.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]').click()


