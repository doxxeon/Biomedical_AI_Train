# 클라이언트

from selenium import webdriver
from selenium.webdriver.common.by import By

# 지시사항 1번을 작성하세요.
with webdriver.Firefox() as driver:
    
    # 지시사항 2번을 작성하세요.
    driver.get("http://localhost:8080") # 127.0.0.1 = localhost
    # 지시사항 3번을 작성하세요.
    t = driver.find_element(By.TAG_NAME, "title")
    print(t.text)
    # 지시사항 4번을 작성하세요.
    i = driver.find_elements(By.TAG_NAME, "img")
    for i in i:
        print(i.get_attribute("src"))
    # 지시사항 5번을 작성하세요.
    d = driver.find_element(By.TAG_NAME, "div")
    for d in d:
        p = d.find_element(By.TAG_NAME, "p")
        for p in p:
            print(p.text)