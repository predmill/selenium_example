from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wait
import subprocess
from selenium.webdriver.common.by import By
import tkinter
import time


def generate_a_password():
    driver = webdriver.Chrome()

    driver.get("https://www.dashlane.com/features/password-generator")

    #Sanity check: get the webpage title
    title = driver.title

    driver.implicitly_wait(0.5)

    #Generate the password
    generate_button = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[aria-label='Regenerate password']")))
    generate_button.click()
    
    
    #Put password on clipboard
    wait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Copy password']"))).click()
    root = tkinter.Tk()
    
    #Print the password from clipboard
    password = root.selection_get(selection="CLIPBOARD")
    print(password)
    root.quit()

    driver.quit()

for x in range(1,11):
    #generate a password then take a beat for 30s
    generate_a_password()
    time.sleep(30)