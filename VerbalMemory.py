from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
# Specify custom profile path
options = Options()
options.add_argument("user-data-dir=/path/to/your/custom/profile/1")  # Replace with your actual custom profile path
options.add_argument("--start-maximized")
# Initialize the Chrome driver with the service and options
driver = webdriver.Chrome(
    service=Service(r"C:\Users\aidan\Downloads\chromedriver-win64\chromedriver.exe"),
    options=options
)
driver.get("https://humanbenchmark.com/tests/verbal-memory")
driver.find_element(By.XPATH, "/html/body/div[1]/div/div[4]/div[1]/div/div/div/div[4]/button").click()
time.sleep(1)
DesiredLevel=100 #Change to level/score you want to end on
score=1
words=[]
while score<DesiredLevel:
    if driver.find_element(By.CLASS_NAME,'word').text in words:
        driver.find_element(By.XPATH,"/html/body/div[1]/div/div[4]/div[1]/div/div/div/div[3]/button[1]").click()
        score+=1
    else:
        words.append(driver.find_element(By.CLASS_NAME,'word').text)
        driver.find_element(By.XPATH,"/html/body/div[1]/div/div[4]/div[1]/div/div/div/div[3]/button[2]").click()
        score+=1
for i in range(3):        
    if driver.find_element(By.CLASS_NAME,'word').text not in words:
        driver.find_element(By.XPATH,"/html/body/div[1]/div/div[4]/div[1]/div/div/div/div[3]/button[1]").click()
    else:
        words.append(driver.find_element(By.CLASS_NAME,'word').text)
        driver.find_element(By.XPATH,"/html/body/div[1]/div/div[4]/div[1]/div/div/div/div[3]/button[2]").click()
save = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[4]/div[1]/div/div/div[3]/button[1]"))).click()
time.sleep(2)
driver.quit()
