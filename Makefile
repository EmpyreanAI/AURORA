init:
	pip3 install -r requirements.txt --user
	sudo easy_install nose
test:
	python3 -m "nose"

.PHONY: init test
