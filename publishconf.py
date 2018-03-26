#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

SITEURL = 'https://leemengtaiwan.github.io'
RELATIVE_URLS = False

FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'

DELETE_OUTPUT_DIRECTORY = True

# Following items are often useful when publishing

DISQUS_SITENAME = "leemengtaiwan"
DISQUS_SECRET_KEY = '5VlHrNMlpJ9f6wKT3nSC3O1lVKYlUetlB9a0eFaqXYqRII2LJWTjsdxeBF4m54Bb'
DISQUS_PUBLIC_KEY = '4aHNPuCwkVqbu7Mzn7VYoiJh39hV0kIUAgdfAgyiIY9U4VQsJqdQgPiFdxujTsNf'

GOOGLE_ANALYTICS = "UA-106559980-1"
