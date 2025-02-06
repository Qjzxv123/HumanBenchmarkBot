from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import AimTrainer, ChimpTest, NumberMemory, ReactionTime, SequenceMemory, Typing, VerbalMemory, VisualMemory
# Specify custom profile path
options = Options()
options.add_argument("user-data-dir=/path/to/your/custom/profile/1")  # Replace with your actual custom profile path
options.add_argument("--start-maximized")
# Initialize the Chrome driver with the service and options
Username = input("Enter Username: ")
Password = input("Enter Password: ")
driver = webdriver.Chrome(
    service=Service(r"C:\Users\aidan\Downloads\chromedriver-win64\chromedriver.exe"),
    options=options
)
driver.get("https://humanbenchmark.com/login")
form=WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div[4]/div/div/form")))
form.find_element(By.XPATH, "/html/body/div/div/div[4]/div/div/form/p[1]/input").send_keys(Username)
form.find_element(By.XPATH, "/html/body/div/div/div[4]/div/div/form/p[2]/input").send_keys(Password)
form.find_element(By.XPATH, "/html/body/div/div/div[4]/div/div/form/p[3]/input").click()
time.sleep(2)
driver.quit()