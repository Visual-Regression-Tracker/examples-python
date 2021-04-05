from playwright.sync_api import sync_playwright

from visual_regression_tracker import Config, IgnoreArea
from visual_regression_tracker.playwright import PlaywrightVisualRegressionTracker, PageTrackOptions, \
    PageScreenshotOptions, Agent, ElementHandleScreenshotOptions, ElementHandleTrackOptions

playwright = sync_playwright().start()
browserType = playwright.chromium
browser = browserType.launch(headless=False)
page = browser.new_page()
page.goto('https://www.python.org/')

try:
    vrt = PlaywrightVisualRegressionTracker(browserType, None)

    with vrt:
        vrt.trackPage(page, 'Home page', PageTrackOptions(
            diffTollerancePercent=1.34,
            ignoreAreas=[
                IgnoreArea(
                    x=100,
                    y=200,
                    width=300,
                    height=400,
                )
            ],
            screenshotOptions=PageScreenshotOptions(
                full_page=True,
                omit_background=True,
            ),
            agent=Agent(
                os='OS',
                device='Device',
            )
        ))

        vrt.trackElementHandle(page.query_selector(".search-the-site"), "Search form", ElementHandleTrackOptions(
            diffTollerancePercent=1.34,
            ignoreAreas=[
                IgnoreArea(
                    x=1,
                    y=2,
                    width=30,
                    height=10,
                )
            ],
            screenshotOptions=ElementHandleScreenshotOptions(
                omit_background=True,
            ),
            agent=Agent(
                os='OS',
                device='Device',
                viewport='1200x12'
            )
        ))
finally:
    browser.close()
    playwright.stop()
