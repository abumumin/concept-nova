import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
#from selenium.webdriver.support.select import Select

#from selenium.webdriver.common.by import By

class DemoFindElementByID():
    def locate_by_id_demo(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get('https://concept-nova.com/')
        driver.maximize_window()
        time.sleep(5)
        driver.find_element_by_xpath("//span[normalize-space()='About Us']").click()
        time.sleep(2)
        driver.find_element_by_xpath("//div[@class='col-3 d-none d-md-block']//a[normalize-space()='Our People']"). click()
        time.sleep(2)
        driver.find_element_by_xpath("//div[@class='col-3 d-none d-md-block']//a[normalize-space()='Join Us']").click()
        time.sleep(2)
        driver.find_element_by_xpath("//span[@class='d-none d-md-block']").click()
        time.sleep(2)
        driver.find_element_by_xpath("//input[@placeholder='Name (required)']").send_keys('Benjamin Franklin')
        time.sleep(2)
        driver.find_element_by_xpath("//input[@placeholder='Email (required)']").send_keys('abcd.23@xyx.com')
        time.sleep(2)
        driver.find_element_by_xpath("//input[@placeholder='Phone Number (required)']").send_keys('+2348011111112')
        time.sleep(2)
        driver.find_element_by_xpath("//input[@placeholder='Company Name']").send_keys('Nigerian Eyes')
        time.sleep(2)
        driver.find_element_by_xpath("//select[@name='partnership_type']").click()
        time.sleep(1)
        
        driver.find_element_by_xpath("//section[@class='container-fluid']//b[1]")
        dro=Select(driver.find_element_by_xpath("//section[@class='container-fluid']//b[1]"))
        time.sleep(2)
        dro.select_by_visible_text('Franchise')
        time.sleep(2)
        driver.find_element_by_name("comment").send_keys('I like the platform')
        time.sleep(3)
        
        driver.find_element_by_xpath("//textarea[@placeholder='Comment (required)']").send_keys('')
                
                
                
                
                
                
        #driver.find_element_by_xpath("//a[normalize-space()='Login / Signup']").click()
        # driver.find_element_by_css_selector('body > div:nth-child(2) > div:nth-child(1) > section:nth-child(1) > div:nth-child(5) > nav:nth-child(1) > div:nth-child(3) > div:nth-child(1) > div:nth-child(2) > div:nth-child(5) > a:nth-child(1)').click
        #time.sleep(1)
        #driver.find_element_by_css_selector('#username').send_keys('zeepapka@gmail.com')
        #time.sleep(1)
        #driver.find_element_by_css_selector('#password').send_keys('kwadu12@')
        #time.sleep(1)
        #driver.find_elements_by_class_name('_0a08a_3czMG _988cf_1aDdJ').click()
        #time.sleep(10)

        time.sleep(5)
        driver.minimize_window()
        driver.quit()
findbyid = DemoFindElementByID()
findbyid.locate_by_id_demo()