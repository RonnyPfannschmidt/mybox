fetch_deps:
	npm install
	bower install
	tox -e dev -rm`

clean:
	rm -rf node_modules bower_components
	py.cleanup

upgrade_envenv:
	pip install -U -r requirements.dev.txt

refresh: fetch_deps upgrade_envenv

check:
	flake8 --max-complexity 8 *.py mybox testing

test:
	py.test

serve:
	python -m mybox
