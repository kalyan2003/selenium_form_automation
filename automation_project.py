import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

service = Service("C:\\Drivers\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.maximize_window()

driver.get(
    "https://trytestingthis.netlify.app/index.html?fname=Varunreddy&lname=Paari&gender=male&option=option+1&Optionwithcheck%5B%5D=option&option1=Option+1&option2=Option+2&option3=Option+3&Options=Mint&favcolor=%233d6b6c&day=&a=100&myfile=Screenshot+%2882%29.png&quantity=1&message=The+cat+was+playing+in+the+garden.")

wait = WebDriverWait(driver, 10)

first_name = wait.until(EC.element_to_be_clickable((By.ID, "fname")))
first_name.clear()
first_name.send_keys("Pavan Klyan")

last_name = wait.until(EC.element_to_be_clickable((By.ID, "lname")))
last_name.clear()
last_name.send_keys("Chimmiri")

gend_radio = wait.until(EC.element_to_be_clickable((By.ID, "female")))
gend_radio.click()

sel_element = wait.until(EC.presence_of_element_located((By.ID, "option")))
select = Select(sel_element)
select.select_by_visible_text("Option 2")

sel_element = wait.until(EC.presence_of_element_located((By.ID, "option")))
select = Select(sel_element)
select.select_by_visible_text("Option 2")

option_check_box = wait.until(EC.presence_of_element_located((By.ID, "moption")))
option_check_box.click()

data_input = driver.find_element(By.NAME, "Options")
data_input.send_keys("Strawberry")

color_input = wait.until(EC.element_to_be_clickable((By.ID, "favcolor")))
color_input.clear()
driver.execute_script("arguments[0].value = '#FF0000';", color_input)

date_element = wait.until(EC.element_to_be_clickable((By.ID, "day")))
date_element.clear()
date_element.send_keys("24-05-2025")

slider_input = wait.until(EC.element_to_be_clickable((By.ID, "a")))
desired_value = "76"
driver.execute_script(f"arguments[0].value = '{desired_value}'; arguments[0].dispatchEvent(new Event('change'));",
                      slider_input)

file_input = wait.until(EC.element_to_be_clickable((By.ID, "myfile")))
file_path = r"C:\Users\pavan\OneDrive\Pictures\Comprhension_1.png"
file_input.send_keys(file_path)

range_input = wait.until(EC.element_to_be_clickable((By.ID, "quantity")))
range_input.clear()
range_input.send_keys("50")

textarea_input = wait.until(EC.element_to_be_clickable((By.TAG_NAME, "textarea")))
textarea_input.clear()
textarea_input.send_keys(
    "Search the world's information, including webpages, images, videos and more. Google has many special features to help you find exactly what you're looking ....")

print("before")
submit_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn.btn-success")))
submit_btn.click()
print("alert")

time.sleep(1000)
driver.quit()