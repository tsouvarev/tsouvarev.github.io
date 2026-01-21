AUTHOR = 'Иван Цуварев'
SITENAME = 'Блог Ивана'
SITEURL = ""

PATH = "content"

TIMEZONE = 'Europe/Moscow'

DEFAULT_LANG = 'ru'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
USE_FOLDER_AS_CATEGORY = False

# Blogroll
LINKS = ()

# Social widget
SOCIAL = ()

DEFAULT_PAGINATION = False

THEME = '../pelican-themes/svbtle/'
PROFILE_IMAGE = None
INTRO = "Description you like"  
TAG_URL = 'tags/{slug}/'
TAG_SAVE_AS = 'tags/{slug}/index.html'
TAGS_URL = 'tags/'
TAGS_SAVE_AS = 'tags/index.html'
CATEGORIES_SAVE_AS = 'categories/index.html'

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

PHOTO_LIBRARY = "content"
PLUGINS = ['pin_to_top', 'tag_cloud']
PLUGIN_PATHS = ["plugins"]

MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.toc': {},
        'markdown.extensions.extra': {},  # for tables
        'markdown.extensions.def_list': {},  
    },
    'output_format': 'html5',
}
