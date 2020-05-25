lint:
	-flake8 *.py
	-pylint *.py --disable=C0114,C0115,C0116

test:
	pytest

install:
	@echo 'Make sure to run as a privileged user'
	@echo
	chmod +x rpn.py
	ln -fs `realpath ./rpn.py` /usr/bin/rpn

uninstall:
	@echo 'Make sure to run as a privileged user'
	@echo
	rm /usr/bin/rpn
