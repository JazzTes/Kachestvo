from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import csv
url = "https://iotvega.com/product"
driver = webdriver.Chrome(executable_path="E:\\S HITACHI\\4\\качество\\l2\\chromedriver\\chromedriver.exe")

PH, PI, PIO, T, RESULTS, url_prod = [], [], [], [], [], []

try:
    driver.get(url=url)
    time.sleep(5)
    element = driver.find_element(By.TAG_NAME, "body")
    for i in range(1, 53, 1):
        url_product = element.find_elements(By.XPATH,
                                            f"/ html / body / section[3] / div / div[2] / div[1] / div[{str(i)}] / a")
        for e in url_product:
            url_prod.append(e.get_attribute('href'))

    for i in range(0, 52, 1):
        driver.get(url=url_prod[i])
        time.sleep(5)
        Block = driver.find_element(By.TAG_NAME, "body")
        portfolio_information = Block.find_elements(By.XPATH, "//section/div/div/div/div/div/h1")
        for e in portfolio_information:
            PH.append(e.text)
        portfolio_information2 = Block.find_elements(By.XPATH, "//section/div/div/div/p")
        for e in portfolio_information2:
            PI.append(e.text.replace('\n', ' '))

        project_info_overflow = Block.find_elements(By.XPATH, "// section / div / div / div[3] / "
                                                              "div / ul")
        for e in project_info_overflow:
            PIO.append(e.text.replace('\n', ', '))

        Table = Block.find_elements(By.XPATH, "//tbody")
        for e in Table:
            T.append(e.text.replace('\n', ', '))

    for i in range(0, 52, 1):
        RESULT = [PH[i], PI[i], PIO[i], T[i]]
        RESULTS.append(RESULT)

    file_name = "out3.csv"
    with open(file_name, "w", newline='') as f:
        csv_writer = csv.writer(f, delimiter=';')
        csv_writer.writerows(RESULTS)
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()



