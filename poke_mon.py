import selenium.webdriver as wb
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import os
import csv
import time 
options = Options()
options.add_argument("--headless")
options.add_argument("--nosandbox")
options.add_argument("--disable-dev-shm-usage")
url = "https://pokemonkorea.co.kr/pokedex"
driver = wb.Chrome(options=options)
driver.maximize_window()
driver.get(url)
img = driver.find_element(By.CSS_SELECTOR, "img.img-fluid")
img.click()
time.sleep(0.2)
h3 = driver.find_element(By.TAG_NAME,"h3")
name = h3.text.split("\n")[1]
poke_exist = os.path.exists("pokemon.csv")
header = ["No.","name"]

with open ("pokemon.csv","a",newline="") as file:
    writer = csv.writer(file)
    if not poke_exist:
        writer.writerow(header)

    writer.writerow(["0001",name])
    print("포켓몬 저장 완료")
