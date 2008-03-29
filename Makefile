JS_TARGET=web/xo.js

all: $(JS_TARGET)

clean:
	rm -f $(JS_TARGET) *.pyc

web/xo.js: web/xo-code.js Makefile
	cat web/jquery-1.2.3.js > $(JS_TARGET)
	cat web/xo-code.js >> $(JS_TARGET)
