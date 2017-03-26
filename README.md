pyinstaller.github.io
=====================

Basic Workflow
---------------------

```
make venv VENVDIR=/tmp/py-web
source /tmp/py-web/bin/activate
… hack, hack, hack
make html
xdg-open _build/html/index.html

… when finished
git commit …
git push
make upload
```


How it works
---------------------

This repository contains two branches:

* `source` (the branch you are currently viewing) holds the source of the
  web-site.

* `master` holds the files to be served.

We are using Github Pages for serving our static web-site. This imposes the
restriction that the file to be served life in the `master` branch.

The HTML files are generated using sphinx.

For easily updating the `master` branch, we use a nice trick and a *git
worktree*. A *git worktree* basically is a directory where a different branch
of the repository is checked out, but is still connected to the same
repository. So in the current directory we have the `source` branch, while the
`master` branch is checkout to `_build/html`, where the html files will be
created.

```
git worktree add _build/html gh-pages
find _build/html -mindepth 1 -not -name .git\* -delete
make html
cd _build/html
git add --all
git commit -m 'Website update.'
cd -
```

The `make upload` does this and takes care of some other housekeeping.


Initial setup
-------------------------------------

If you want to set up a repository like this one, here are the steps:

```
export GIT_DIR=$PWD/.git
rm -rf _build/html
mkdir -p _build/html
cd _build/html
git branch -D gh-pages
git checkout --orphan gh-pages
git rm -r .

echo > .gitignore "#"        # Create some file to commit
echo >>.gitignore .buildinfo
echo >>.gitignore _sources/  # If you want to ignore it, of course
git add .gitignore
git commit -m 'Initial Commit'
git checkout master
cd -
rm -rf _build/html
unset GIT_DIR
```
