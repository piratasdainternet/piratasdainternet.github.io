#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Piratas da Internet'
SITENAME = 'Piratas da Internet'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Sao_Paulo'

DEFAULT_LANG = 'pt'

THEME = 'theme'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ('Linux Play', 'https://www.youtube.com/user/LinuxPlay0'),
    ('Eduardo Klosowski', 'https://eduardoklosowski.wordpress.com/'),
    ('Tchubirabiron', 'http://tchubs.tk/'),
    ('Hack \'n\' Cast', 'http://hackncast.org/'),
)

# Social widget
SOCIAL = (
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

PLUGIN_PATHS = ['plugins']
PLUGINS = ['pelican-podcast-feed']

PODCAST_FEED_PATH = 'podcast.rss'
