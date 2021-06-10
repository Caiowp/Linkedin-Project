from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from sys import argv, exit
import time

with webdriver.Chrome() as driver:
    driver.get("https://linkedin.com")
    time.sleep(0.5)
    username = driver.find_element_by_xpath("//input[@name='session_key']")
    password = driver.find_element_by_xpath("//input[@name='session_password']")

    try:
        scriptname, username, password = argv
        username.send_keys(username)
        password.send_keys(password)
    except ValueError as e:
        print ('YOU NEED TO SPECIFY YOUR USERNAME FOLLOWED BY YOUR PASSWORD\neg. python linkedin.py foo bar')
        exit(1)

    submit = driver.find_element_by_xpath("//button[@type = 'submit']").click()

    time.sleep(2)

    driver.get("https://www.linkedin.com/search/results/people/?network=%5B%22F%22%5D&origin=FACETED_SEARCH")

    time.sleep(2)

    all_buttons = driver.find_elements_by_tag_name("button")
    message_buttons = [btn for btn in all_buttons if btn.text == "Enviar mensagem"]

    for i in range(0, len(message_buttons)):
        message_buttons[i].click()
        time.sleep(0.5)
        main_div = driver.find_element_by_xpath("//div[starts-with(@class, 'msg-form__msg-content-container')]").click()
        time.sleep(0.5)
        paragraphs = driver.find_elements_by_tag_name("p")
        paragraphs[-5].send_keys("teste")
        time.sleep(0.5)
        send_button = driver.find_element_by_xpath("//button[@type= 'submit' ]").click()
        time.sleep(0.5)
        close_button= driver.find_element_by_xpath("//button[starts-with(@data-control-name, 'overlay.close_conversation_window')]").click()
        time.sleep(0.5)
