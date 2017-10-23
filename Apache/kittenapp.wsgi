#/usr/bin/env python

import os
import sys
import site

# Add the site-packages of the chosen virtualenv to work with
site.addsitedir('/root/.virtualenvs/cats/local/lib/python2.7/site-packages')

# Add the app's directory to the PYTHONPATH
sys.path.append('/opt/interview/')
#sys.path.append('/opt/interview/kitten_counter/')

# Activate your virtual env
activate_env=os.path.expanduser("/root/.virtualenvs/cats/bin/activate_this.py")
execfile(activate_env, dict(__file__=activate_env))

from kitten_counter.app import app as application
