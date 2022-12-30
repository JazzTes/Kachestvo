import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

url = "https://iotvega.com/product"
driver = webdriver.Chrome(executable_path="E:\\S HITACHI\\4\\качество\\l2\\chromedriver\\chromedriver.exe")
url_prod, T = [], []


class MyTestCase(unittest.TestCase):
    def test_table(self):
        try:
            driver.get(url=url)
            time.sleep(5)
            file_name = "out3.csv"
            out3 = open(file_name, 'r')
            s = ''
            for i in out3.readlines():
                s += i
            element = driver.find_element(By.TAG_NAME, "body")
            for i in range(1, 53, 1):
                url_product = element.find_elements(By.XPATH, f"/ html / body / section[3] / div / div[2] / div[1] "
                                                              f"/ div[{str(i)}] / a")
                for e in url_product:
                    url_prod.append(e.get_attribute('href'))
            for i in range(0, 52, 1):
                driver.get(url=url_prod[i])
                time.sleep(5)
                Block = driver.find_element(By.TAG_NAME, "body")
                Table = Block.find_elements(By.XPATH, "//tbody")
                for e in Table:
                    T.append(e.text.replace('\n', ', '))
            for i in T:
                self.assertIn(i, s)
            out3.close()
        except Exception as ex:
            print(ex)
        finally:
            driver.close()
            driver.quit()


if __name__ == '__main__':
    unittest.main()
