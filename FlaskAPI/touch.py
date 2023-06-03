# -*- coding: utf-8 -*-
"""
Created on Fri Jun  2 21:52:21 2023

@author: otusa
"""

import os

def touch_file(filename):
    with open(filename, 'a'):
        os.utime(filename, None)

filename = 'wsgi.py'  # Replace with your desired filename
touch_file(filename)
