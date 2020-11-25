from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from visual_regression_tracker import VisualRegressionTracker, Config, TestRun

driver = webdriver.Chrome(ChromeDriverManager().install())

config = Config(
    apiUrl='http://localhost:4200',
    project='Default project',
    apiKey='9JEA4NS8YRMTTEHJVP16XTZ5S7AM',
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
