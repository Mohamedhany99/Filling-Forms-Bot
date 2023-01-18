import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By

df = pd.read_excel("VOIS TASK.xlsx",sheet_name="Sheet1")
# print(df["Joining Date"])
df.sort_values("Joining Date",ascending = True,inplace=True)
DRIVER_PATH = "chromedriver.exe"
driver = webdriver.Chrome(executable_path=DRIVER_PATH)
driver.get("https://www.rpachallenge.com/")
driver.implicitly_wait(0.9)
driver.maximize_window()
start_button = driver.find_element(By.XPATH, '/html/body/app-root/div[2]/app-rpa1/div/div[1]/div[6]/button').click()
# print(df["First Name"])
for index,row in df.iterrows():
    # print(row["Last Name "])
    first_name = driver.find_element(By.XPATH,'//input[@ng-reflect-name="labelFirstName"]').send_keys(row["First Name"])
    last_name = driver.find_element(By.XPATH,'//input[@ng-reflect-name="labelLastName"]').send_keys(row["Last Name "])
    company_name = driver.find_element(By.XPATH,'//input[@ng-reflect-name="labelCompanyName"]').send_keys(row["Company Name"])
    role_in_company = driver.find_element(By.XPATH,'//input[@ng-reflect-name="labelRole"]').send_keys(row["Role in Company"])
    address = driver.find_element(By.XPATH,'//input[@ng-reflect-name="labelAddress"]').send_keys(row["Address"])
    email = driver.find_element(By.XPATH,'//input[@ng-reflect-name="labelEmail"]').send_keys(row["Email"])
    phone_number = driver.find_element(By.XPATH,'//input[@ng-reflect-name="labelPhone"]').send_keys(row["Phone Number"])
    driver.implicitly_wait(0.2)
    submit_buttpon = driver.find_element(By.XPATH, '/html/body/app-root/div[2]/app-rpa1/div/div[2]/form/input').click()
    
