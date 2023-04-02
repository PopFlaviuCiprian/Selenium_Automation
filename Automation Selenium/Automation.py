from selenium.webdriver import Chrome
from time import sleep
from selenium.webdriver.common.by import By

driver = Chrome()
driver.get("http://www.theTestingWorld.com/testings")
driver.maximize_window()
driver.implicitly_wait(10)


driver.find_element(By.NAME, "fld_username").send_keys("Test")
driver.find_element(By.XPATH, "//input[@name='fld_email']").send_keys("automation@gmail.com")
driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys("Testpass")
driver.find_element(By.NAME, "fld_cpassword").send_keys("Testpass")
driver.find_element(By.NAME, "fld_username").clear()
driver.find_element(By.NAME,'fld_username').send_keys("Cipri")
driver.find_element(By.XPATH, "//input[@value='home']").click()
driver.find_element(By.NAME, "sex").click()
driver.find_element(By.XPATH, "//input[@type='checkbox']").click()
driver.find_element(By.XPATH, "//input[@value='Sign up']").click()
driver.find_element(By.LINK_TEXT, "Read Detail").click()
driver.find_element(By.LINK_TEXT, "X").click()


