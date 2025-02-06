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
driver.get("https://humanbenchmark.com/tests/memory")
driver.find_element(By.XPATH, "/html/body/div/div/div[4]/div[1]/div/div/div/div[2]/button").click()
DesiredLevel=100 #Change to level/score you want to end on
squares=3
while squares-2<DesiredLevel:
    Highlighted=[]
    while len(Highlighted)!=squares:
        Highlighted = driver.find_elements(By.CSS_SELECTOR,'div.active')
    time.sleep(2)
    for i in Highlighted:
        i.click()
    squares+=1
items=driver.find_element(By.XPATH,"/html/body/div/div/div[4]/div[1]/div/div/div/div[2]/div").find_elements(By.CLASS_NAME,"css-lxtdud")
for i in range(3):
    Highlighted=[]
    while len(Highlighted)!=squares:
        Highlighted = driver.find_elements(By.CSS_SELECTOR,'div.active')
    time.sleep(2)
    clicks=0
    for i in items:
        if i not in Highlighted and clicks<3:
            i.click()
            clicks+=1
save = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[4]/div[1]/div/div/div[3]/button[1]"))).click()
time.sleep(2)
driver.quit()