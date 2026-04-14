#! /usr/bin/env python

__author__ = 'iped'
import os
os.environ['ETS_TOOLKIT'] = 'qt'
from view.pyloc import PylocControl
import yaml

if __name__ == '__main__':
    with open(os.path.join(os.path.dirname(__file__), 'config.yml'), encoding='utf-8') as f:
        config = yaml.safe_load(f)
    controller = PylocControl(config)
    controller.exec_()
