#!C:\Users\Harish\AppData\Local\Programs\Python\Python37\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'OreoML==1.0.0','console_scripts','oreoml_train'
__requires__ = 'OreoML==1.0.0'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('OreoML==1.0.0', 'console_scripts', 'oreoml_train')()
    )
