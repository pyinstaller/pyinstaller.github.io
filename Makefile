
all: index.html

%.html: %.rst
	rst2html --embed-stylesheet --stylesheet-path=html4css1.css,./default.css,./website.css  $< > $@

clean:
	rm index.html
