#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import pandas as pd

# Pelican setting start below
# --------------------------
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

SITE_KEYWORDS = "部落格, 資料科學, 數據科學, Python, R, 機器學習, 資料分析, 深度學習, 資料視覺化, 軟體工程, 資料工程, 雲端運算, 台灣, blog, data science, machine learning, deep learning, data analysis, data visualization, data engineering, taiwan, tensorflow, tensorflow.js, keras"
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
    'en': ('en_US', '%a, %d %b %Y'),
    'jp': ('ja_JP', '%Y-%m-%d(%a)'),
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

# Pagination Patterns
# http://docs.getpelican.com/en/stable/settings.html?highlight=PAGINATION_PATTERNS#using-pagination-patterns
PAGINATION_PATTERNS = (
    (1, '{url}', '{save_as}'),
    (2, '{base_name}/{number}/', '{base_name}/{number}/index.html'),
)

# Tell pelican-ipynb plugin to use the native meta data specified inside of notebook
# instead of .ipynb-meta files
IPYNB_USE_META_SUMMARY = False
IPYNB_IGNORE_CSS = True
IPYNB_SKIP_CSS = True
STATIC_CHECK_IF_MODIFIED = True

# Use sub-folder as categories
USE_FOLDER_AS_CATEGORY = True
DEFAULT_CATEGORY = 'Miscellaneous'


# Pelican default theme for dev
THEME = "/Users/meng.lee/git/blog/pelican-jupyter-notebook/themes/Hola10"
DIRECT_TEMPLATES = ['index', 'tags', 'categories', 'authors', 'archives', 'blog', 'search', 'books']
# DIRECT_TEMPLATES = ['index', 'tags', 'categories', 'authors', 'archives', 'blog', 'search']
# PAGINATED_DIRECT_TEMPLATES = ['index', 'blog', 'books']
PAGINATED_DIRECT_TEMPLATES = ['index', 'blog']

# Copy notebook to output folder for downloading
# reference: `ARTICLE_SAVE_AS` in http://docs.getpelican.com/en/3.6.3/settings.html
IPYNB_NB_SAVE_AS = 'notebooks/{slug}.ipynb'

# Email receiving setting
EMAIL_FORM_ACTION = "https://formspree.io/b98705001@gmail.com"

