all: xo.js

clean:
	rm xo.js *.pyc

xo.js: xo-code.js Makefile
	cat jquery-1.2.3.js > xo.js
	cat xo-code.js >> xo.js