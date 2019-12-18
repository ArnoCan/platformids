# -*- coding: utf-8 -*-
"""Custom configuration of *conf.py*.
to be appended to the file:
    ::

        ${BUILDDIR}/apidoc/sphinx/conf.py

"""

import sys
import os
import sphinx

from distutils.version import LooseVersion

#
# running on read-the-docs
#
on_rtd = os.environ.get('READTHEDOCS', None) == 'True'
if not on_rtd:  # only import and set the theme if we're building docs locally   
    import sphinx_rtd_theme  # local installed theme


__author__ = 'Arno-Can Uestuensoez'
__license__ = "Artistic-License-2.0 + Forced-Fairplay-Constraints"
__copyright__ = "Copyright (C) 2016 Arno-Can Uestuensoez" \
                " @Ingenieurbuero Arno-Can Uestuensoez"
__version__ = '0.1.37'
__uuid__ = "7add5ded-c39b-4b6e-8c87-1b3a1c150ee9"

__docformat__ = "restructuredtext en"


#
# add path for temporary tools required for this configuration
#
sys.path.insert(0, os.path.abspath(os.path.dirname(os.getcwd())))
sys.path.insert(0, os.path.abspath(os.getcwd()))


#
# global metadata
#
project = 'platformids'
copyright = __copyright__
license = __license__
version = __version__
uuid = __uuid__


# authoring support
# todo_include_todos = False


#
# required minimal sphinx version
#
# needs_sphinx = '1.0'

#
# required extensions
#
extensions = []
if on_rtd:
    extensions.extend(
        [
            'sphinx.ext.mathjax',
        ]
    )
elif LooseVersion(sphinx.__version__) < LooseVersion('1.4'):
    extensions.extend(
        [
            'sphinx.ext.pngmath',
        ]
    )
else:
    extensions.extend(
        [
            'sphinx.ext.imgmath',
        ]
    )

extensions.extend(
    [
        'matplotlib.sphinxext.plot_directive',
        'sphinx.ext.autodoc',
        'sphinx.ext.doctest',
        'sphinx.ext.githubpages',
        'sphinx.ext.ifconfig',
        'sphinx.ext.inheritance_diagram',
        'sphinx.ext.napoleon',
        'sphinx.ext.todo',
        'sphinx.ext.viewcode',

        'setupdocx.sphinx.ext.imagewrap',
        'setupdocx.sphinx.ext.literalincludewrap',
    ]
)


#
# master document of toctree
#
master_doc = 'index'

#
# source_suffix = ['.rst', '.md']
#
source_suffix = '.rst'

#
# language for generated text by sphinx
#
# language = None

#
# patterns to ignore - relative to source directory
# (affects also html_static_path and html_extra_path)
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# style for syntax highlighting
pygments_style = 'sphinx'


###############################
#                             #
#        *** html ***         #
#                             #
###############################


#
# theme name
#
# html_theme = 'read_the_docs'
html_theme = 'sphinx_rtd_theme'                                              


#
# logo and favicon
#
html_logo = "_static/logo.png"
html_favicon = "_static/favicon.ico"  # 64x64 - 4bit/16    

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
html_use_smartypants = True

#
# search paths - relative to the build directory + target directory
#
# html_static_path = ['_static']
# html_tepmplate_path = ['_templates']
# html_theme_path = ['_themes']

if not on_rtd:  # only import and set the theme if we're building docs locally   
    html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]                   


#
# custom sidebar templates
#
#
# The default sidebars (for documents that don't match any pattern) are
# defined by theme itself.
#
#   html_sidebars = {
#      default: ``['localtoc.html', 'relations.html', 'sourcelink.html', 'searchbox.html']``
#   }
#


#
# html options
#
html_theme_options = {
    'canonical_url': '',
    # 'analytics_id': 'UA-XXXXXXX-1',  #  Provided by Google in your dashboard
    'logo_only': True,
    'display_version': True,
    'prev_next_buttons_location': 'bottom',
    'style_external_links': False,
    # 'vcs_pageview_mode': '',
    # 'style_nav_header_background': 'white',
    
    # Toc options
    'collapse_navigation': True,
    'sticky_navigation': True,
    'navigation_depth': 6,
    'includehidden': True,
    'titles_only': False
}



if not on_rtd:  # only import and set the theme if we're building docs locally   
    def setup(app):
        app.add_stylesheet('custom.css')  # someone(?) inserts "_static"
        
        app.add_config_value('apiref', os.environ.get('DOCX_APIREF', '0'), True)

#         if os.environ.get('DOCX_APIREF') == '1':
#             # create API reference, activates 'quick navigation' menu entry
#             app.add_config_value('apiref', '1', True)
# 
#         else:
#             app.add_config_value('apiref', '0', True)


else:                                                                            
    html_context = {                                                             
        'css_files': [                                                           
            'https://media.readthedocs.org/css/sphinx_rtd_theme.css',            
            'https://media.readthedocs.org/css/readthedocs-doc-embed.css',       
            '_static/custom.css',                                       
        ],                                                                       
    }
    
    

