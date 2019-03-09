init:
	python3 -m pip install --user virtualenv
	python3 -m virtualenv env
	pip3 install -r requirements.txt --user
	pip3 install nose2
test:
	nose2 -v -C --coverage ./sample tests

.PHONY: init test
