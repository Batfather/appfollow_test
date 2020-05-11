# -*- coding: utf-8 -*-
import os

JSONIFY_PRETTYPRINT_REGULAR = True

# MONGODB SETTINGS
MONGO_URI = 'mongodb://' + os.environ['MONGODB_HOSTNAME'] + ':27017/' \
                                  + os.environ['MONGODB_DATABASE']
