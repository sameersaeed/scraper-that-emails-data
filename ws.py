# sameer saeed
# scraper that gets stock availability of various retailers from site 'stocktrack.ca'
# i used this to check if certain pools were in stock at walmarts in a specific location

import datetime
import time
from selenium import webdriver

directory = '/Users/sameersaeed/Downloads/chromedriver' # directory for chromedriver, in macOS
link = 'https://stocktrack.ca/?s=wm'
src = 'wm/index.php'
UPC = '82180803890'   # UPC of product: bestway 15x33
SKU = '6000202186409' # SKU of product: bestway 15x33
#UPC = '19207202359'  # product: summer waves 14ft
search = '[input a string here to search]' # to search for something manually
search = search.replace(" ", "%20") # formatting search value so it can be appended to url
#wm = walmart, ct=canadian tire, st=staples, bb=bestbuy, src=the source, hd=home depot, lws=lowe's, reno=renodepot,sc=sportchek, as=atmosphere
stores = ['?s=wm', '?s=ct', '?s=st', '?s=bb', '?s=src', '?s=hd', '?s=lws', '?s=rona', '?s=reno', '?s=sc', '?s=as']
types = ['&upc=' + UPC, '&sku=' + SKU, '&search=' + search] #type of search being done
Location = "Windsor, ON"

# getting date and time of screnshot
date_time = str(datetime.datetime.now())
date_time_ = date_time.replace(" ", "_")
filename = "ws_screenshot_" + date_time_ + ".png"

# scraping
selectType = ".//select[@name='type']"
driver = webdriver.Chrome(directory)
driver.get(link)
driver.maximize_window()
driver.switch_to.frame(driver.find_element_by_xpath("//iframe[contains(@src,'wm/index.php?s=wm')]"))
time.sleep(12)

pType = driver.find_element_by_xpath(selectType)
pType.click()

# types of searches
upcSelect = "1"
searchSelect = "2"
skuSelect = "3"
dealsSelect = "4"

# doing searches with UPC ID
pinnerType = driver.find_element_by_xpath(selectType + "/option[" + upcSelect + "]").click()

sType = driver.find_element_by_name('q').send_keys(UPC)
loc = driver.find_element_by_name('loc').send_keys(Location)

# getting div elements and sleeping to let everything load properly
Check = driver.find_element_by_xpath('//*[@id="layoutObj"]/div/div[1]/div[2]/div/div/div[1]/div[2]/div/div/div[8]/div/div[2]').click()
time.sleep(7)
# Product = driver.find_element_by_xpath("//*[contains(@id, 'ListObject_')]/div").click()
driver.refresh()
time.sleep(12)

# taking a screenshot of data to include in email
driver.save_screenshot(filename)
print("Screenshot saved.\nFilename is: " + filename)
driver.quit()
