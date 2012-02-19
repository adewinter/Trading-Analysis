#!/usr/bin/env python
import os
from django.core.management import execute_manager
import imp
try:
    imp.find_module('settings') # Assumed to be in the same directory.
except ImportError:
    import sys
    sys.stderr.write("Error: Can't find the file 'settings.py' in the directory containing %r. It appears you've customized things.\nYou'll have to run django-admin.py, passing it your settings module.\n" % __file__)
    sys.exit(1)

import settings
import sys
print 'INSERTING THE FOLLOWING INTO PYTHONPATH'
up_level = os.path.split(os.path.abspath(__file__))[0]
print up_level
sys.path.insert(0,up_level)
up_level = os.path.split(up_level)[0]
print up_level
sys.path.insert(0, up_level)


if __name__ == "__main__":
    execute_manager(settings)
