# Playwright + SDK

[example.py](example.py) opens https://the-internet.herokuapp.com headless with [Playwright for Python](https://playwright.dev/python/) and tracks the full page and the heading element with the Playwright integration of [sdk-python](https://github.com/Visual-Regression-Tracker/sdk-python), with an ignore area, a diff tolerance and agent details.

## Prerequisites

- Python 3.15 or later
- A running [Visual Regression Tracker](https://github.com/Visual-Regression-Tracker/Visual-Regression-Tracker) 6.0 server and its API key

## Setup

- Copy `vrt.json.example` to `vrt.json` and set your connection, or use the [`VRT_*` environment variables](https://github.com/Visual-Regression-Tracker/sdk-python#or-as-environment-variables), which override the file
- Install dependencies: `pip install -r requirements.txt`
- Install the browser: `playwright install chromium`

## Run

```sh
python example.py
```

## What to expect

`enableSoftAssert` is on: the SDK logs a failed check instead of raising, so the script finishes and prints a link to each test run.

- First run: `No baseline` for "Home page" and "Heading". The VRT UI shows a build with two new test runs. Approve them to make them the baseline for the branch.
- Next runs: nothing is logged while the page looks the same. When it changes, `Difference found`, and the build shows the diff to approve or reject.

Set `enableSoftAssert` to `false` to make new and changed screenshots raise an error.
