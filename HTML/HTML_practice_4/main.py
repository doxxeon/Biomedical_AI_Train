from selenium import webdriver
from selenium.webdriver.common.by import By

# 지시사항 1번을 작성하세요.
with webdriver.Firefox() as driver:
    driver.get("http://localhost:8080")
    # 지시사항 2번을 작성하세요.
    xpath = '/html/body/ol/li'
    print('pl/li: ', xpath)

    # 지시사항 3번을 작성하세요.
    li_list = driver.find_elements(By.XPATH, xpath)
    for li in li_list:
        print(li.text)

    # 지시사항 4번을 작성하세요.
    xpath2 = '//*[contains(@class, "big")]'
    print(xpath2)

    # 지시사항 5번을 작성하세요.
    big_list = driver.find_element(By.XPATH, xpath2)
    for big in big_list:
        print(big.text)

    # 지시사항 6번을 작성하세요.
    xpath3 = ''
    print(xpath3)

    # 지시사항 7번을 작성하세요.
    