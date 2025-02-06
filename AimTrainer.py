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
driver.get("https://humanbenchmark.com/tests/aim")
area=WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div[4]/div[1]/div/div[1]/div[2]")))
for i in range(31):
    while True:
        try:
            area.find_element(By.XPATH, '/html/body/div/div/div[4]/div[1]/div/div[1]/div/div/div/div[6]').click()
            break
        except:
            continue
save=WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div[4]/div[1]/div/div[1]/div/div[3]/button[1]"))).click()
time.sleep(2)
driver.quit()