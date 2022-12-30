import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

url = "https://iotvega.com/product"
driver = webdriver.Chrome(executable_path="E:\\S HITACHI\\4\\качество\\l2\\chromedriver\\chromedriver.exe")


class MyTestCase(unittest.TestCase):
    def test_name(self):
        try:
            PN = []
            driver.get(url=url)
            time.sleep(5)
            element = driver.find_element(By.TAG_NAME, "body")
            Product_name = element.find_elements(By.CLASS_NAME, "product-name")
            for e in Product_name:
                PN.append(e.text)

            file_name = "out3.csv"
            out3 = open(file_name, 'r')
            all_data = ''
            for i in out3.readlines():
                all_data += i
            for i in PN:
                self.assertIn(i, all_data)

            out3.close()
        except Exception as ex:
            print(ex)
        finally:
            driver.close()
            driver.quit()


if __name__ == '__main__':
    unittest.main()
