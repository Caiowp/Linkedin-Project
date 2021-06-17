from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import ElementClickInterceptedException, ElementNotInteractableException
from sys import exit, argv
import time

with webdriver.Chrome() as driver:
    driver.get("https://linkedin.com")
    time.sleep(0.5)
    username = driver.find_element_by_xpath("//input[@name='session_key']")
    password = driver.find_element_by_xpath("//input[@name='session_password']")

    try:
        scriptname, userArg, passArg, keyword = argv
        username.send_keys(userArg)
        password.send_keys(passArg)
    except ValueError as e:
        print ('YOU NEED TO SPECIFY YOUR USERNAME FOLLOWED BY YOUR PASSWORD FOLLOWED BY A KEYWORD FOR YOUR SEARCH\neg. python linkedin.py foo bar')
        exit(1)

    submit = driver.find_element_by_xpath("//button[@type = 'submit']").click()

    time.sleep(2)

    driver.get("https://www.linkedin.com/search/results/people/?keywords="+keyword+"&origin=GLOBAL_SEARCH_HEADER")

    time.sleep(2)


    count = 2
    while True:
      all_buttons = driver.find_elements_by_tag_name("button")
      connect_buttons = [btn for btn in all_buttons if btn.text == "Conectar"]
      for i in range(0, len(connect_buttons)):
        time.sleep(1)
        try:
            connect_buttons[i].click()
            time.sleep(0.3)
            all_buttons = driver.find_elements_by_tag_name("button")
            send_button = [btn for btn in all_buttons if btn.text == "Enviar"]
            send_button[0].click()
        except ElementClickInterceptedException:
            time.sleep(2)
            driver.get("https://www.linkedin.com/search/results/people/?keywords="+keyword+"&origin=GLOBAL_SEARCH_HEADER&page="+str(count-1))
            time.sleep(1)
        except ElementNotInteractableException:
            time.sleep(2)
            driver.get("https://www.linkedin.com/search/results/people/?keywords="+keyword+"&origin=GLOBAL_SEARCH_HEADER&page="+str(count-1))
            time.sleep(1)
      time.sleep(0.3)
      driver.get("https://www.linkedin.com/search/results/people/?keywords="+keyword+"&origin=GLOBAL_SEARCH_HEADER&page="+str(count))
      count+=1
      time.sleep(0.5)
