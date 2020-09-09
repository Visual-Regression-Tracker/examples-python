from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from visual_regression_tracker import VisualRegressionTracker, Config, TestRun

driver = webdriver.Chrome(ChromeDriverManager().install())

config = Config(
    apiUrl='http://localhost:4200',
    project='Default project',
    apiKey='M7X93CSR67MH76NNKCQ6KDQS18K8',
    branchName='develop',
    enableSoftAssert=True
)

vrt = VisualRegressionTracker(config)

with vrt:
    try:
        driver.get("http://www.python.org")
        vrt.track(TestRun(
            name='Image name',
            imageBase64=driver.get_screenshot_as_base64(),
            diffTollerancePercent=0,
            os='Mac',
            browser='Chrome',
            viewport='800x600',
            device='PC',
        ))
    finally:
        driver.quit()
