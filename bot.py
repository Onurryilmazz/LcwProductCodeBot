from selenium import webdriver
from writeExcel import writeExcelFile
import time
import os

def getProductsCode(link,productCount,excelFileName):

    # op = webdriver.ChromeOptions()
    # op.headless = True
    # op.add_experimental_option('excludeSwitches', ['enable-logging'])
    # driver = webdriver.Chrome('chromedriver.exe',options=op)
    # driver.get(link)

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")

    driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"),options=chrome_options)
    driver.get(link)

    div_list = driver.find_elements_by_xpath("//*[@class='product-card product-card--one-of-4']")

    div_list = ControlProductCount(driver,div_list,int(productCount))

    productsLinkList = [product.find_element_by_tag_name("a").get_attribute("href") for product in div_list]
 
    productsCode = []
    for productPage in productsLinkList:
        driver.get(productPage)
        try:
            productCode = driver.find_element_by_xpath("//*[@id='rightInfoBar']/div[1]/div/div[1]/div[1]/div[1]").text
            productsCode.append(productCode.replace("Ürün Kodu:",'').strip())
            
        except:
            productCodeDiv = driver.find_elements_by_xpath("//*[@class='look-product-detail-col look-product-code hidden-xs hidden-sm']")
            for productCodeTextElement in productCodeDiv:
                productCode = productCodeTextElement.find_elements_by_tag_name("p")[1].get_attribute("innerHTML")
                productsCode.append(productCode)
            

    writeExcelFile(productsCode,excelFileName)
    driver.close()


def ControlProductCount(driver,product_div_list,productCount):

    if len(product_div_list) >= productCount:
        return product_div_list[:productCount]

    else:
        while len(product_div_list) <= productCount:
            button_div = driver.find_element_by_xpath("//*[@class='paginator__button']")
            driver.execute_script("arguments[0].click();", button_div)
            time.sleep(1)
            product_div_list = driver.find_elements_by_xpath("//*[@class='product-card product-card--one-of-4']")
        return product_div_list[:productCount]