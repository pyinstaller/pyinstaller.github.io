#!/usr/bin/env python3
#-----------------------------------------------------------------------------
# Copyright (c) 2005-2018, PyInstaller Development Team.
#
# Distributed under the terms of the GNU General Public License with exception
# for distributing bootloader.
#
# The full license is in the file COPYING.txt, distributed with this software.
#-----------------------------------------------------------------------------
"""
Update version numbers and sha256 checksums in the website files
(downloads.rst) and the Sphinx configuration file (conf.py).
"""

import os
import io
import re
import argparse
import subprocess
import glob
import pkginfo
import hashlib

BASEDIR = os.path.normpath(os.path.join(os.path.dirname(__file__), ".."))
SPHINX_CONF = os.path.join(BASEDIR, "conf.py")
DOWNLOADS_RST = os.path.join(BASEDIR, "downloads.rst")

COMMIT_MESSAGE = "Update for release {latest_version}."

VERSION_PATTERN = re.compile(r"""
^\s*
(version|release)
\s*=\s*
['"](?P<V>.*?)['"]
""", re.VERBOSE+re.MULTILINE)


def dist_get_latest_release(distdir):
    if not os.path.isdir(distdir):
        raise SystemExit("Error: %d does not exist or is not a directory."
                         % distdir)
    digests = {}
    for filename in glob.glob(os.path.join(distdir, "*")):
        if filename.endswith('.tar.gz'):
            type = "tar.gz"
            meta = pkginfo.SDist(filename)
        elif filename.endswith('.whl'):
            type = "wheel"
            meta = pkginfo.Wheel(filename)
        else:
            continue
        version = meta.version
        sha2_hash = hashlib.sha256()
        with open(filename, "rb") as fp:
            for content in iter(lambda: fp.read(io.DEFAULT_BUFFER_SIZE), b''):
                sha2_hash.update(content)
        digests[filename] = digests[type] = sha2_hash.hexdigest()
    print(version, digests)
    return version, digests


def get_preceeding_version():
    with open(SPHINX_CONF) as fh:
        conf = fh.read()
    m = VERSION_PATTERN.search(conf)
    if not m:
        raise SystemExit("No version found in %s" % SPHINX_CONF)
    return m.group('V')


def update_sphinx_conf(preceeding, latest):

    def replace(m):
        return m.string[m.start():m.end()].replace(preceeding, latest)

    with open(SPHINX_CONF) as fh:
        text = fh.read()
    text = VERSION_PATTERN.sub(replace, text)
    with open(SPHINX_CONF, "w") as fh:
        fh.write(text)


def update_download_rst(preceeding, latest, digests):

    DOWNLOADS_PATTERN = re.compile(r"""
    (PyInstaller (\s+is)?
    |Release)
    \s+""" + preceeding, re.VERBOSE)

    def replace(m):
        return m.string[m.start():m.end()].replace(preceeding, latest)

    with open(DOWNLOADS_RST) as fh:
        lines = fh.readlines()
    for i, line in enumerate(lines):
        l = line.lstrip()
        if l.startswith('__ https://github.com/pyinstaller/pyinstaller/'
                        'releases'):
            lines[i] = line.replace(preceeding, latest)
        elif l.startswith(".. |Release-Tar-sha256|"):
            lines[i] = line.rsplit(None, 1)[0] + " " + digests["tar.gz"] + "\n"
        elif l.startswith(".. |Release-Wheel-sha256|"):
            lines[i] = line.rsplit(None, 1)[0] + " " + digests["wheel"] + "\n"
        else:
            lines[i] = DOWNLOADS_PATTERN.sub(replace, line)

    with open(DOWNLOADS_RST, "w") as fh:
        fh.writelines(lines)


parser = argparse.ArgumentParser()
parser.add_argument('distdir', metavar="dist-directory",
                    help="Directory containing the distribution files "
                    "as uploaded to PyPI.")
args = parser.parse_args()


preceeding_version = get_preceeding_version()
latest_version, digests = dist_get_latest_release(args.distdir)

update_sphinx_conf(preceeding_version, latest_version)
update_download_rst(preceeding_version, latest_version, digests)

os.chdir(BASEDIR)
subprocess.call(["git", "diff", "--color-words=."])

#subprocess.call(["git", "grep", "-F", "-I", "-O", "--heading", preceeding_version])

out = subprocess.check_output(["git", "grep", "-F", "-I",
                               "--heading", "--break", preceeding_version],
                              universal_newlines=True)
if out.strip():
    #import pdb ; pdb.set_trace()
    print("Old version can still be found here:")
    for l in out.splitlines(False):
        if len(l) > 75:
            print(l[:75], '...')
        else:
            print(l)
    print()

while 1:
    try:
        res = input("Okay to commit (Y/n)? ")
    except EOFError:
        res = "n"
        print("*** Aborted.")
    else:
        res = res.strip().lower() or "y"
    if res and res[0] in "yn":
        res = res[0]
        break
    print("Invalid answer. Please anser `y` for yes or `n` for no.")

if res == "y":
    subprocess.call([
        "git", "commit", "-a", "-m", COMMIT_MESSAGE.format(**globals())])
