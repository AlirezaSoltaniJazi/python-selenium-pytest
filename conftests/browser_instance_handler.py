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
    browser_args = {}
    if browser_name == browsers_headless['chrome_h']:
        browser_name = 'chrome'
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        browser_args['options'] = options
    browser_instance = browsers[browser_name](**browser_args)
    if implicit_wait_state:
        browser_instance.implicitly_wait(implicit_wait)
    yield browser_instance
    browser_instance.quit()
