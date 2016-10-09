=============================================
Welcome to PyInstaller official website
=============================================

.. container:: sidenote bold

  If you have problems to get your application running, please have a
  look at `If Things Go Wrong`_ and `How to Report Bugs`_, which will
  help us a lot on solving the bug.


PyInstaller is a program that freezes (packages) Python programs into
stand-alone executables, under Windows, Linux, Mac OS X, FreeBSD,
Solaris and AIX. Its main advantages over similar tools are that
PyInstaller works with Python 2.7 and 3.3—3.5, it builds smaller
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


Features
================

* Packaging of Python programs into standard executables, that work
  on computers without Python installed.

* Multiplatform: works under

  - Windows (32-bit and 64-bit),
  - Linux (32-bit and 64-bit),
  - Mac OS X (32-bit and 64-bit),
  - contributed suppport for FreeBSD, Solaris and AIX.

* Multiversion: supports Python 2.7 and Python 3.3, 3.4 and 3.5.

* Flexible packaging mode:

  * Single directory: build a directory containing an executable plus
    all the external binary modules (.dll, .pyd, .so) used by the
    program.

  * Single file: build a single executable file, totally
    self-contained, which runs without any external dependency.

  * Custom: you can automate PyInstaller to do whatever packaging
    mode you want through a simple script file in Python.

* Explicit intelligent support for many 3rd-packages (for hidden
  imports, external data files, etc.), to make them work with
  PyInstaller out-of-the-box (see `Supported Packages`_).

* Full egg support: required .egg files are automatically
  inspected for dependencies and bundled, and all the egg-specific
  features are supported at runtime as well (entry points, etc.).

* Automatic support for binary libraries used through ctypes
  (see the `feature page <features.html#ctypes-dependency-support>`__ for details).

* Support for automatic binary packing through the well-known
  `UPX compressor <http://upx.sf.net/>`_.

* Optional console mode (see standard output and standard error at
  runtime).

Windows-specific features
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Support for `code-signing executables
  <features.html#Windows-code-signing>`__.

* `Full automatic support for CRTs <features.html#python26-win>`__: no
  need to manually distribute MSVCR*.DLL, redist installers,
  manifests, or anything else; *true* one-file applications that work
  everywhere!

* Selectable executable icon.

* Fully configurable version resource section and manifests in
  executable.


Mac-specific features
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* `Support for bundles <features.html#mac-os-compatibility>`__


Downloads
================

The latest stable release of PyInstaller is 3.2.
(`Change Log <https://pyinstaller.readthedocs.io/en/latest/CHANGES.html>`_).


* **Release 3.2**:

  Stable, supports Python 2.7, 3.3–3.5

  - `PyInstaller 3.2 (tar.gz)`__ (sha-256: 7598d4c9f5712ba78beb46a857a493b1b93a584ca59944b8e7b6be00bb89cabc)
  - `PyInstaller 3.2 (zip)`__ (sha-256: e27ad7e840d49924f375d3ffa4e0d67b9340f4d78c8279378dd5f4a89dbf6318)

  __ https://github.com/pyinstaller/pyinstaller/releases/download/v3.2/PyInstaller-3.2.tar.gz
  __ https://github.com/pyinstaller/pyinstaller/releases/download/v3.2/PyInstaller-3.2.zip


* **Development**: supports Python 2.7, 3.3–3.5

  - `Current development code (tar.gz)`__
  - `Current development code (zip)`__

  __ https://github.com/pyinstaller/pyinstaller/tarball/develop
  __ https://github.com/pyinstaller/pyinstaller/zipball/develop


See the `full list of releases
<https://github.com/pyinstaller/pyinstaller/releases>`__ for older
(obsolete) releases.

See `PyInstaller Logos <logos>`__ for marketing materials.

.. comment:

  Quickest tutorial --- comment
  =============================

  Uncompress PyInstaller somewhere (let's call the directory you chose
  ``$PYINST``), then configure it for the first time:

     $ python $PYINST/Configure.py

  Go to your program's directory and run::

   $ python $PYINST/Makespec.py --onefile yourprogram.py
   $ python $PYINST/Build.py yourprogram.spec


  This will generate the bundle in a subdirectory called ``dist``.

  For a more detailed walkthrough, see the `manual
  <https://pyinstaller.readthedocs.io/>`_].



