from selenium import webdriver
from selenium.webdriver.common.by import By

# 지시사항 1번을 작성하세요.
with webdriver.Firefox() as driver:
    driver.get("http://localhost:8080")
    # 지시사항 2번을 작성하세요.
    o = driver.find_element(By.TAG_NAME, "ol")
    print(type(o))
    l = o.find_elements(By.TAG_NAME, "li")
    print(type(l))

    for li in l:
        print(li.text)


    # 지시사항 3번을 작성하세요.
    big_list = driver.find_element(By.CLASS_NAME, "big")
    for big in big_list:
        print(big.text)
    # 지시사항 4번을 작성하세요.
    
    ul = driver.find_element(By.TAG_NAME, "ul")
    bold = ul.find_elements(By.CLASS_NAME, "bold")
    print(bold.text)
