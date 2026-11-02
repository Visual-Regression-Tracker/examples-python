# Selenium + SDK

[example.py](example.py) opens https://the-internet.herokuapp.com in headless Chrome with [Selenium](https://www.selenium.dev/documentation/webdriver/) and tracks two screenshots with [sdk-python](https://github.com/Visual-Regression-Tracker/sdk-python), the second with browser, viewport and device details.

## Prerequisites

- Python 3.11 or later
- Google Chrome; Selenium Manager downloads a matching chromedriver
- A running [Visual Regression Tracker](https://github.com/Visual-Regression-Tracker/Visual-Regression-Tracker) 6.0 server and its API key

## Setup

- Copy `vrt.json.example` to `vrt.json` and set your connection, or use the [`VRT_*` environment variables](https://github.com/Visual-Regression-Tracker/sdk-python#or-as-environment-variables), which override the file
- Install dependencies: `pip install -r requirements.txt`

## Run

```sh
python example.py
```

## What to expect

`enableSoftAssert` is on: the SDK logs a failed check instead of raising, so the script finishes and prints a link to each test run.

- First run: `No baseline` for "Home page" and "Checkboxes page". The VRT UI shows a build with two new test runs. Approve them to make them the baseline for the branch.
- Next runs: nothing is logged while the pages look the same. When one changes, `Difference found`, and the build shows the diff to approve or reject.

Set `enableSoftAssert` to `false` to make new and changed screenshots raise an error.
