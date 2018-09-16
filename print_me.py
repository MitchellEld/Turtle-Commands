from selenium import webdriver
driver = webdriver.Chrome()
driver.get('https://aggieprint.tamu.edu/myprintcenter/')

username_box = driver.find_element_by_id('input-login-username')
username_box.send_keys('mitcheld')

password_box = driver.find_element_by_id('input-login-password')
password_box.send_keys('password')

driver.find_element_by_xpath("//form[@id='form-login']/button[@type='submit']").click()

driver.implicitly_wait(30)
uploadElement = driver.find_element_by_name("Content")
#print(uploadElement.get_property('attributes')[0])
uploadElement.send_keys("C:\\Users\\Mitchell\\Documents\\git\\Turtle-Commands\\requirements.txt")