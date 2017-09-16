

Features
================

* Packaging of Python programs into standard executables, that work
  on computers without Python installed.

* Multi-platform: works under

  - Windows (32-bit and 64-bit),
  - Linux (32-bit and 64-bit),
  - Mac OS X (32-bit and 64-bit),
  - contributed suppport for FreeBSD, Solaris, HPUX, and AIX.

* Multi-version: supports Python 2.7 and Python 3.3, 3.4 and 3.5.

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

* Full single-file Egg-support: required .egg files are automatically
  inspected for dependencies and bundled, and all the egg-specific features
  are supported at runtime as well (entry points, etc.).

* Partial directory Egg-support: required .egg directories are automatically
  inspected for dependencies and bundled, but egg-specific features will not
  work at runtime.

* Automatic support for binary libraries used through `ctypes`
  (see the :ref:`ctypes-dependency-support` for details).

* Support for automatic binary packing through the well-known
  `UPX compressor <https://upx.github.io/>`_.

* Optional console mode (see standard output and standard error at
  runtime).

Windows-specific features
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Support for code-signing executables (see `Recipe Win Code Signing`__ for
  details).

  __ https://github.com/pyinstaller/pyinstaller/wiki/Recipe-Win-Code-Signing

* Full automatic support for CRTs: no need to manually distribute
  MSVCR*.DLL, redist installers, manifests, or anything else; *true*
  one-file applications that work everywhere! (But see the :ref:`restriction
  when building on Windows 10 <manual:Platform-specific Notes - Windows>`.)

* Selectable executable icon.

* Fully configurable version resource section and manifests in
  executable.

* Configurable .exe requirement running as administrator - UAC admin.


Mac-specific features
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Support for .app bundles.

* Support for code-signing: created .app bundles can be signed by
  :program:`codesign` (see `Recipe OSX Code Signing`__ for details.

  __ https://github.com/pyinstaller/pyinstaller/wiki/Recipe-OSX-Code-Signing


.. _ctypes-dependency-support:

`ctypes` Dependencies Support
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

`ctypes` is a foreign function library for Python, that allows calling
functions present in shared libraries. Those libraries are not imported as
Python packages, because they are not picked up via Python imports: their path
is passed to `ctypes` instead, which deals with the shared library directly;
this caused <1.4 PyInstaller import detect machinery to miss those libraries,
failing the goal to build self-contained PyInstaller executables::

  from ctypes import *
  # This will pass undetected under PyInstaller detect machinery,
  # because it's not a direct import.
  handle = CDLL("/usr/lib/library.so")
  handle.function_call()


Solution in PyInstaller
----------------------------

PyInstaller contains a pragmatic implementation of `ctypes` dependencies: it
will search for simple standard usages of `ctypes` and *automatically* track and
bundle the referenced libraries. The following usages will be correctly
detected::

  CDLL("library.so")
  WinDLL("library.so")
  ctypes.DLL("library.so")
  cdll.library # Only valid under Windows - a limitation of ctypes, not PyInstaller's
  windll.library # Only valid under Windows - a limitation of ctypes, not PyInstaller's
  cdll.LoadLibrary("library.so")
  windll.LoadLibrary("library.so")

More in detail, the following restrictions apply:

* **Only libraries referenced by bare filenames (e.g. no leading paths) will
  be handled**. Handling absolute paths would be impossible without modifying
  the bytecode as well (remember that while running frozen, `ctypes` would keep
  searching the library at that very absolute location, whose presence on the
  host system nobody can guarantee), and relative paths handling would require
  recreating in the frozen executable the same hierarchy of directories
  leading to the library, in addition of keeping track of which the current
  working directory is;

* **Only library paths represented by a literal string will be detected and
  included in the final executable** PyInstaller import detection works by
  inspecting raw Python bytecode, and since you can pass the library path to
  `ctypes` using a string (that can be represented by a literal in the code, but
  also by a variable, by the return value of an arbitrarily complex function,
  etc...), it's not reasonably possible to detect *all* `ctypes` dependencies;

* **Only libraries referenced in the same context of `ctypes'` invocation will
  be handled**.

We feel that it should be enough to cover most `ctypes'` usages, with little
or no modification required in your code. If you think, |PyInstaller| should
do more by itself, please :ref:`help improving <manual:how-to-contribute>`
|PyInstaller|.


Restrictions
--------------

The `ctypes` detect system at ``Analysis()`` time is based on
``ctypes.util.find_library()``. This means that you have to make sure that
while performing ``Analysis()`` and running frozen, all the environment values
``find_library()`` uses to search libraries are aligned to those when running
un-frozen. Examples include using :envvar:`LD_LIBRARY_PATH` or
:envvar:`DYLD_LIBRARY_PATH` to widen find_library scope.


.. include:: _common_definitions.txt
