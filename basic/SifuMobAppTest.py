from appium import webdriver
import time

# Step 1 : Create "Desired Capabilities"
desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '10'
desired_caps['deviceName'] = 'emulator-5554'
desired_caps['automationName'] = 'UiAutomator2'
desired_caps['app'] = ('C:/Users/Adilah/Downloads/sifu_dev_v1.0.1.apk')
desired_caps['appPackage'] = 'my.com.tmrnd.sifu'
desired_caps['appActivity'] = 'my.com.tmrnd.sifu.MainActivity'

# Step 2 : Create "Driver object"
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)

# Step 3 : "Enter Login Credentials"
# Username
ele_xpath = driver.find_element_by_xpath("//android.widget.EditText[@resource-id='username']").send_keys("sqa0001")
# Password
ele_xpath = driver.find_element_by_xpath("//android.widget.EditText[@resource-id='password']").send_keys('pass1234')
# Login btn
ele_xpath = driver.find_element_by_xpath("//android.widget.Button[@resource-id='kc-login']").click()

# Step 4 : Wait for 2 seconds
time.sleep(2)

# Step 5 : Close the driver object
driver.quit()