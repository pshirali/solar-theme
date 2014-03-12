Preview
=======

Styles
------
* List element 1
* List element 2

Code snippet::

	from fabric.api import local

	def run_rcc():
		"""Generate resources file"""
		local("pyrcc4 -o resources_rc.py ui/resources.qrc")

	def run_uic():
		"""Process ui file"""
		local("pyuic4 -o ui_window.py ui/window.ui")


Admonition levels
-----------------

Note
....

.. note::

    This is a note!

Hint, Tip
.........

.. hint::

   This can be a hint.

Warning, Important
..................

.. warning::

    There can be warnings too!

Caution, Attention, Danger and Error
....................................

.. attention::

   Requires your attention.