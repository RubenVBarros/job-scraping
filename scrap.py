from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Edge()
driver.get('https://glassdoor.com')

#on attend pour pas faire le robot
time.sleep(10)


#GLASSDOOR
#emailField = driver.find_element(By.ID,'')
#emailButton -> bouton continuer avec un email  inlineUserEmail -> champ email
emailInput = driver.find_element(By.ID,"inlineUserEmail")
emailInput.send_keys("rubenvenancio67@gmail.com")
time.sleep(5)
emailButton = driver.find_element(By.CLASS_NAME,"emailButton")
emailButton.click()
#jobCardField = driver.find_element(By.ID,"left-column")

#jobCardField.click()

time.sleep(2)