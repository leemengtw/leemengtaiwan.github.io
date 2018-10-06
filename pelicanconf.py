#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Lee Meng'
SITENAME = "LeeMeng"
SITETITLE = 'All About DataScience'
SITEURL = ''
SITE_DESCRIPTION_LIST = [
    "現居東京的資料科學家 L 在數據世界裡頭的所想、所學以及所感。這個網站紀錄了所有我的個人資訊，包含工作經歷、",
    "做過的專案以及與資料科學相關的文章。透過分享自己的學習心得以及業界經驗，我希望能讓更多人接觸到資料科學的奧秘。",
    "此部落格主要會提及資料科學、資料工程、機器學習及資料視覺化技巧。"
]
SITE_DESCRIPTION = "".join(SITE_DESCRIPTION_LIST)

SITE_KEYWORDS = "部落格, 資料科學, Python, R, 機器學習, 資料分析, 資料視覺化, 軟體工程, 資料工程, 雲端運算, 台灣, blog, data science, machine learning, data analysis, data visualization, data engineering, taiwan"
PATH = 'content'

# Set path for stat files like favicon and robot.txt
STATIC_PATHS = [
    'images',
    'Udacity/Deep Learning/images',
    'extra/robots.txt',
    'extra/favicon.ico',
    'extra/.htaccess',
    'extra/CNAME'
]

EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/favicon.ico': {'path': 'favicon.ico'},
    'extra/.htaccess': {'path': '.htaccess'},
    'extra/CNAME': {'path': 'CNAME'}
}

# Use draft as default for preventing publish unfinished articles.
# Note that we then have to set Status field to "published" for every draft that
# we want to published
# DEFAULT_METADATA = {
#     'status': 'draft',
# }


TIMEZONE = 'Asia/Tokyo'
DEFAULT_LANG = 'zh-hant-tw'
DATE_FORMATS = {
    'zh-hant-tw': '%Y-%m-%d (%a)',
    'en': ('en_US','%a, %d %b %Y'),
    'jp': ('ja_JP','%Y-%m-%d(%a)'),
}

# Url settings
# ARTICLE_URL = 'posts/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
# ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%m}/{date:%d}/{slug}.html'


# Feed generation is usually not desired when developing
# FEED_DOMAIN = SITEURL
# FEED_ALL_RSS = 'feeds/all.rss.xml'
#
# FEED_ALL_ATOM = None
# CATEGORY_FEED_ATOM = None
# TRANSLATION_FEED_ATOM = None
# AUTHOR_FEED_ATOM = None
# AUTHOR_FEED_RSS = None

# github settings
# GITHUB_URL = "https://github.com/leemengtaiwan"

# Google custom sea
SEARCH_BOX = True


# Blogroll
# LINKS = (('Github', 'https://github.com/leemengtaiwan'),
#          ('You can modify those links in your config file', '#'),)

# Social contact/link
GITHUB = 'https://github.com/leemengtaiwan'
LINKEDIN = 'https://www.linkedin.com/in/leemeng1990/'
INSTAGRAM = 'https://www.instagram.com/leemengtaiwan/'
FACEBOOK = 'https://www.facebook.com/LeeMengTaiwan'
MAIL = 'mailto:b9875001@gmail.com'

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# enable Pelican to use plugins for additional features
MARKUP = ('md', 'ipynb')
PLUGIN_PATHS = ['/Users/meng.lee/git/blog/pelican-plugins']
PLUGINS = ['pelican-ipynb.markup', 'pelican-toc']
IGNORE_FILES = ['.ipynb_checkpoints']
IPYNB_USE_METACELL = True

TOC = {
    'TOC_HEADERS'       : '^h[1-6]', # What headers should be included in
                                     # the generated toc
                                     # Expected format is a regular expression

    'TOC_RUN'           : 'true',    # Default value for toc generation,
                                     # if it does not evaluate
                                     # to 'true' no toc will be generated

    'TOC_INCLUDE_TITLE': 'true',     # If 'true' include title in toc
}


# Jinja extensions
JINJA_ENVIRONMENT = {
    'extensions': ['jinja2.ext.loopcontrols']
}

