#!/usr/bin/python3.6
import sys
import logging
import site


logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/var/www/testapp/")


from app import app as application

application.secret_key = 'Add your secret key'
