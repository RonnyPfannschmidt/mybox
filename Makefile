BROWSER=PhantomJS

fetch_deps:
	./bower install

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

robot_test:
	mkdir -p selenium_result
	pybot -d selenium_result --variable BROWSER:${BROWSER} testing/atest


serve:
	PYTHONPATH=. python -m mybox
