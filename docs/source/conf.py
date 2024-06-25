# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys

sys.path.insert(0, os.path.abspath('../..'))

# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'tool template'
copyright = '2024, seanhu'
author = 'seanhu'
release = 'v0.0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
    'recommonmark',
]

autodoc_default_options = {
    'member-order': 'bysource',  # 按代码顺序组织文档
    'private-members': True,  # 展示私有方法及属性
    'special-members': True,  # 展示魔术方法
    'undoc-members': True,  # 没有docstrings的方法将不展示
    'show-inheritance': True,  # 默认展示类和函数的 点'.'分层级
    'exclude-members': '__dict__',  # 排除不展示魔术方法__dict__,
}

autodoc_mock_imports = ['_tkinter']

templates_path = ['_templates']
exclude_patterns = []

language = 'zh_CN'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# html_theme = 'alabaster'
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
