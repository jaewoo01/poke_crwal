from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import selenium.webdriver as wb
import time
import csv
import os
service = Service(executable_path="/usr/bin/chromedriver")
options = Options()
options.add_argument("--headless") # 창 없음
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
url_poke = "https://pokemonkorea.co.kr/pokedex"
driver = wb.Chrome(service=service, options=options)
driver.maximize_window()
driver.get(url_poke)
poke_list = []
delay = 0.5
for _ in range (10):
    body = driver.find_element(By.TAG_NAME, "body")
    body.send_keys(Keys.END)
    time.sleep(delay)
img_list = driver.find_elements(By.CSS_SELECTOR, ".img-fluid")
for i in range (len(img_list)):
    for _ in range(10):
        body = driver.find_element(By.TAG_NAME, "body")
        body.send_keys(Keys.END)
        time.sleep(delay)
    img_list = driver.find_elements(By.CSS_SELECTOR, ".img-fluid")
    img_list[i].click()
    time.sleep(delay)
    # Name
    h3 = driver.find_element(By.TAG_NAME, "h3")
    poke_name = h3.text.split("\n")[1]
    # Type
    type_list = driver.find_elements(By.CSS_SELECTOR,"img-type>p")
    poke_type = ""
    poke_type = ", ".join([p.text for p in type_list])
    # detail info
    info_list = driver.find_elements(By.CSS_SELECTOR, "h4.mb-3+p")
    poke_heig = info_list[0].text
    poke_cate = info_list[1].text
    poke_weig = info_list[2].text
    driver.back()
    pokemon_exist = os.path.exists("poke_test.csv")
    with open("poke_test.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([poke_name, poke_type, poke_heig, poke_cate, poke_weig])
    
        if not pokemon_exist:
            writer.writerow(header)             
driver.close()
    
