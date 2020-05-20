lint:
	-flake8 *.py
	-pylint *.py --disable=C0114,C0115,C0116

test:
	pytest
