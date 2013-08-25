""" Settings for peer-edit """

import os
from .base import *

env = get_env_setting("HOST_ENV")
if env == "development":
	from development import *
elif env == "production":
	from production import *
elif env == "staging":
	from test import *
else:
	print "Env not recognized:", env

DEBUG=True