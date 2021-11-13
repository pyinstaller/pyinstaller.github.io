.. _main-page:

.. image:: logos/pyinstaller-draft1c-header-trans.png
   :alt: PyInstaller official website

.. include:: _fundraisingbox.txt

.. container:: bold leadtext

   |PyInstaller| freezes (packages) Python applications
   into stand-alone executables,
   under Windows, GNU/Linux, Mac OS X, FreeBSD, Solaris and AIX.

.. container:: sidenote bold

  If you have problems to get your application running, please have a
  look at `If Things Go Wrong`_ and `How to Report Bugs`_, which will
  help us a lot on solving the bug.

PyInstaller's main advantages over similar tools are that
PyInstaller works with Python 3.6 or newer, it builds smaller
executables thanks to transparent compression, it is fully
multi-platform, and use the OS support to load the dynamic libraries,
thus ensuring full compatibility.

The main goal of PyInstaller is to be **compatible with 3rd-party
packages out-of-the-box**. This means that, with PyInstaller, all the
required tricks to make external packages work are already
**integrated within PyInstaller itself** so that there is no user
intervention required. You'll never be required to look for tricks in
wikis and apply custom modification to your files or your setup
scripts. As an example, **libraries like PyQt, Django or matplotlib
are fully supported**, without having to handle plugins or external
data files manually. Check our compatibility list of `Supported Packages`_
for details.

Feel free to join us in the effort! Please consult our Roadmap to
check our plans. Also usage reports are welcomed: let us know if
PyInstaller works for you and how, or what problems you found in using
it.

Check our list of `Projects using PyInstaller`_.


PyInstaller Quickstart
=============================

Install PyInstaller from PyPI::

  pip install pyinstaller

Go to your program's directory and run::

   pyinstaller yourprogram.py


This will generate the bundle in a subdirectory called ``dist``.

For a more detailed walkthrough, see the `manual
<https://pyinstaller.readthedocs.io/>`_.


.. toctree::
   :maxdepth: 1
   :hidden:

   features
   downloads
   documentation
   support
   license
   funding
   development
   logos/index


.. include:: _common_definitions.txt
