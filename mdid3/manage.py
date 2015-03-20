#!/usr/bin/env python
import os
import sys
from unipath import Path
try:
    import pymysql
    pymysql.install_as_MySQLdb()
except ImportError:
    pass

if __name__ == "__main__":
    sys.path.append(Path(__file__).child('contrib'))
    sys.path.append(Path(__file__).child('core'))
    sys.path.append('/var/local/mdid/rooibos/contrib')
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config")
    os.environ.setdefault("DJANGO_CONFIGURATION", "Local")

    from configurations.management import execute_from_command_line

    execute_from_command_line(sys.argv)
