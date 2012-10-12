test:
	python -m doctest first.py
	python -m doctest README.rst
	python test_first.py

.PHONY: test
