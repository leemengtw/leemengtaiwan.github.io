#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

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

BLOG_DESCRIPTION_LIST = [
    "不只是資料科學家，處在資訊時代的各行各業都需要能活用資料科學的人才。",
    "透過分享自己的學習心得以及業界經驗，我希望讓更多人接觸到資料科學的奧秘。",
    "部落格主要會提及資料科學、資料工程、機器學習及資料視覺化技巧。"
]
BLOG_DESCRIPTION = "".join(BLOG_DESCRIPTION_LIST)

BOOK_DESCRIPTION_LIST = [
    "這邊記錄了那些為我的生活以及思考帶來不少影響的著作，推薦給你，也方便提醒自己隨時反思咀嚼。",
    "一個人的想法、價值觀、乃至思考方式都深深地受到那些他 / 她平常接觸的書籍與著作影響。",
    "這些「精神糧食」充實我們的內在，讓我們成為更好的人。"
]
BOOK_DESCRIPTION = "".join(BOOK_DESCRIPTION_LIST)

SITE_KEYWORDS = "部落格, 資料科學, 數據科學, Python, R, 機器學習, 資料分析, 深度學習, 資料視覺化, 軟體工程, 資料工程, 雲端運算, 台灣, blog, data science, machine learning, deep learning, data analysis, data visualization, data engineering, taiwan, tensorflow, tensorflow.js, keras, pytorch, transformer, bert, gpt"
PATH = "working_content"

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
PLUGIN_PATHS = ['/Users/meng.lee/Documents/workspace/pelican-plugins']
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
THEME = "/Users/meng.lee/Documents/workspace/pelican-jupyter-notebook/themes/Hola10"
DIRECT_TEMPLATES = ['index', 'tags', 'categories', 'authors', 'archives', 'blog', 'search', 'books']
PAGINATED_DIRECT_TEMPLATES = ['index', 'blog']


# Copy notebook to output folder for downloading
# reference: `ARTICLE_SAVE_AS` in http://docs.getpelican.com/en/3.6.3/settings.html
IPYNB_NB_SAVE_AS = 'notebooks/{slug}.ipynb'

# Email receiving setting
EMAIL_FORM_ACTION = "https://formspree.io/xpzjnzdg"

# Portfolio setting, order matters
PROJECTS = []


# ignore node modules from tfjs applications
IGNORE_FILES = [
    'node_modules',
    'yarn.lock',
    '.ipynb_checkpoints',
    'tfjs-apps',
]

# left navigation image information for all articles
# left_nav_image_id: img info
LEFT_NAV_IMAGES = {
    "transformer": {
        "name": "Transformer 架構圖",
        "id": "transformer",
        "filename": "transformer.jpg",
        "style": "background-color:white"
    }

}