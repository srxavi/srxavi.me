#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Xavi Francisco'
SITENAME = u"Xavi's non-euclidean space"
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('About', '#'),
         ('Projects', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
STATIC_PATHS = ['images']

THEME = 'Flex'

# Theme related stuff

SITELOGO = 'images/me.jpg'
ROBOTS = 'index, follow'
COPYRIGHT_YEAR = 2015
CC_LICENSE = {
    'name': 'Creative Commons Attribution-ShareAlike',
    'version': '4.0',
    'slug': 'by-sa'
}

SOCIAL = (
    ('linkedin', 'https://es.linkedin.com/in/xavifrancisco'),
    ('github', 'https://github.com/srxavi'),
    ('google', 'https://plus.google.com/+XaviFrancisco'))
