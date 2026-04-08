from bs4 import BeautifulSoup
import requests
from time import sleep

#Website URL
URL = "https://appbrewery.github.io/Zillow-Clone/"
response = requests.get(URL)
data = response.text

#Useing Beautifulsoup to scrap data
soup = BeautifulSoup(data,"html.parser")

#saving address
address_list = []
for i in soup.select('address'):
    address_list.append(i.get_text().strip())

#saving price
rate_list = []
for i in soup.select('.PropertyCardWrapper__StyledPriceLine'):
    rate_list.append(i.get_text().strip())

# saving links
link = []
for i in  soup.select("#zpid_2056905294 a"):
    link.append(i.get("href").strip())

#using selenium to automate the data obtained by web-scraping to enter in google form
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

GOOGLE_FORM = "YOUR_GOOGLE_FORM_LINK"

#setting up Chrome Driver
options = webdriver.ChromeOptions()
options.add_experimental_option("detach",True)

driver = webdriver.Chrome(options=options)
driver.get(GOOGLE_FORM)
driver.maximize_window()
wait = WebDriverWait(driver,10)
driver.implicitly_wait(5)

#Adding all the values in google form
for i in range(0,len(address_list)):
    address_form = wait.until(ec.presence_of_element_located((By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div[2]/textarea')))
    address_form.send_keys(address_list[i])

    rate_form = driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    rate_form.send_keys(rate_list[i])

    link_form = driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div[2]/textarea')
    link_form.send_keys(link[i])

    submit = driver.find_element(By.XPATH,"//div[@role='button' and @aria-label='Submit']")
    submit.click()

    again = wait.until(ec.element_to_be_clickable((By.XPATH,'//a[contains(normalize-space(),"Submit another response")]')))
    again.click()

    print(f"Date Entry :- {i+1} Submitted..✅")
    print(f"-- > {address_list[i]}")
    print(f"-- > {rate_list[i]}")
    print(f"-- > {link[i]}")
    print("_________________________________________________")
sleep(2)
driver.quit()

