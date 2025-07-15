import selenium.webdriver as wb
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import time
import csv
import os


service = Service(executable_path="/usr/bin/chromedriver")

options = Options()
options.add_argument("--headless") # 창 없음
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

url = "https://pokemonkorea.co.kr/pokedex"
driver = wb.Chrome(service=service, options=options)
driver.maximize_window()
driver.get(url)
img = driver.find_element(By.CSS_SELECTOR, "img.img-fluid")
img.click()
time.sleep(1)
h3 = driver.find_element(By.TAG_NAME, "h3")
name = h3.text.split("\n")[1]

driver.close()


pokemon_exist = os.path.exists("pokemon.csv")
header = ["no", "name"]

with open("pokemon.csv", "a", newline="") as file:
    writer = csv.writer(file)

    if not pokemon_exist:
        writer.writerow(header)

    writer.writerow(["0001", name])
    print("포켓몬 저장 완료!!")
