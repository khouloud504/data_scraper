import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
import soupsieve


driver = webdriver.Chrome()
driver.implicitly_wait(15) 

url = "https://www.woolworths.com.au/shop/browse/drinks/cordials-juices-iced-teas/iced-teas"

driver.get(url)

elements = driver.find_elements(By.CSS_SELECTOR, ".primary")

information_list = []
information_elements = soupsieve.find_all("div", class_="_ngcontent-serverapp-c172 primary")
for element in information_elements:
    information_list.append(element.text.strip())
    
driver.quit()

# Write the extracted information to a text file
output_file = "output.txt"
with open(output_file, "w") as file:
    for info in information_list:
        file.write(info + "\n")