# Portfolio setting, order matters
PROJECTS = [
    {
        "name": "GapMinder 中文版",
        "thumb": "gapminder",
        "categories": "利用公開數據來探索全世界以及台灣的動態資料視覺化工具",
        "link": "https://leemeng.tw/gapminder.html",
        "link_title": "專案介紹連結",
        "description": '這是一個利用各國公開數據來探索世界以及台灣的資料視覺化工具。你可以在<a href="https://leemeng.tw/gapminder.html">如何用 30 秒了解台灣發展與全球趨勢：用 GapMinder 培養正確世界觀</a>實際使用此工具並了解細節'
    },
    {
        "name": "由淺入深的 AI 與深度學習資源",
        "thumb": "deep-learning-resources",
        "categories": "大量優質的 AI 與深度學習的線上資源，適合各個學習階段的你進一步探索",
        "link": "https://leemeng.tw/deep-learning-resources.html",
        "link_title": "專案介紹連結",
        "description": '我將線上的深度學習資源做些整理並逐一介紹。你可以在<a href="https://leemeng.tw/deep-learning-resources.html">由淺入深的深度學習資源整理</a>了解細節，或者直接去專屬的 <a href="https://github.com/leemengtaiwan/deep-learning-resources" target="_blank">Github Repo</a> 關注並查看所有資源。'
    },
    {
        "name": "AI 如何找出你的喵",
        "thumb": "cat-recognizer",
        "categories": "一個利用 TensorFlow 以及 Flask 實做的貓狗辨識應用",
        "link": "https://demo.leemeng.tw/",
        "description": '這是一個利用 TensorFlow 以及 Flask 來分辨貓咪以及狗狗的圖片辨識應用，使用 Docker 封裝並部署在 Heroku 上。你可以閱讀 <a href="https://demo.leemeng.tw/" target="_blank">AI 如何找出你的喵：直觀理解卷積神經網路</a> 來了解細節並實際使用該神經網路。'
    },
    {
        "name": "用 CartoonGAN 畫日本動漫",
        "thumb": "cartoongan",
        "categories": "讓任何人都可以使用對抗生成網路 GAN 來生成動漫的一個 TensorFlow 2 專案",
        "link": "https://leemeng.tw/generate-anime-using-cartoongan-and-tensorflow2.html",
        "link_title": "專案介紹連結",
        "description": '閱讀<a href="https://leemeng.tw/generate-anime-using-cartoongan-and-tensorflow2.html">用 CartoonGAN 及 TensorFlow 2 生成新海誠與宮崎駿動畫</a>或前往 <a href="https://github.com/mnicnc404/CartoonGan-tensorflow" target="_blank">Github</a> 了解細節。'
    },
    {
        "name": "漫畫連載通知 App",
        "thumb": "airflow-comic",
        "categories": "透過 Airflow 以及 Slack 來通知最新漫畫連載的應用",
        "link": "https://leemeng.tw/a-story-about-airflow-and-data-engineering-using-how-to-use-python-to-catch-up-with-latest-comics-as-an-example.html",
        "link_title": "專案介紹連結",
        "description": '這是一個透過 Airflow 以及 Slack 來通知最新漫畫連載的 App。你可以在<a href="https://leemeng.tw/a-story-about-airflow-and-data-engineering-using-how-to-use-python-to-catch-up-with-latest-comics-as-an-example.html">一段 Airflow 與資料工程的故事：談如何用 Python 追漫畫連載</a>了解細節，或者直接去 <a href="https://github.com/leemengtaiwan/airflow-tutorials" target="_blank">Github</a> 查看程式碼。'
    },
    {

        "name": "Gist x Evernote 同步工具",
        "thumb": "gist-evernote",
        "categories": "利用 Selenium 將 Github Gists 同步到 Evernote 的生產工具",
        "link": "https://github.com/leemengtaiwan/gist-evernote",
        "description": '這是一個利用 Selenium 將 Github Gists 同步到 Evernote 的生產工具。你可以在 <a href="https://github.com/leemengtaiwan/gist-evernote" target="_blank">Github</a> 查看細節。'
    },
    {
        "name": "天龍八部小說生成器",
        "thumb": "text-generation",
        "categories": "利用 TensorFlow 2.0 及 TensorFlow.js 生成似真似假的武俠小說",
        "link": "https://leemeng.tw/how-to-generate-interesting-text-with-tensorflow2-and-tensorflow-js.html",
        "link_title": "文章連結",
        "description": '展示一個由 TensorFlow 2.0 以及 TensorFlow.js 實現的線上文本生成應用。你可以前往<a href="https://leemeng.tw/how-to-generate-interesting-text-with-tensorflow2-and-tensorflow-js.html" target="_blank">讓 AI 寫點金庸：如何用 TensorFlow 2.0 及 TensorFlow.js 寫天龍八部</a>了解詳情。'
    },
    {
        "thumb": "minimalismo"
    },

]

# get book information for books.html
BOOKS = pd.read_csv(PATH + '/additional_content/books/books.csv').fillna('').to_dict('records')
print('Done: Processed {} books.'.format(len(BOOKS)))

# ignore node modules from tfjs applications
IGNORE_FILES = [
    'node_modules',
    'yarn.lock',
    '.ipynb_checkpoints'
]

# left navigation image information for all articles
# TODO: 把相關的圖（scaled attn, multi head ...）弄成一張
LEFT_NAV_IMAGES = {
    "transformer": {
        "name": "Transformer 架構圖",
        "id": "transformer",
        "filename": "transformer.jpg",
        "style": "background-color:white"
    }
}



# get news feed
# NEWS_FEEDS = pd.read_csv(PATH + '/additional_content/news-feed/news-feed.csv').fillna('').to_dict('records')
# print('Done: Processed {} news feeds.'.format(len(NEWS_FEEDS)))

# local ga test
# PLUGINS += ['ga_page_view']
# GOOGLE_SERVICE_ACCOUNT = 'blog-usage@blog-usage.iam.gserviceaccount.com'
# GOOGLE_KEY_FILE = './Blog-usage-0799d847dd8f.p12'
# GA_START_DATE = '2017-10-01'
# GA_END_DATE = 'today'
# GA_METRIC = 'ga:pageviews'
# POPULAR_POST_START = 'A month ago'




