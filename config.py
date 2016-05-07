import os

PORT = 1338
DEMOS_PATH = os.getcwd() + "/static/demos/"

try:
    from dev_config import *
except ImportError:
    pass
