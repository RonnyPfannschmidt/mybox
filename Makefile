
fetch_deps:
	./bower install

clean_deps:
	rm -rf node_modules bower_components

upgrade_envenv:
	pip install -U -r requirements.dev.txt

refresh: clean_deps fetch_deps upgrade_envenv

check:
	flake8 --max-complexity 8 *.py mybox testing

test:
	py.test

serve:
	python -m mybox
