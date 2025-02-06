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
driver.get("https://humanbenchmark.com/tests/number-memory")
driver.find_element(By.XPATH, "/html/body/div/div/div[4]/div[1]/div/div/div/div[3]/button").click()
time.sleep(1)
DesiredLevel=5 #Change to level/score you want to end on
level=1
while level<DesiredLevel:
    Number = driver.find_element(By.CLASS_NAME,'big-number').text
    input = WebDriverWait(driver, 10000000).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div[4]/div[1]/div/div/div/form/div[2]/input")))
    input.send_keys(str(Number))
    driver.find_element(By.XPATH,"/html/body/div/div/div[4]/div[1]/div/div/div/form/div[3]/button").click()
    time.sleep(1)
    driver.find_element(By.XPATH,"/html/body/div/div/div[4]/div[1]/div/div/div/div[2]/button").click()
    level+=1
input = WebDriverWait(driver, 10000000).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div[4]/div[1]/div/div/div/form/div[2]/input")))
input.send_keys("a")
driver.find_element(By.XPATH,"/html/body/div/div/div[4]/div[1]/div/div/div/form/div[3]/button").click()
save = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div[4]/div[1]/div/div/div/div[2]/div/button[1]"))).click()
time.sleep(2)
driver.quit()