from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Edge()
driver.get('https://glassdoor.com')

#on attend pour pas faire le robot
time.sleep(5)

#GLASSDOOR
#emailField = driver.find_element(By.ID,'')
#emailButton -> bouton continuer avec un email  inlineUserEmail -> champ email

email = input("What is your email ?\n")
pwd = input('What is your password ?\n')
time.sleep(4)
emailInput = driver.find_element(By.ID,"inlineUserEmail")
emailInput.send_keys(email)
time.sleep(5)
emailButton = driver.find_element(By.CLASS_NAME,"emailButton")
emailButton.click()
time.sleep(3)
pwdInput = driver.find_element(By.ID,"inlineUserPassword")
pwdInput.send_keys(pwd)
time.sleep(3)
pwdButton = driver.find_element(By.CLASS_NAME,"emailButton")
pwdButton.click()

time.sleep(1000)
#jobCardField = driver.find_element(By.ID,"left-column")

#jobCardField.click()
