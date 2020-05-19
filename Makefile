lint:
	-flake8 *.py
	-pylint *.py

test:
	pytest
