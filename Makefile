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

.PHONY: help Makefile clean upload

clean:
	rm -rf _build/html

upload:
	rm -rf _build/html
	git worktree prune
	git worktree add _build/html master
	find _build/html -mindepth 1 -not -name .git\* -delete
	make html
	cd _build/html && \
	git add --all && \
	git commit -m 'Website update.' && \
	git push $(REPOSITORY)


# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
