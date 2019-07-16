.PHONY: all serve clean

all: clean serve

clean:
		rm -rf **/*/dist/

serve:
		FLASK_DEBUG=1 FLASK_ENV=development flask run --host=0.0.0.0
