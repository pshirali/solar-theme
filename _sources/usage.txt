========
Usage
========

To use Solar in a Sphinx project

#. Modify ``conf.py`` to include the following::

        import solar_theme

        html_theme = 'solar_theme'

        html_theme_path = [solar_theme.theme_path]

#. Rebuild Sphinx project using::

        make html
