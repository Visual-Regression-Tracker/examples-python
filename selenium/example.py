from selenium import webdriver
from selenium.webdriver.common.by import By
from visual_regression_tracker import VisualRegressionTracker, TestRun

options = webdriver.ChromeOptions()
options.add_argument('--headless=new')
options.add_argument('--window-size=1280,1024')
driver = webdriver.Chrome(options=options)
vrt = VisualRegressionTracker()

with vrt:
    try:
        driver.get('https://the-internet.herokuapp.com/')
        vrt.track(TestRun(
            name='Home page',
            imageBase64=driver.get_screenshot_as_base64(),
        ))

        driver.find_element(By.LINK_TEXT, 'Checkboxes').click()
        vrt.track(TestRun(
            name='Checkboxes page',
            imageBase64=driver.get_screenshot_as_base64(),
            browser='Chrome',
            viewport='1280x1024',
            device='PC',
        ))
    finally:
        driver.quit()
