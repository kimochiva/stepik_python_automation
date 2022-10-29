import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default="en",
                     help="Choose languages: ru, en, es")

@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption("language")
    chrome_options = Options()
    chrome_options.add_argument('--languages')
    chrome_options.add_experimental_option('prefs',
                                        {"intl.accept_languages": user_language})
    browser = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chrome_options)

    yield browser
    browser.quit()