Documentation
================

* Documentation for version 3.2:
  `html <https://pyinstaller.readthedocs.io/>`__,
  `pdf <https://rtfd.io/projects/pyinstaller/downloads/pdf/stable/>`__

* Manual for development version:
  `html <https://pyinstaller.readthedocs.io/latest/>`__,
  `pdf <https://rtfd.io/projects/pyinstaller/downloads/pdf/latest/>`__.

* See the list of `Supported Packages`_

* Read our FAQ_ and have a look at the Recipes_.

* If your packed application does not run as expected, please read
  `If Things Go Wrong`_.


License
==================

.. role:: bolditalic


PyInstaller is distributed under the GPL license (see the file
`doc/LICENSE.GPL <https://github.com/pyinstaller/pyinstaller/blob/develop/doc/LICENCE.GPL?raw=true>`_
in the source code), with a :bolditalic:`special exception` **which allows to use
PyInstaller to build and distribute non-free programs** (including
commercial ones). In other words, you have no restrictions in
**using** PyInstaller as-is, but any kind of **modifications** to it
will have to comply with the GPL license. See also our FAQ_.


Support
================

.. container:: bold

  If you have problems to get your application running, please have a
  look at `If Things Go Wrong`_ and `How to Report Bugs`_, which will
  help us a lot on solving the bug.

Mailing List
~~~~~~~~~~~~~~~~

* `PyInstaller Mailing List
  <http://groups-beta.google.com/group/PyInstaller>`_,
  also available at
  `Gmane <http://dir.gmane.org/gmane.comp.python.pyinstaller>`_,
  `The Mail Archive
  <http://www.mail-archive.com/pyinstaller@googlegroups.com/>`_ and
  `Nabble <http://pyinstaller.47505.n6.nabble.com/>`_

* To subscribe to the mailing list, send an empty e-mail to
  `pyinstaller+subscribe@googlegroups.com
  <mailto:pyinstaller+subscribe@googlegroups.com>`_ (you don't need a
  Google Account nor GMail! It's just a regular mailing list, use any
  e-mail address you wish).

IRC Channel
~~~~~~~~~~~~~~~~

* IRC channel **#pyinstaller** at `freenode <http://freenode.net/>`_
  also available online at `IRC webchat
  <http://webchat.freenode.net/?channels=pyinstaller&prompt=1>`_


Bug reports
~~~~~~~~~~~~~~~~

Look at the `list of open bugs
<https://github.com/pyinstaller/pyinstaller/issues>`_. You can report
bugs either anonymously or after registering to this website. If you
register, you will be able to followup on the tickets and receive
notifications.


Development
================

We are happy about contributions. `How to Contribute <how-to-contribute.html>`__ should
provide all information you need.

Source Code Repository
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* You may browse the current repostory at the `Repository Browser
  <https://github.com/pyinstaller/pyinstaller/>`_.

* Or you may check out the current version by running::

    git clone https://github.com/pyinstaller/pyinstaller.git


If you are interested in the "core" development, including tools and
processes, please refer to the Development_ section.


Maintainers
~~~~~~~~~~~~~~~~

* PyInstaller is currently maintained by Martin Zibricky, `Hartmut
  Goebel <http://www.crazy-compilers.com>`_, David Cortesi and David
  Vierra.

  The project was founded by `Giovanni Bajo
  <http://giovanni.bajo.it>`_ (rasky@develer.com, `@giovannibajo
  <http://twitter.com/giovannibajo>`_).
  Installer.

We would like to thank Gordon McMillan who wrote the original Python
Installer, and William Caban for his initial development and
maintenance effort without which PyInstaller would not exist today.

.. _Development: development.html
.. _FAQ: faq.html
.. _`How to Report Bugs`: how-to-report-bugs.html
.. _`If Things Go Wrong`: if-things-go-wrong.html
.. _Recipes: https://github.com/pyinstaller/pyinstaller/wiki/Recipes
.. _`Projects using PyInstaller`: https://github.com/pyinstaller/pyinstaller/wiki/Projects-Using-PyInstaller
.. _`Supported Packages`: https://github.com/pyinstaller/pyinstaller/wiki/Supported-Packages
