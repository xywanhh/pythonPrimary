import configparser

"""
自定义的模块与包
"""

def read(config_file):
    config=configparser.ConfigParser()
    config.read(config_file)
    return config