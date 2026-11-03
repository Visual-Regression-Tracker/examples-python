# Visual Regression Tracker examples for Python

Each folder is a separate project with its own `requirements.txt`, `vrt.json.example` and README, on [sdk-python](https://github.com/Visual-Regression-Tracker/sdk-python) 5.0.0 from PyPI and Python 3.15 or later. The examples open https://the-internet.herokuapp.com headless and track screenshots in a [Visual Regression Tracker](https://github.com/Visual-Regression-Tracker/Visual-Regression-Tracker) 6.0 server.

| Example                  | Stack                                        | Client                                                                                                      |
| ------------------------ | -------------------------------------------- | ----------------------------------------------------------------------------------------------------------- |
| [playwright](playwright) | Playwright, the SDK's Playwright integration | [sdk-python](https://github.com/Visual-Regression-Tracker/sdk-python#integration-with-microsoft-playwright) |
| [selenium](selenium)     | Selenium 4                                   | [sdk-python](https://github.com/Visual-Regression-Tracker/sdk-python)                                       |

The examples connect with `vrt.json` or `VRT_*` environment variables, the way [sdk-python reads its configuration](https://github.com/Visual-Regression-Tracker/sdk-python#configure-connection). `vrt.json.example` holds the URL, API key and project of a fresh local install; copy it to `vrt.json` and change what differs.

CI runs every example against a VRT server started from [.github/vrt/docker-compose.yml](.github/vrt/docker-compose.yml).
