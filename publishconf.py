#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

SITEURL = 'https://leemeng.tw'
RELATIVE_URLS = False

# Parse content and save as JSON for searching
PLUGINS += ['tipue_search', 'ga_page_view', 'sitemap', 'share_post']
PLUGINS = list(set(PLUGINS))


# Feeds
FEED_DOMAIN = SITEURL
FEED_ALL_RSS = 'feeds/all.rss.xml'
FEED_ALL_ATOM = 'feeds/all.atom.xml'
# CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'

DELETE_OUTPUT_DIRECTORY = True

# Following items are often useful when publishing

DISQUS_SITENAME = "leemengtaiwan"
DISQUS_SECRET_KEY = '5VlHrNMlpJ9f6wKT3nSC3O1lVKYlUetlB9a0eFaqXYqRII2LJWTjsdxeBF4m54Bb'
DISQUS_PUBLIC_KEY = '4aHNPuCwkVqbu7Mzn7VYoiJh39hV0kIUAgdfAgyiIY9U4VQsJqdQgPiFdxujTsNf'

GOOGLE_ANALYTICS = "UA-106559980-1"


# Sitemap settings
SITEMAP = {
    "format": "xml",
    "priorities": {
        "articles": 0.7,
        "indexes": 0.5,
        "pages": 0.3,
    },
    "changefreqs": {
        "articles": "always",
        "indexes": "hourly",
        "pages": "monthly",
    }
}

# Google Page View Plugin setting
# Reference: https://github.com/jhshi/pelican.plugins.ga_page_view
GOOGLE_SERVICE_ACCOUNT = 'blog-usage@blog-usage.iam.gserviceaccount.com'
GOOGLE_KEY_FILE = './Blog-usage-0799d847dd8f.p12'
GA_START_DATE = '2017-10-01'
GA_END_DATE = 'today'
GA_METRIC = 'ga:pageviews'
POPULAR_POST_START = 'A month ago'