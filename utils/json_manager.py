"""Utils to handle json"""

import json
import os


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RES_DIR = os.path.join(BASE_DIR, 'resources')
SETUP_PATH = '{}/setup.json'.format(RES_DIR)


def get_setup_data()-> dict:
    """Get data from setup.json file"""
    with open(SETUP_PATH) as data_file:
        data = json.load(data_file)

    return data
