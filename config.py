import os

PORT = 8000
DEMOS_PATH = os.getcwd() + "/static/demos/"

try:
    from dev_config import *
except ImportError:
    pass
