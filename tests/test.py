import pytest
from selenium.webdriver.common.by import By

def test_example(selenium):
    selenium.get("https://websdk.dev.vyyer.id/")

    # locating product on webpage and getting name of the product
    #productText = selenium.find_element(By.XPATH, '//*[@id="1"]/p').text

    # clicking the "full KYC button on the page"
    selenium.find_element(By.XPATH, "//div[@id='app']/div/div/div[2]/div[2]/div/div[2]").click()

    # then we'll click on the element on the widget, the same KYC
    selenium.find_element(By.XPATH, "//div[@id='app']/div/div/vyyer-widget").click()

    # locating product in cart and getting name of the product in cart
    #productCartText = selenium.find_element(By.XPATH, '//*[@id="__next"]/div/div/div[2]/div[2]/div[2]/div/div[3]/p[1]').text

    # checking whether product has been added to cart by comparing product name
    #assert productCartText == productText
