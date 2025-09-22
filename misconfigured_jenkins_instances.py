from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
import re

options = Options()
options.headless = False
username = "Your Github username"
password = "Your github password"
jenkins_list = open("jenkins-instances.txt","r").readlines()
for jenkins in jenkis_list:
    jenkins = jenkins.rstrip("\n")
    print("Checking - "+jenkins)
    driver = webdriver.Firefox(options=options)
    driver.set_page_load_timeout(20)
    try:
        driver.get(jenkins)
    except:
        print("Page load timeout")
    driver.implicitly.wait(20)
    try:
        element = driver.find_element_by_id("login_field")
        element.send_key(username)
        element = driver.find_element_by_id("password")
        element.send_key(password)
        element = driver.find_element_by_name("commit")
        element.click()
        element = driver.find_element_by_id("js-oauth-authorize-btn")
        element.click()
    except:
        pass
    if re.findall(r"Manage\sJenkins",driver.page_source):
        print(jenkins+" - Jenknis Misconfigured")
    driver.quit()
