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
driver.get("https://humanbenchmark.com/tests/chimp")
driver.find_element(By.XPATH, "/html/body/div[1]/div/div[4]/div[1]/div/div[1]/div[2]/button").click()
DesiredLevel=100 #Change to level/score you want to end on
level=1

while level<DesiredLevel:
    grid=driver.find_element(By.XPATH,"/html/body/div[1]/div/div[4]/div[1]/div/div[1]/div/div")
    numbers= [i.text for i in grid.find_elements(By.CLASS_NAME,"css-19b5rdt")]
    Highlighted=list(zip(grid.find_elements(By.CLASS_NAME,"css-19b5rdt"),numbers))
    for j in range(level+3):
        for i in Highlighted:
            if i[1]==str(j+1):
                i[0].click()
                Highlighted.remove(i)
    level+=1
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div[4]/div[1]/div/div[1]/div[3]/button"))).click()
for i in range(3):
    grid=driver.find_element(By.XPATH,"/html/body/div[1]/div/div[4]/div[1]/div/div[1]/div/div")
    numbers= [i.text for i in grid.find_elements(By.CLASS_NAME,"css-19b5rdt")]
    Highlighted=list(zip(grid.find_elements(By.CLASS_NAME,"css-19b5rdt"),numbers))
    for j in range(3):
        for i in Highlighted:
            if i[1]!=str(j+1):
                i[0].click()
                Highlighted.remove(i)
                break
        else:
            continue
        break
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[4]/div[1]/div/div[1]/div[3]/button"))).click()
save = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div[4]/div[1]/div/div/div[3]/button[1]"))).click()
time.sleep(2)
driver.quit()