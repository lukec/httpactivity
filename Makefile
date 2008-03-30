all: xo.js

xo.js: xo-code.js Makefile
	cat jquery-1.2.3.js > xo.js
	cat xo-code.js >> xo.js
