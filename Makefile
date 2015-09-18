
all: index.html


%.html: %.rst default.css website.css
	rst2html --embed-stylesheet --stylesheet-path=html4css1.css,./default.css,./website.css  $< > $@

clean:
	rm -f index.html
