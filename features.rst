

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
  `UPX compressor <https://upx.github.io/>`_.

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



.. include:: _common_definitions.txt
