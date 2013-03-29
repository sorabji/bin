

#!/usr/local/bin/python
# This must be saved in same directory as pyp and named PypCustom.py

import optparse
import sys
import os
import time
import json
import glob
import tempfile
import datetime

class Colors(object):
    OFF = chr(27) + '[0m'
    RED = chr(27) + '[31m'
    GREEN = chr(27) + '[32m'
    YELLOW = chr(27) + '[33m'
    MAGENTA = chr(27) + '[35m'
    CYAN = chr(27) + '[36m'
    WHITE = chr(27) + '[37m'
    BLUE = chr(27) + '[34m'
    BOLD = chr(27) + '[1m'
    COLORS = [OFF, RED, GREEN, YELLOW, MAGENTA, CYAN, WHITE, BLUE, BOLD]

class PypCustom(object):
    'modify below paths to set macro paths'
    def __init__(self):
        self.user_macro_path = os.path.expanduser('~')+ '/config/bin/pyp_user_macros.json'
        self.group_macro_path = os.path.expanduser('~')+ '/config/bin/pyp_user_macros.json'

class PowerPipeListCustom():
    'this is used for pp functions (list fuctions like sort)'
    def __init__(self, *args):
        pass
    
    def test(self):
        print 'test' #pp.test() will print "test"


class PypStrCustom():   
    'this is used for string functions'
    def __init__(self, *args):
        pass
    
    def test(self):
        print 'test' #p.test() will print "test" is p is a str
    
    
class PypListCustom():
    def __init__(self, *args):
        pass

    def test(self):
        print 'test' #p.test() will print "test" is p is a list broken up from a str

class PypFunctionCustom(object):
    'this is used for custom functions and variables (non-instance)'
    test_var = 'works'
    
    def __init__(self, *args):
        pass
    
    def test(self):
        print 'working func '  + self

