import os,sys

'''
执行脚本
'''

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from core import core
from conf import my_log_settings

if __name__ == '__main__':
    my_log_settings.load_my_logging_cfg()
    core.run()
