import json, os, time
from selenium import webdriver

dir_path = os.path.dirname(os.path.realpath(__file__))
with open(os.path.join(dir_path, 'userConfig.json')) as f:
    userConfig = json.load(f)

USERNAME = userConfig.get("username")
PASSWORD = userConfig.get("password")

USERNAME_XPATH = ''

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get('https://www.instagram.com/')

driver.find_element_by_name('username').send_keys(USERNAME)
driver.find_element_by_name('password').send_keys(PASSWORD)
driver.find_element_by_name('password').submit()

driver.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button[2]').click()

# driver.get('https://www.instagram.com/aishwarya.juhi')

imgs = driver.find_elements_by_css_selector('img.FFVAD')

imgUrls = []

for img in imgs:
    url = img.get_attribute('src')
    imgUrls.append(url)

time.sleep(5)
driver.quit()
