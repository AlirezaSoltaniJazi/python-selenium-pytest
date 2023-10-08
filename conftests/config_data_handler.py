import json

from pytest import fixture

from utils.logger_formatter import LOGGER
from utils.project_directory_finder import get_project_directory


@fixture(scope='session')
def get_data_from_config():
    directory = get_project_directory()
    file_address = directory + '/config.json'
    with open(file_address, encoding='utf-8') as file_name:
        config_data = json.load(file_name)
        LOGGER.info('Config data', extra={'Config File Data': config_data})
    config_data['browser'] = config_data['browser'].lower()
    browser_name = config_data['browser']
    implicit_wait_state = config_data['active_implicit_wait']
    implicit_wait = config_data['implicit_wait']
    if browser_name not in ['headless chrome', 'firefox', 'chrome', 'safari', 'edge']:
        raise TypeError(f'Browser {browser_name} is not supported!')
    if not isinstance(implicit_wait_state, bool):
        raise ValueError(
            f'The implicit wait state {implicit_wait_state} must be a boolean'
        )
    if not isinstance(implicit_wait, int):
        raise ValueError(f'The implicit wait time {implicit_wait} must be an integer')
    if implicit_wait < 0:
        raise ValueError(f'The implicit wait time must be greater than {implicit_wait}')
    return config_data
