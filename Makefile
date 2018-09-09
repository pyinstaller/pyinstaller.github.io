# You can set these variables from the command line.
SPHINXOPTS    =
SPHINXBUILD   = sphinx-build
SPHINXPROJ    = PyInstaller
SOURCEDIR     = .
BUILDDIR      = _build
REPOSITORY    = origin

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile clean upload venv

clean:
	rm -rf _build

upload:
	rm -rf _build/html
	git worktree prune
	git worktree add _build/html master
	find _build/html -mindepth 1 -not -name .git\* -delete
	git update-index -q --refresh
	make html
	git describe --dirty=.mod --always > _build/html/_static/build-tag
	cd _build/html && \
	git add --all && \
	git commit -m 'Website update.' && \
	git push $(REPOSITORY)

venv:
	@if test -z "$(VENVDIR)" ; then \
       echo ; echo "Run make venv VENVDIR=/tmp/v34 " ; echo ; false ; fi
	pyvenv "$(VENVDIR)"
	"$(VENVDIR)"/bin/pip install --upgrade pip
	"$(VENVDIR)"/bin/pip install -r requirements.txt
	@echo
	@echo "Now run 'source "$(VENVDIR)"/bin/activate'"

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
