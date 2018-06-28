from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

import csv, os

USE_HEADLESS = False
#url = "https://www.apartments.com/san-jose-ca/?bb=_-m8ujm6wO1shnm9I"
url = "https://www.apartments.com"
location = "San Jose, CA"

if USE_HEADLESS:
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    #chrome_options.add_argument("--window-size=1920x1080")
    # chrome_driver = os.getcwd() + "\\chromedriver.exe"
    driver = webdriver.Chrome(chrome_options=chrome_options)
else:
    driver = webdriver.Chrome()
#driver = webdriver.PhantomJS()
driver.get(url)


search_location_elem = driver.find_element_by_css_selector("input.quickSearchLookup")
search_location_elem.send_keys(location)

search_location_elem.clear()
search_location_elem.send_keys(location)

search_action_elem = driver.find_element_by_class_name("go").click()

csv_file = open("rent_range2.csv", "w", newline='')
writer = csv.writer(csv_file)
writer.writerow(["Apt name", "Rent range"])


data = driver.find_elements_by_class_name("altRentDisplay")
print(data)
for rent_range in data:
    print(rent_range.text)

driver.close()
