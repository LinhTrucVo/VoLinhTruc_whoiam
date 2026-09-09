# -- Path setup --------------------------------------------------------------

import os

# -- Project information -----------------------------------------------------

project = 'VoLinhTruc_whoiam'
copyright = '2026, Vo Linh Truc'
author = 'Vo Linh Truc'
release = '1.0'

# -- General configuration ---------------------------------------------------

extensions = [
    'sphinxcontrib.plantuml',
]

plantuml = 'java -jar {}'.format(
    os.path.join(os.path.dirname(__file__), 'plantuml/plantuml-1.2025.7.jar')
)
plantuml_output_format = 'svg'

templates_path = ['_templates']
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------

html_theme = 'sphinx_rtd_theme'
html_static_path = []