# Pagination
# https://github.com/getpelican/pelican/blob/master/docs/settings.rst#pagination
DEFAULT_PAGINATION = 11
NUM_TOP_TAGS = 5
NUM_ARTICLES_HOMEPAGE = 4
# PAGINATION_PATTERNS = (
#     (1, '{base_name}/', '{base_name}/index.html'),
#     (2, '{base_name}/page/{number}/', '{base_name}/page/{number}/index.html'),
# )

# Tell pelican-ipynb plugin to use the native meta data specified inside of notebook
# instead of .ipynb-meta files
IPYNB_USE_META_SUMMARY = False
IPYNB_IGNORE_CSS = True
STATIC_CHECK_IF_MODIFIED = True

# Use sub-folder as categories
USE_FOLDER_AS_CATEGORY = True
DEFAULT_CATEGORY = 'Miscellaneous'


# Pelican default theme for dev
THEME = "/Users/meng.lee/git/blog/pelican-jupyter-notebook/themes/Hola10"
# DIRECT_TEMPLATES = ['index', 'tags', 'categories', 'authors', 'archives', 'blog', 'search', 'blog-dev']
DIRECT_TEMPLATES = ['index', 'tags', 'categories', 'authors', 'archives', 'blog', 'search']
# PAGINATED_DIRECT_TEMPLATES = ['index', 'blog', 'blog-dev']
PAGINATED_DIRECT_TEMPLATES = ['index', 'blog']

# Copy notebook to output folder for downloading
# reference: `ARTICLE_SAVE_AS` in http://docs.getpelican.com/en/3.6.3/settings.html
IPYNB_NB_SAVE_AS = 'notebooks/{slug}.ipynb'

# Email receiving setting
EMAIL_FORM_ACTION = "https://formspree.io/b98705001@gmail.com"


# Portfolio setting, order matters
PROJECTS = [
    {
        "name": "貓咪辨識 App",
        "thumb": "cat-recognizer",
        "categories": "TensorFlow, Flask, Docker, Heroku",
        "link": "https://github.com/leemengtaiwan/cat-recognition-app",
        "description": '這是一個利用 TensorFlow 以及 Flask 來分辨貓咪以及狗狗的圖片辨識應用，使用 Docker 封裝並部署在 Heroku 上。你可以前往 <a href="https://github.com/leemengtaiwan/cat-recognition-app" target="_blank">Github</a> 查看細節。'
    },
    {
        "name": "Gist x Evernote 同步工具",
        "thumb": "gist-evernote",
        "categories": "Selenium, Github GraphQL, Evernote Python SDK",
        "link": "https://github.com/leemengtaiwan/gist-evernote",
        "description": '這是一個利用 Selenium 將 Github Gists 同步到 Evernote 的生產工具。你可以在 <a href="https://github.com/leemengtaiwan/gist-evernote" target="_blank">Github</a> 查看細節。'
    },
    {
        "thumb": "salad"
    },
    {
        "name": "漫畫連載通知 App",
        "thumb": "airflow-comic",
        "categories": "Airflow, Selenium, Slack",
        "link": "https://leemeng.tw/a-story-about-airflow-and-data-engineering-using-how-to-use-python-to-catch-up-with-latest-comics-as-an-example.html",
        "link_title": "專案介紹連結",
        "description": '這是一個透過 Airflow 以及 Slack 來通知最新漫畫連載的 App。你可以在我的部落格文章<a href="https://leemeng.tw/a-story-about-airflow-and-data-engineering-using-how-to-use-python-to-catch-up-with-latest-comics-as-an-example.html">一段 Airflow 與資料工程的故事：談如何用 Python 追漫畫連載</a>了解細節，或者直接去 <a href="https://github.com/leemengtaiwan/airflow-tutorials" target="_blank">Github</a> 查看程式碼。'
    },
    {
        "thumb": "lighthouse"
    },
    {
        "thumb": "woodcraft"
    },
    {
        "thumb": "shutterbug"
    },
    {
        "thumb": "minimalismo"
    },

]