#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'phonxis'
SITENAME = 'phonxis'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Kiev'

DEFAULT_LANG = 'ru'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True


ARTICLE_URL = '{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'
PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'
CATEGORY_URL = 'category/{slug}'
CATEGORY_SAVE_AS = 'category/{slug}/index.html'
CATEGORIES_SAVE_AS = 'categories/index.html'
TAGS_SAVE_AS = 'tags/index.html'
TAG_URL = 'tag/{slug}'
TAG_SAVE_AS = 'tag/{slug}/index.html'
YEAR_ARCHIVE_SAVE_AS = '{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = '{date:%Y}/{date:%m}/index.html'
DAY_ARCHIVE_SAVE_AS = '{date:%Y}/{date:%m}/{date:%d}/index.html'
AUTHOR_SAVE_AS = ''


PLUGIN_PATHS = ['pelican-plugins',]
PLUGINS = ['sitemap', 'neighbors', 'related_posts', 'assets']

THEME = 'pelican-themes/nice-blog'
#nice-blog	semantic-ui	Flex	mg	chunk	Casper2Pelican	cid 	clean-blog
# mediumfox 	medius