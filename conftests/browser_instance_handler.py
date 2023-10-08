from pytest import fixture

from selenium import webdriver


@fixture
def browser(config):
    browser_name = config['browser']
    implicit_wait_state = config['active_implicit_wait']
    implicit_wait = config['implicit_wait']
    browsers = {
        'firefox': webdriver.Firefox,
        'chrome': webdriver.Chrome,
        'safari': webdriver.Safari,
        'edge': webdriver.Edge,
    }
    browsers_headless = {'chrome_h': 'headless chrome'}
    if browser_name == browsers_headless['chrome_h']:
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        browser_instance = webdriver.Chrome(options=options)
    else:
        browser_instance = browsers[browser_name]()
    if implicit_wait_state:
        browser_instance.implicitly_wait(implicit_wait)
    yield browser_instance
    browser_instance.quit()
